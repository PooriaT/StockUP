# StockUP

A sophisticated AI assistant for stock market analysis and recommendations.

## Overview

StockUP is a web application leveraging advanced AI algorithms to suggest optimal stock trading strategies. It offers users a comprehensive dashboard to track the performance of their stock portfolios. By utilizing the Google Gemeni AI library for predictive analytics and Plotly for interactive data visualization, StockUP empowers users to make informed investment decisions.

**Disclaimer:** This application is for educational and research purposes only. It is not intended to serve as investment advice. StockUP is not responsible for any losses or gains made while using this application.

## Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemeni
- **Package Management**: Poetry
- **Charting Library**: Plotly

## Installation

To get started with StockUP, follow these steps:

1. Install Poetry: 
   ```bash
   pip install poetry
   ```
2. Install project dependencies:
   ```bash
   poetry install
   ```

## Testing

Ensure the reliability of the application by running the following tests and checks:

1. Execute unit tests:
   ```bash
   pytest .
   ```
2. Run code linters:
   ```bash
   poetry run pylint .
   ```
3. Run code formatter:
   ```bash
   poetry run black .
   ```
4. Execute pre-commit hooks:
   ```bash
   poetry run pre-commit run --all-files
   ```

## Docker

For deployment using Docker, execute these commands:

1. Build the Docker image:
   ```bash
   docker build -t stockup-app .
   ```
2. Start the Docker container:
   ```bash
   docker run -p 8501:8501 stockup-app
   ```

+++++++++++++++++++++++
========================

### **1. Project Directory Structure**
We'll structure the project as follows:

```
my-web-app/
│── backend/             # FastAPI backend
│   ├── app/
│   │   ├── main.py      # Entry point for FastAPI
│   │   ├── models/      # Database models (if using a database)
│   │   ├── routers/     # API routes
│   │   ├── services/    # Business logic
│   │   ├── dependencies.py  # Common dependencies
│   │   ├── config.py    # Configuration settings
│   ├── pyproject.toml   # Poetry package configuration
│   ├── poetry.lock      # Poetry lock file
│   ├── .env             # Environment variables
│
│── frontend/            # Svelte frontend
│   ├── src/
│   │   ├── routes/      # Svelte pages
│   │   ├── components/  # Reusable UI components
│   │   ├── main.ts      # Entry file
│   │   ├── App.svelte   # Root Svelte component
│   ├── package.json     # NPM dependencies
│   ├── svelte.config.js # Svelte configuration
│   ├── vite.config.js   # Vite configuration
│   ├── tsconfig.json    # TypeScript configuration
│   ├── node_modules/    # Installed dependencies
│
│── README.md            # Documentation
│── .gitignore           # Ignore unnecessary files
│── .dockerignore        # Ignore unnecessary files in Docker
│── docker-compose.yml   # Docker configuration (if needed)
│── .env                 # Global environment variables
```

---

### **2. Setting Up the Backend (FastAPI with Poetry)**

#### **Step 1: Create Backend with Poetry**
```bash
mkdir my-web-app && cd my-web-app
mkdir backend && cd backend
poetry init
```
(Answer the questions, or use `--no-interaction` for default values.)

#### **Step 2: Install Dependencies**
```bash
poetry add fastapi uvicorn
```

If using a database (e.g., PostgreSQL with SQLAlchemy & Alembic):
```bash
poetry add sqlalchemy psycopg2 alembic
```

#### **Step 3: Create the FastAPI App**
Create `backend/app/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust this for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
```

#### **Step 4: Run the Backend**
```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

### **3. Setting Up the Frontend (Svelte with Vite)**

#### **Step 1: Create Frontend**
```bash
cd ..
mkdir frontend && cd frontend
npm create vite@latest . -- --template svelte
```

#### **Step 2: Install Dependencies**
```bash
npm install
```

#### **Step 3: Create API Call in Frontend**
Modify `frontend/src/routes/+page.svelte`:

```svelte
<script>
    let message = "Loading...";

    async function fetchMessage() {
        const res = await fetch("http://localhost:8000/");
        const data = await res.json();
        message = data.message;
    }

    fetchMessage();
</script>

<h1>{message}</h1>
```

#### **Step 4: Run the Frontend**
```bash
npm run dev -- --host
```
This will run the frontend on `http://localhost:5173`.

---

### **4. Connecting Backend and Frontend**
Your **frontend** makes API calls to `http://localhost:8000/`, and FastAPI allows requests from `http://localhost:5173` thanks to the CORS middleware.

If you deploy, update CORS settings and API URLs accordingly.

---

### **5. Running the Full Stack**
To start everything:
1. Run the backend:
   ```bash
   cd backend
   poetry run uvicorn app.main:app --reload
   ```
2. Run the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

Now open `http://localhost:5173`, and your frontend should fetch data from the FastAPI backend.



===========================================

## **Approach: Serve the Frontend with FastAPI**
A common solution is to **build the frontend as static files** and serve them with FastAPI. This way, you only need to run FastAPI, and it will serve both the API and frontend.

### **Steps to Deploy on Render**
---

### **1. Modify the Backend to Serve the Frontend**
After building the Svelte app, we serve the static files using FastAPI’s `StaticFiles`.

#### **Install Required Package**
```bash
poetry add fastapi[all] 
```

#### **Modify `backend/app/main.py`**
Update `main.py` to serve the frontend:
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Serve frontend from "frontend/dist"
frontend_path = Path(__file__).parent.parent / "frontend" / "dist"
if frontend_path.exists():
    app.mount("/", StaticFiles(directory=str(frontend_path), html=True), name="frontend")
```
---
### **2. Modify the Frontend**
Update the frontend API call in `frontend/src/routes/+page.svelte`:
```svelte
<script>
    let message = "Loading...";

    async function fetchMessage() {
        const res = await fetch("/api");  // No need for localhost:8000
        const data = await res.json();
        message = data.message;
    }

    fetchMessage();
</script>

<h1>{message}</h1>
```

---
### **3. Modify the Dockerfile**
The Dockerfile should:
- **Build the frontend**
- **Copy it into the backend**
- **Run FastAPI**

Create `backend/Dockerfile`:
```dockerfile
# Stage 1: Build the frontend
FROM node:18 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Stage 2: Build the backend
FROM python:3.11 AS backend
WORKDIR /app
COPY backend/pyproject.toml backend/poetry.lock ./
RUN pip install poetry && poetry install --no-dev

# Copy backend and built frontend
COPY backend ./
COPY --from=frontend-build /app/frontend/dist ./frontend/dist

# Expose FastAPI port
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
---
### **4. Deploy on Render**
#### **Step 1: Push to GitHub**
Ensure your repository is structured like this:
```
my-web-app/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── poetry.lock
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
```
Commit and push it to GitHub.

#### **Step 2: Deploy on Render**
1. Go to **Render** → Create a new **Web Service**.
2. Select your GitHub repository.
3. Choose **Docker** as the environment.
4. Set the **Dockerfile path** to `backend/Dockerfile`.
5. Set the **PORT** environment variable to `8000`.
6. Deploy! 
