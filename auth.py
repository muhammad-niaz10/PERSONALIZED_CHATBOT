from jose import JWTError, jwt
from passlib.context import CryptContext 
from app.database import session,get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from app.models import Users
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")

def hashing_password(password):
    
    return pwd_context.hash(password[:72])

def verify_password(plain_password,hash_password):
    return pwd_context.verify(plain_password[:72],hash_password)

SECRET_KEY="mysecretkey"
algorithm='HS256'

def token(payload):
    return jwt.encode(payload,SECRET_KEY,algorithm=algorithm)

def token_verify(token):
    return jwt.decode(token,SECRET_KEY,algorithms=[algorithm])


from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
security = HTTPBearer()




def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)
,db:Session=Depends(get_db)):

    payload=token_verify(credentials.credentials)
    user_id = payload.get("sub")

    user = db.query(Users).filter(Users.id==user_id).first()

    return user