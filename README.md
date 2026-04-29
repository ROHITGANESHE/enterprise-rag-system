# 🧠 Enterprise RAG System (Amazon Bedrock + Streamlit)

An advanced **Retrieval-Augmented Generation (RAG)** application that allows users to query company documents and receive **accurate, context-aware answers with citations**.

Built using **Streamlit UI + Amazon Bedrock + S3 Knowledge Base**.

---

## 🚀 Features

- 💬 Chat-based interface using Streamlit
- 📄 Upload documents (PDF, TXT, DOCX) to knowledge base
- 🔍 Intelligent document retrieval (RAG)
- 🧠 AI-generated answers using Amazon Bedrock
- 📎 Source citations for transparency
- ⚡ Fast and interactive UI
- 🧹 Clear chat history functionality

---

## 🏗️ Project Architecture


User → Streamlit UI → RAG Pipeline → Amazon Bedrock
↘ Upload Docs → S3 Bucket → Knowledge Base


---

## 📂 Project Structure


enterprise-rag-system/
│
├── app.py # Streamlit UI (Main Application)
├── bedrock_rag.py # RAG logic (query + retrieval)
├── config.py # Configurations (S3, app settings)
├── requirements.txt # Dependencies
└── .env # Environment variables (NOT pushed)


---

## ⚙️ How It Works

1. User enters a question in the UI  
2. Query is sent to RAG pipeline  
3. Relevant documents are retrieved from S3  
4. Amazon Bedrock generates an answer  
5. Answer + citations are displayed  

Example from code: :contentReference[oaicite:0]{index=0}

---

## 🛠️ Installation
git clone https://github.com/your-username/enterprise-rag-system.git
cd enterprise-rag-system

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
🔐 Environment Setup

Create a .env file:

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=your_region
S3_BUCKET_NAME=your_bucket

⚠️ Never push .env to GitHub

▶️ Run the App
streamlit run app.py
📤 Upload Documents
Upload via sidebar
Supported formats: PDF, TXT, DOCX
Files stored in S3 bucket
Used for knowledge retrieval
📸 UI Preview
Chat interface
Document upload panel
Source citation viewer
🧠 Tech Stack
Python
Streamlit
Amazon Bedrock
AWS S3
RAG (Retrieval-Augmented Generation)
💡 Use Cases
Enterprise knowledge assistant
Internal documentation search
Customer support automation
HR policy Q&A bot
⚠️ Important Notes
Ensure AWS permissions are configured
Sync knowledge base after upload
Keep API keys secure
📌 Future Improvements
Authentication system
Multi-user support
Chat history persistence (DB)
Advanced document chunking
UI enhancements
🤝 Contributing

Feel free to fork and improve the project!

👨‍💻 Author

Rohit Ganeshe

⭐ If you like this project

Give it a ⭐ on GitHub!
