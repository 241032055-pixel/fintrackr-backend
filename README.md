# FinTrackr – Finance Backend System

## Overview

FinTrackr is a Python-based backend system built using FastAPI. It allows users to manage financial transactions such as income and expenses and provides summary analytics.

## Features

* Add financial transactions (income/expense)
* View all transactions
* Filter transactions by type and category
* Generate financial summary (income, expense, balance)
* JSON-based API input
* Input validation using Pydantic

## Tech Stack

* Python
* FastAPI
* Uvicorn

## How to Run

1. Install dependencies:
   pip install fastapi uvicorn

2. Run server:
   uvicorn main:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs

## API Endpoints

* GET / → Check API status
* POST /add → Add transaction
* GET /transactions → View all transactions
* GET /summary → Get financial summary
* GET /filter → Filter transactions
* GET /recent → Get recent transactions

## Example Input

{
"amount": 1000,
"type": "income",
"category": "salary"
}

## Output Example

{
"total_income": 3000,
"total_expense": 500,
"balance": 2500
}

## Assumptions

* Data is stored in memory (no database used)
* Designed for demonstration purposes

## Future Improvements

* Database integration (SQLite/PostgreSQL)
* User authentication and roles
* Advanced analytics
