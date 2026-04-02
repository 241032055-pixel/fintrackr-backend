from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model (for JSON input)
class Transaction(BaseModel):
    amount: float
    type: str
    category: str

# Store data
transactions = []

# Home route
@app.get("/")
def home():
    return {"message": "Finance API Running 🚀"}

# Add transaction (JSON input)
@app.post("/add")
def add_transaction(txn: Transaction):
    new_txn = {
        "id": len(transactions) + 1,
        "amount": txn.amount,
        "type": txn.type,
        "category": txn.category
    }
    transactions.append(new_txn)
    return {"message": "Transaction added", "data": new_txn}

# Get all transactions
@app.get("/transactions")
def get_transactions():
    return transactions

# Summary
@app.get("/summary")
def get_summary():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }
# Filter transactions
@app.get("/filter")
def filter_transactions(type: str = None, category: str = None):
    result = transactions

    if type:
        result = [t for t in result if t["type"] == type]

    if category:
        result = [t for t in result if t["category"] == category]

    return result


# Recent transactions
@app.get("/recent")
def recent_transactions():
    return transactions[-5:]
    