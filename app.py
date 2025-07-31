from langchain_community.llms import LlamaCpp
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import gradio as gr
import os

model_path = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

loader = TextLoader("data/sample_publication.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(documents)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(texts, embedding)

llm = LlamaCpp(model_path=model_path, n_ctx=2048, n_threads=4, verbose=True)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def ask_ai(question):
    return qa.run(question)

gr.Interface(fn=ask_ai, inputs="text", outputs="text", title="JW Study Assistant (Offline)").launch()
