**GenAI Developer 7-Day Intensive Learning Plan**

---

### **Day 1: FastAPI Basics**
**Goal:** Build simple APIs and understand backend flow.

**Tasks:**
- Install FastAPI + Uvicorn.
- Learn routes (`GET`, `POST`) and JSON handling.
- Test with Postman.
- Mini project: CRUD API for “Todo app” or “Student record”.

**Output:** Working API that can return and accept JSON.

**Resources:**
- FastAPI official docs: https://fastapi.tiangolo.com
- YouTube: FastAPI beginner tutorials

---

### **Day 2: Async & Backend Workflow**
**Goal:** Make APIs faster and ready for AI models.

**Tasks:**
- Learn `async` / `await` in Python.
- Add a POST route to accept chat messages.
- Implement simple validation with Pydantic.

**Output:** FastAPI endpoint that can accept user input.

---

### **Day 3: Introduction to LLMs (Qwen / NeMo)**
**Goal:** Load a model and generate text.

**Tasks:**
- Install and run Qwen / NeMo models locally or via API.
- Generate simple text responses from a prompt.
- Experiment with prompt engineering.

**Output:** Script that takes text input and returns generated output.

---

### **Day 4: Embeddings & Vector Search**
**Goal:** Understand RAG fundamentals.

**Tasks:**
- Learn what embeddings are and how they work.
- Convert text data into embeddings.
- Store embeddings in a vector store (FAISS, Chroma, Pinecone).
- Retrieve top-k relevant documents.

**Output:** Script: input a query, get top relevant data snippets.

---

### **Day 5: Build Mini RAG Chatbot**
**Goal:** Combine backend + LLM + embeddings.

**Tasks:**
- FastAPI endpoint accepts a query.
- Fetch top relevant docs using embeddings.
- Pass context + query to LLM for final answer.
- Return response via API.

**Output:** Simple RAG chatbot working locally.

---

### **Day 6: Polish & Integration**
**Goal:** Make it production-ready for demonstration.

**Tasks:**
- Add multi-turn conversation memory.
- Handle edge cases (empty query, missing docs, API errors).
- Clean code, modular structure (functions & classes).

**Output:** Demo-ready RAG chatbot backend.

---

### **Day 7: Optional Extras / Learning on the Go**
**Goal:** Be prepared for on-the-job learning.

**Tasks:**
- Deploy locally or on cloud (Heroku, AWS EC2, Docker).
- Learn to query other LLM APIs if local model too heavy.
- Experiment with enhancements (summarization, embeddings from PDFs).

**Output:** Solid foundation and working project.

---

### **Tips for This Week**
- Focus on hands-on practice rather than theory.
- Start small: get one endpoint working with LLM first.
- Document what you learn for easy reference.
- Don’t worry about perfection — the goal is practical skills you can show/apply.

