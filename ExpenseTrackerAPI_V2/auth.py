from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from dependencies import SECRET_KEY, ALGORITHM, EXPIRATION, get_db

pwd_hash = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password:str)->str:
    return pwd_hash.hash(password)

def check_password(password:str,hashed:str)->bool:
    return pwd_hash.verify(password, hashed)

def create_token(data:dict):
    payload = data.copy()
    expire =  datetime.now(timezone.utc) + timedelta(minutes= int(EXPIRATION))
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY ,algorithm=ALGORITHM)

def refresh_token(data:dict, refresh: timedelta=timedelta(days=7)):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + refresh
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY ,algorithm=ALGORITHM)

