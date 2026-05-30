# Lumora AI

### Personalized Academic Intelligence Platform for University Learning

---

## Project Overview

Lumora AI is an AI-powered academic learning platform designed to transform university education through intelligent document understanding and personalized learning support.

Students can upload lecture notes, assignments, reference books, lab manuals, and previous year question papers. Lumora AI processes these academic resources and acts as an intelligent academic assistant capable of answering questions, generating study notes, creating examination papers, and supporting examination preparation.

The system combines Retrieval-Augmented Generation (RAG), Natural Language Processing (NLP), Semantic Search, Learning Analytics, and Large Language Models to deliver contextual academic assistance.

---

## Project Domain

Artificial Intelligence
Natural Language Processing
Retrieval-Augmented Generation (RAG)
Educational Technology
Learning Analytics

---

## Objectives

* Build an intelligent academic assistant for universities
* Enable semantic understanding of uploaded educational materials
* Generate academic notes automatically
* Assist students with exam preparation
* Improve learning efficiency through AI
* Demonstrate practical applications of Data Science and NLP

---

## Key Features

### Academic Chatbot

Ask questions directly from uploaded academic materials.

### Multi-PDF Upload

Upload multiple lecture notes, books, and assignments.

### RAG-Based Question Answering

Generate contextual responses using vector retrieval.

### Study Notes Generator

Create structured academic notes instantly.

### Question Paper Generator

Generate examination questions with answers.

### Viva Simulator

Practice oral examinations with AI evaluation.

### Learning Analytics Dashboard

Track academic engagement and usage statistics.

### Knowledge Base

Manage indexed documents and uploaded resources.

### Professional PDF Export

Export generated notes, viva reports, and question papers.

---

## System Architecture

Student Uploads PDFs
↓
Document Parsing (LlamaParse)
↓
Text Extraction
↓
Chunking
↓
Embeddings Generation
↓
FAISS Vector Database
↓
Retriever
↓
Gemini API
↓
Lumora AI Response

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Document Parsing

* LlamaParse

### Embeddings

* sentence-transformers
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### Large Language Model

* Google Gemini API
* gemini-2.5-flash

### Libraries

* streamlit
* llama-parse
* sentence-transformers
* faiss-cpu
* google-generativeai
* pandas
* plotly
* pypdf
* python-dotenv

---

## Project Structure

```plaintext
LumoraAI/

app.py
styles.css
requirements.txt
README.md
.env

uploads/
vectorstore/

exports/
├── notes/
├── exams/
└── viva/

modules/
├── dashboard.py
├── chatbot.py
├── notes_generator.py
├── exam_generator.py
├── viva_simulator.py
├── analytics.py
├── knowledge_base.py

utils/
├── parser.py
├── embeddings.py
├── retriever.py
├── vectorstore.py
├── gemini_chat.py
├── pdf_generator.py
├── analytics_tracker.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd LumoraAI
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
GOOGLE_API_MODEL=gemini-2.5-flash

LLAMA_CLOUD_API_KEY=your_key
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Expected Workflow

1. Upload Academic PDFs
2. Process Documents
3. Ask Questions
4. Generate Study Notes
5. Create Question Papers
6. Practice Viva
7. Export PDFs

---

## Future Enhancements

* Professor Style Mimicking
* Weak Topic Detection
* Personalized Study Planner
* Multi-Course Learning Assistant
* Voice-Based Academic Interaction
* Cloud Deployment

---

## Academic Contribution

Lumora AI demonstrates how Artificial Intelligence and Retrieval-Augmented Generation can improve higher education through intelligent learning support and personalized academic assistance.

---

## Developed By

Namita S, 
MSc Data Science, 
Symbiosis International University.

---

## License

This project is developed for academic and educational purposes.
