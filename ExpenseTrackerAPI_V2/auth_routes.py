

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth import hash_password,create_token,refresh_token,check_password
from schemas import RegisterRequest, LoginRequest
from dependencies import get_db, verify_token
from models import User


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/Login")
async def login(data:LoginRequest,db:Session = Depends(get_db)):
    log_user = db.query(User).filter(User.email == data.email).first()

    if not log_user:
        raise HTTPException(status_code=401, detail="Credential invalid")
    check = check_password(data.password, log_user.hashed_password)
    if not check:
        raise HTTPException(status_code=400, detail="Credential invalid")
    token = create_token({"sub": data.email})
    refresh = refresh_token({"sub": data.email})

    return {"access_token":token, "refresh_token": refresh,"token_type":"bearer"}


@auth_router.post("/Login-form")
async def login_form(forms: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    log_user = db.query(User).filter(User.email == forms.username).first()

    if not log_user:
        raise HTTPException(status_code=401, detail="Credential invalid")
    check = check_password(forms.password, log_user.hashed_password)
    if not check:
        raise HTTPException(status_code=400, detail="Credential invalid")
    token = create_token({"sub": forms.username})

    return {"access_token":token,"token_type":"bearer"}



@auth_router.post("/Register")
async def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    print(user)
    if  user:
        raise HTTPException(status_code=400, detail="User Already Exists")
    else:
        user = User(username=data.username,
                    email=data.email,
                    hashed_password=hash_password(data.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"Result":"User Created"}

@auth_router.get("/refresh")
async def refresh(payload: dict = Depends(verify_token)):

    access_token = create_token(payload)
    return {"access_token":access_token,"token_type":"bearer"}
