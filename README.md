# Smart Task AI Planner

A full-stack AI-powered productivity system that helps users manage tasks intelligently using automated priority detection and clean workflow management.

This project was built as a structured, production-style system focusing on clarity, correctness, and maintainability rather than feature overload.

---

## Overview

Smart Task AI Planner is a minimal yet well-architected task management system designed to demonstrate clean backend structure, safe API design, and thoughtful AI-assisted decision logic.

The system automatically analyzes task text and assigns priority using an extensible AI-assisted rule engine, while maintaining a simple and reliable user workflow.

---

## Tech Stack

### Backend
- Python  
- Flask (API)  
- SQLAlchemy  
- SQLite  
- Structured logging  

### Frontend
- React  
- Clean component-based UI  

### Other
- REST API design  
- Modular architecture  
- AI-assisted priority engine  
- Error handling and validation  

---

## Key Features
- Create and manage tasks  
- Automatic AI-based priority detection  
- Status tracking (pending/completed)  
- Clean REST API architecture  
- Structured backend with services, routes, and models  
- Logging for observability and debugging  
- Simple, responsive React interface  

---

## System Design Approach

This project was intentionally designed as a small but production-structured system.

### Key engineering decisions
- Clear separation of routes, services, and models  
- Centralized configuration  
- Logging for observability  
- Validation at service layer  
- Extensible AI priority logic  
- Simple predictable API design  

The goal was to prioritize clarity and maintainability over feature volume.

---

## How to Run Locally

Follow these steps to run the project on your system.

### 1. Clone the repository
```bash
git clone https://github.com/dineshkvs1304/smart-task-ai-planner.git
cd smart-task-ai-planner
```

### 2. Start Backend Server
Open a terminal and run:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

Backend will start at:  
http://127.0.0.1:5000  

Test backend health:
http://127.0.0.1:5000/api/health

You should see a success response confirming the backend is running.

---

### 3. Start Frontend (open new terminal)

```bash
cd frontend
npm install
npm start
```

Frontend will run at:  
http://localhost:3000  

---

### 4. Test the Application

Once both backend and frontend are running:

- Create a new task  
- Try using words like **urgent**, **exam**, or **deadline**  
- The system will automatically assign priority  
- Mark the task as completed  
- Verify status updates correctly in the UI  

The SQLite database file will be created automatically inside the backend folder when the server runs.  

---

## AI Usage

AI was used as a development assistant while building this project. I used it primarily to think through architectural structure, improve code clarity, and refine certain implementation decisions.

For example, AI helped me explore better ways to organize the backend into routes, services, and models, improve logging structure, and simplify parts of the priority detection logic. It also helped in reviewing edge cases and improving readability.

However, all code was manually reviewed, tested, and adjusted by me before being finalized. I made sure I understood every part of the implementation and verified the behavior through actual testing in the running system.

AI was used as a productivity tool to enhance development quality — not as a replacement for understanding or engineering judgment.

---

## Future Improvements
- User authentication  
- Deployment (Docker/AWS)  
- Advanced AI scheduling suggestions  
- Unit and integration testing expansion  
- Priority scoring model instead of keyword engine  

---

## Author
**Kandyana Venkata Sai Dinesh**  
B.Tech CSE
