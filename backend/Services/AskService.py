from duckduckgo_search import DDGS
from flask import current_app
from langchain import hub
from langchain.schema import Document
from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langgraph.graph import START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from typing_extensions import List, TypedDict


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


class AskService:
    def __init__(self):
        self.llm = ChatOllama(
            model="llama3.2", base_url=current_app.config["OLLAMA_URL"], temperature=0
        )
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text", base_url=current_app.config["OLLAMA_URL"]
        )
        self.rag_prompt = hub.pull("rlm/rag-prompt")
        self.site_for_search = ""

    def retrieve(self, state: State) -> State:
        docs_content = self.search_with_duckduckgo(state)

        return {"context": docs_content}

    def search_with_duckduckgo(self, state: State) -> dict:
        question = state["question"] + self.site_for_search

        return DDGS().text(question, max_results=4, safesearch=True, region="pt-br")

    def generate(self, state: State) -> State:
        messages = self.rag_prompt.invoke(
            {"question": state["question"], "context": state["context"]}
        )

        response = self.llm.invoke(messages)

        return {"answer": response.content}

    def create_graph(self) -> CompiledStateGraph:
        graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])

        graph_builder.add_edge(START, "retrieve")

        return graph_builder.compile()

    def run(self, question: str) -> str:
        graph = self.create_graph()

        response = graph.invoke({"question": question})

        return response["answer"]
