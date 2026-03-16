from fastapi import APIRouter,HTTPException,Depends
from app.schemas import LoginUser
from app.database import session,get_db
from sqlalchemy.orm import Session
from app.auth import verify_password,token
from datetime import datetime, timedelta
from app.models import Users

login_router = APIRouter()

@login_router.post("/login")
def login(data:LoginUser,db:Session=Depends(get_db)):

    user = db.query(Users).filter(Users.email == data.email).first()

    if not user:
        raise HTTPException(status_code=400,detail="invalid credentials")

    if not verify_password(data.password,user.hashed_password): 
        raise HTTPException(status_code=400,detail="invalid credentials")

    expire_time = datetime.utcnow() + timedelta(hours=1)


    payload = {
        "sub": str(user.id),
        "exp": expire_time
    }
    generate_token = token(payload)

    return {"access_token": generate_token, "token_type": "bearer"}


    