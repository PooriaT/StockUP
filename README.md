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

