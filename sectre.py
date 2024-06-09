import streamlit as st
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.arxiv_toolkit import ArxivToolkit

st.title("Chat with sectre")
st.caption("This app allows to to chat with sectre using OpenAI GPT-4o model")

openai_access_token = st.text_input("OpenAI API key")
if openai_access_token:
    assistant = assistant(
        model="gpt-4o",
        max_tokens=1024,
        temperature=0.9,
        api_key=openai_access_token, tools=[ArxivToolkit()], show_tool_calls=True
    )

query = st.text_input("Enter the search query", type='default')
if query:
    response = assistant.run(query, stream=False)
    st.write(response)
