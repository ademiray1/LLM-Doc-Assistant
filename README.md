
# 📄 LLM Doc Assistant

A lightweight, full-stack RAG (Retrieval-Augmented Generation) app that allows users to upload **PDFs, Word documents, PowerPoints, or TXT files**, then ask **natural language questions** or generate **summaries** — powered entirely by **local LLMs via Ollama**.

## 🌐 Live Preview

> Upload a document → Ask a question → Get an intelligent response  
> Powered by: `Flask` + `FastAPI` + `LangChain` + `Ollama` + `FAISS`

---

## 🚀 Features

✅ Upload `.pdf`, `.docx`, `.pptx`, `.txt` files  
✅ Ask contextual questions about your documents  
✅ Summarization and Q&A handled locally with Ollama  
✅ Modular FastAPI backend with LangChain pipeline  
✅ Lightweight Flask UI for easy interaction  
✅ Vectorized document storage using FAISS

---

## ⚙️ Tech Stack

| Layer        | Tool                | Purpose                        |
|--------------|---------------------|--------------------------------|
| UI           | Flask + HTML/CSS    | File upload + prompt input     |
| API          | FastAPI             | Handles prompt & doc logic     |
| LLM          | Ollama (e.g. Mistral)| Local language model inference |
| Embeddings   | Ollama + LangChain  | Vectorizing document chunks    |
| RAG Pipeline | LangChain           | Retrieval-augmented generation |
| Vector Store | FAISS               | In-memory search for retrieval |

---

## 💡 Why Local RAG Matters

Using a local RAG setup like this:

- ✅ Keeps your sensitive documents **private**
- ✅ No cloud API cost, no rate limits
- ✅ Works offline once models are pulled
- ✅ Fully hackable and extendable
- ✅ Built for personal knowledge bases, enterprise docs, or internal tools

---

## 🛠 Setup

1. **Clone the repo**
2. Create virtual environment & activate:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Pull required Ollama models:
   ```bash
   ollama pull mistral
   ollama pull nomic-embed-text
   ```
5. Start services:
   - In one terminal:
     ```bash
     python -m uvicorn fastapi_backend.main:app --reload
     ```
   - In another terminal:
     ```bash
     python flask_ui/app.py
     ```
6. Visit `http://localhost:5000` and enjoy!

---

## 📸 Screenshot

> Example: Upload a PDF agenda → Ask "What is this document about?"  
> ![screenshot](./screenshot.png)

---

## 🧠 TODOs / Next Features

- [ ] ✅ Add **multi-file upload** and multi-document context
- [ ] ✅ Implement **chat-style continuous conversation** (ConversationalRetrievalChain)
- [ ] ✅ Add user-level **API key access and auth**
- [ ] 🌟 Add **offline PDF agent**: extract structured metadata (dates, amounts, names)
- [ ] 🌟 Add **voice-to-question**: Ask questions via microphone input
- [ ] 💡 Add **"doc memory mode"**: Let users upload a file and revisit chat later

---

## 💬 Cool Use Cases

- 📚 **Reading long research papers or contracts** — Skip to what matters with fast, intelligent summaries and contextual Q&A.
- 🏢 **Internal company docs, handbooks, or HR policies** — Ask natural questions instead of digging through pages.
- 🛠 **Factory maintenance manuals or SOPs** — Instantly get step-by-step procedures for tools or machines by asking "How do I reset machine X?" or "What's the PM checklist for tool Y?"
- 🧠 **Personal knowledge base** — Upload all your favorite PDFs, notes, or guides and interact with them like ChatGPT.
- 🧾 **Legal, compliance, and audit docs** — Summarize or extract obligations, dates, clauses from long legal paperwork.
- 🧪 **Scientific papers** — Ask "What is the main hypothesis?" or "What methods were used?" and get contextual answers.

---

## 🙌 Credits

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
