# IAT AI Chatbot 🤖

A simple AI-powered chatbot built for the IAT Networks website using FastAPI and Gemini AI.  
It includes a hybrid response system with static replies for common queries and AI fallback for unknown questions.

---

## 🚀 Features

- FastAPI backend for chat API
- Clean and responsive frontend chat UI
- Hybrid response system:
  - Static responses for common queries (services, contact, etc.)
  - AI fallback using Google Gemini
- Proper error handling and structured responses
- Simple and extendable architecture

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Google Gemini AI (google-genai)
- HTML, CSS, JavaScript

## ⚙️ Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/ankitdevlabs/ias-chatbot.git
cd ias-chatbot
```
### 2. Add production.yaml
```
src->chatbot->production.yaml
inside this add
gemini_api_Kkey=your_api_key_here
```

### 3. Install dependecies
```poetry install```

### 4. Run BE server
```poetry run cli chatbotapi serve```

### 5. run index.html
```
Right click → Open with browser
OR
Copy file path and open in browser
```
