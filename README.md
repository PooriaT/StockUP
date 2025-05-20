# StockUP

## Overview

StockUP is a sophisticated AI assistant for stock market analysis and recommendations. It leverages advanced AI algorithms to suggest optimal stock trading strategies and offers users a comprehensive dashboard to track stock performance.

## Disclaimer

This application is for educational and research purposes only. It is not intended to serve as investment advice. StockUP is not responsible for any losses or gains made while using this application.

## Features

*   Displays historical stock data (1d, 5d, 1mo, 6mo, 1y, 5y).
*   Shows general stock information and latest news.
*   Provides AI-powered analysis and trading recommendations for stocks using Google Gemini.
*   Includes an AI chatbot for specific stock-related queries, also powered by Google Gemini.
*   Homepage features a dashboard for "big seven" tech companies.

## Tech Stack

*   **Backend:** Python, FastAPI, Poetry (for dependency management), Google Gemini API.
*   **Frontend:** Svelte, Vite, TypeScript, Node.js.

## Prerequisites

*   Node.js and npm (or pnpm/yarn)
*   Python (3.9+ recommended)
*   Poetry

## Project Structure

*   `backend/`: Contains the FastAPI application.
*   `frontend/`: Contains the SvelteKit application.

## Setup and Installation

### General

1.  Clone the repository: `git clone <repository-url>`
2.  Navigate to the project directory: `cd <project-name>`

### Backend Setup

1.  Navigate to the backend directory: `cd backend`
2.  Create a virtual environment (optional but recommended if not using Poetry's env management): `python -m venv .venv` and `source .venv/bin/activate` (or `.\.venv\Scriptsctivate` on Windows).
3.  Install dependencies: `poetry install`
4.  Set up environment variables:
    *   Copy `.env.example` to `.env`: `cp .env.example .env`
    *   Add your Google Gemini API Key to `.env`: `GEMINI_API_KEY="YOUR_API_KEY"`

### Frontend Setup

1.  Navigate to the frontend directory: `cd frontend`
2.  Install dependencies: `npm install` (or `pnpm install` / `yarn install`)

## Running the Application

### Backend

1.  Navigate to `backend/`.
2.  Run: `poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### Frontend

1.  Navigate to `frontend/`.
2.  Run: `npm run dev -- --host`
    *   Alternatively, use `npm run dev -- --open` to automatically open the app in a new browser tab.
3.  Access the application in your browser, usually at `http://localhost:5173`.

## Building for Production (Frontend)

To create a production version of the frontend app:

1.  Navigate to `frontend/`.
2.  Run: `npm run build`

You can preview the production build locally (after building) with: `npm run preview`.

## Testing

### Backend

1.  Navigate to `backend/`.
2.  Run unit tests: `pytest .`
3.  Linters/Formatters:
    *   `poetry run pylint .`
    *   `poetry run black .`
    *   `poetry run pre-commit run --all-files`

### Frontend

1.  Navigate to `frontend/`.
2.  Run linter: `npm run lint`
3.  Run formatter: `npm run format`

## Docker Deployment (Simplified)

*   The project includes a `backend/Dockerfile` that can be used to build a container image for the application.
*   This Dockerfile builds the frontend and serves it using the FastAPI backend.
*   Build the image: `docker build -t stockup-app -f backend/Dockerfile .`
*   Run the container: `docker run -p 8000:8000 -e GEMINI_API_KEY="YOUR_API_KEY" stockup-app`

## Contributing

*   Contributions are welcome! Please feel free to open an issue or submit a pull request.
*   Check the `.github/ISSUE_TEMPLATE/` for reporting bugs or requesting features.
*   Follow the existing coding style and ensure tests pass before submitting a PR.
