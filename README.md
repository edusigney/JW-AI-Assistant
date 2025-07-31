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



---

📘 **Disclaimer**

This is a personal study tool built with educational intent. The data used and referenced is from publicly available, downloadable sources from [jw.org](https://www.jw.org). Please respect their terms of use. This project is not affiliated with any official religious organization.

---

🤝 **Contributing**

Pull requests are welcome. If you’re interested in helping build tools like this for educational or spiritual enrichment, feel free to fork and share ideas.

---

📜 **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
