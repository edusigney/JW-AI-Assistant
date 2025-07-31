import os
import gradio as gr
import whisper
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA

# Load Whisper model
whisper_model = whisper.load_model("base")  # Options: "base", "small", "medium", "large"

# Load embedding and vectorstore
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="bible_vectorstore", embedding_function=embedding)

# Load local LLM
llm = LlamaCpp(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    verbose=False
)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Voice chat function using Whisper
def voice_chat(audio_path):
    result = whisper_model.transcribe(audio_path)
    text = result["text"].strip()
    if not text:
        return "I couldn’t understand anything from the audio."

    response = qa.run(text)
    os.system(f'say "{response}"')  # Optional: comment out if you don't want voice feedback
    return f"You asked: {text}\n\nResponse: {response}"

# Gradio interface
gr.Interface(
    fn=voice_chat,
    inputs=gr.Audio(type="filepath", label="Speak now"),
    outputs="text",
    title="JW Voice Study Assistant"
).launch()
