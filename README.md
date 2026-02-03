# 🚀 Me-API Playground (Track A)

A professional backend API built with FastAPI that serves my candidate profile, projects, and work experience. This project fulfills the requirements for the AI Engineer Track A assessment.

## 👤 Candidate Information
- Name: Kratika
- Resume: https://drive.google.com/file/d/1dGmlUV0Zw7cWG8Mb0g8CPhJR3CJjkSAX/view?usp=sharing
- LinkedIn: https://www.linkedin.com/in/kratika-singh-40a3b231b

---

## 🏗️ System Architecture
The system uses a modern RESTful architecture with an in-memory NoSQL-style database for high-speed retrieval.



```mermaid
graph LR
    A[Frontend/Client] -->|HTTP GET/PUT| B(FastAPI Backend)
    B -->|Query/Update| C[(In-Memory DB)]
    B -->|Auto-Docs| D[Swagger UI /docs]
