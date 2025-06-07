import requests
import streamlit as st

API_URL = "http://backend:80/ask"

def send_question(pergunta: str) -> str:
    try:
        http_response = requests.post(API_URL, json={"question": pergunta})

        http_response.raise_for_status()

        llama_response = http_response.json().get("answer", "Sem resposta.")

        return f"Resposta: {llama_response}"

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao se comunicar com o backend: {e}")

    except ValueError:
        st.error("Erro ao processar a resposta do backend.")
