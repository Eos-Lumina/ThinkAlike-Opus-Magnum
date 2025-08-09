"""
Chrona Wallet API Endpoints
Implements RESTful endpoints for wallet operations: deposit, withdraw, simulate, transaction history.
"""

from fastapi import APIRouter, HTTPException, Request
from .wallet import ChronaWallet

router = APIRouter()

# In-memory wallet store for demonstration
wallets = {}

@router.post("/wallet/{user_id}/deposit")
def deposit(user_id: str, amount: float):
    wallet = wallets.setdefault(user_id, ChronaWallet(user_id))
    new_balance = wallet.deposit(amount)
    return {"user_id": user_id, "new_balance": new_balance}

@router.post("/wallet/{user_id}/withdraw")
def withdraw(user_id: str, amount: float):
    wallet = wallets.setdefault(user_id, ChronaWallet(user_id))
    try:
        new_balance = wallet.withdraw(amount)
        return {"user_id": user_id, "new_balance": new_balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/wallet/{user_id}/balance")
def get_balance(user_id: str):
    wallet = wallets.setdefault(user_id, ChronaWallet(user_id))
    return {"user_id": user_id, "balance": wallet.get_balance()}

@router.get("/wallet/{user_id}/transactions")
def get_transactions(user_id: str):
    wallet = wallets.setdefault(user_id, ChronaWallet(user_id))
    return {"user_id": user_id, "transactions": wallet.get_transactions()}

@router.post("/wallet/{user_id}/simulate")
def simulate(user_id: str, amount: float, tx_type: str):
    wallet = wallets.setdefault(user_id, ChronaWallet(user_id))
    result = wallet.simulate_transaction(amount, tx_type)
    return result
