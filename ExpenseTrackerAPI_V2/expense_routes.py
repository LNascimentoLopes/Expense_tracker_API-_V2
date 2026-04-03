from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from models import User,Expense
from dependencies import verify_token
from schemas import ExpenseCreate,ExpenseUpdate

expense_router = APIRouter(prefix="/expense", tags=["expense"], dependencies=[Depends(verify_token)])

@expense_router.post("/create_expense")
async def create_expense(expense:ExpenseCreate,db:Session = Depends(get_db),current_user:User = Depends(verify_token)):
    current_id = db.query(User).filter(User.email == current_user["sub"]).first()
    date = datetime.now().isoformat()
    add = Expense(description=expense.description, value=expense.value,date=date,user_id=current_id.id)
    db.add(add)
    db.commit()
    db.refresh(add)

    return "success"
@expense_router.get("/list_expenses")
async def list_expenses(db:Session = Depends(get_db),current_user:User = Depends(verify_token)):
    current_id = db.query(User).filter(User.email == current_user["sub"]).first()
    expenses = db.query(Expense).filter(Expense.user_id == current_id.id).all()
    return expenses
@expense_router.delete("/detail_expense/{expense_id}")
async def delete_expenses(expense_id: int,db:Session = Depends(get_db),current_user:User = Depends(verify_token)):
    current_id = db.query(User).filter(User.email == current_user["sub"]).first()
    expenses_delete = db.query(Expense).filter(Expense.id== expense_id, Expense.user_id == current_id.id).first()
    db.delete(expenses_delete)
    db.commit()
    return "success"

@expense_router.put("/update_expense/{expense_id}")
async def update_expenses(content_update:ExpenseUpdate,expense_id: int,db:Session = Depends(get_db),current_user:User = Depends(verify_token)):
    current_id = db.query(User).filter(User.email == current_user["sub"]).first()
    date = datetime.now().isoformat()
    expenses_update = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_id.id).first()
    if not expenses_update:
        raise HTTPException(status_code=401, detail="Expense not found.",)
    expenses_update.description = content_update.description
    expenses_update.value= content_update.value
    expenses_update.date = date
    db.commit()
    db.refresh(expenses_update)
    return "success"
@expense_router.get("/list_by_date")
async def list_by_date(date_start: str, date_end: str,db:Session = Depends(get_db),current_user:User = Depends(verify_token)):
    current_id = db.query(User).filter(User.email == current_user["sub"]).first()
    expenses = db.query(Expense).filter(Expense.user_id == current_id.id,Expense.date <= date_end, Expense.date >= date_start).all()

    if not expenses:
        raise HTTPException(status_code=401, detail="Expense not found.")

    return expenses