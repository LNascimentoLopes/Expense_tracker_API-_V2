from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

from security import oauth2_scheme
from models import User

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRATION = os.getenv("EXPIRATION")

engine = create_engine(DB_URL)

SessionLocal= sessionmaker (autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    test = db.query(User).filter(User.email == payload["sub"]).first()
    if test:
        return payload
    else:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

