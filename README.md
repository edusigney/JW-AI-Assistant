# JW Voice Study Assistant 🎙📖

An offline voice-based Bible study assistant built with Whisper, LangChain, Mistral, and Gradio. This project is designed to allow conversational study and research using downloadable publications from [jw.org](https://www.jw.org/) and [wol.jw.org](https://wol.jw.org/), with future plans to automate ingestion of PDFs and offer seamless voice interaction.

---

## ✨ Features

- 🎤 Voice input using OpenAI Whisper
- 🧠 Local LLM (Mistral) for private, fast responses
- 🔍 Vector-based Bible content search with ChromaDB + HuggingFace embeddings
- 🗣 Audio-to-text transcription with Whisper
- 🖥 Simple web UI with Gradio
- 💾 Runs locally — No internet required after setup

---

## 🛠 Technologies Used

- [`whisper`](https://github.com/openai/whisper) – for audio transcription  
- `langchain` + `langchain_community` – framework for chaining LLM and retrievers  
- `llama-cpp-python` – interface for running LLMs like Mistral locally  
- `sentence-transformers` – HuggingFace embeddings for semantic search  
- `chromadb` – persistent vector database  
- `gradio` – UI for voice interaction

---

## 🧪 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/edusigney/JW-AI-Assistant.git
   cd JW-AI-Assistant
