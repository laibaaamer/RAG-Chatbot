import streamlit as st
from rag import ask_question
st.set_page_config(page_title="RAG AI Chatbot",page_icon="🤖",layout="centered")
st.title("🤖 RAG AI Chatbot")
st.write("Ask questions about the company knowledge base.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if (
            message["role"] == "assistant"
            and "sources" in message):
            with st.expander("View Source"):
                for source, document in zip(
                    message["sources"],
                    message["documents"]):
                    st.markdown(f"**{source}**")
                    st.write(document)
user_question = st.chat_input("Ask a question...")
if user_question:
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({
        "role": "user",
        "content": user_question})
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            try:
                answer, sources, documents = ask_question(user_question,st.session_state.messages)
                st.markdown(answer)
                with st.expander("View Source"):
                    for source, document in zip(sources,documents):
                        st.markdown(f"**{source}**")
                        st.write(document)
            except Exception as e:
                answer = (f"Sorry, an error occurred: {e}")
                sources = []
                documents = []
                st.error(answer)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
        "documents": documents
    })