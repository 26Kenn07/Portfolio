import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

import time

from dotenv import load_dotenv

load_dotenv()

groq_api_key = "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"
HUGGINGFACEHUB_API = "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"

def Jarvis():
    st.title("🤓 Jarvis")

    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Make sure do not give duplicate answers.
        Please provide the most accurate response based on the question
        <context>
        {context}
        <context>

        Questions:{input}
        """
    )

    if "vector_db_ready" not in st.session_state:
        st.session_state.vector_db_ready = False

    if st.button("Chat With Jarvis"):
        with st.spinner("Please wait for few minutes..."):
            vector_embedding()
        st.success("You can chat with Jarvis...")
        st.session_state.vector_db_ready = True

    if st.session_state.vector_db_ready:
        prompt1 = st.text_input("Ask anything about Kirtan: ")

        if prompt1:
            start = time.process_time()
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vector_DB.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)
            response = retrieval_chain.invoke({'input': prompt1})
            response_time = time.process_time() - start
            st.write(response['answer'])

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = HuggingFaceBgeEmbeddings(
            model_name="sentence-transformers/all-MiniLM-l6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        st.session_state.loader = PyPDFDirectoryLoader("Data")
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.documents)
        st.session_state.vector_DB = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

