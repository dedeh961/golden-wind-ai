import streamlit as st
from Utils.EnviarPerguntautil import send_question
from tinydb import TinyDB

db = TinyDB('chat_history.json')

chat_history = db.all()

st.title("Chat com inteligência artificial")

if len(db.all()) > 0:
    if st.button("Resetar o histórico do chat"):
        db.truncate()

        st.experimental_rerun()

for message in chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat = st.chat_input("Digite sua pergunta:")

if chat:
    user_message = {"role": "user", "content": chat}
    chat_history.append(user_message)
    db.insert(user_message)

    with st.chat_message("user"):
        st.markdown(chat)

    response = send_question(chat)

    agent_message= {"role": "ai", "content": response}
    chat_history.append(agent_message)
    db.insert(agent_message)

    with st.chat_message("ai"):
        st.markdown(response)
