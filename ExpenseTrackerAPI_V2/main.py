from fastapi import FastAPI

from expense_routes import expense_router
from auth_routes import auth_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(expense_router)




# @app.get("/expenses")
# def get_expenses():
#     return {"expenses":getData()}
#
# @app.delete("/expenses/{id}")
# def delete_expenses(id:int):
#     return {"expenses":remove_expense_db(id)}
#
# @app.put("/expenses/{id}")
# def update_expenses(id: int, data : ExpenseCreate):
#     return {"expenses":update_expense(id, data)}
#
# @app.get("/expenses/total")
# def get_total_expenses():
#     return {"expenses":sum_all_expenses()}
#
# @app.get("/expenses/month/{month}")
# def get_month_expenses(month:int):
#     return {"expenses":get_expense_by_month(month)}
