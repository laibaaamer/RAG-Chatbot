import streamlit as st
from rag import ask_question
st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="centered")
st.title("🤖 RAG AI Chatbot")
st.write("Ask questions about the knowledge base.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
question = st.chat_input("Ask a question...")
if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question})
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        with st.spinner(
            "Searching knowledge base..."):
            try:
                answer, sources, documents = ask_question(question,st.session_state.messages[:-1])
                st.write(answer)
                if sources:
                     with st.expander("📚 View Sources"):
                        for i, (source, document) in enumerate(
                            zip(sources, documents),start=1):
                                st.markdown(f"**Source {i} — {source}**")
                                st.write(document)
                                st.divider()
            except Exception as e:
                st.error(f"Error: {e}")
                answer = ("Sorry, something went wrong.")
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer})