from fastapi import FastAPI,Depends,HTTPException
from app.database import engine,session,get_db
from app.models import Base,Users
from app.scraper import scrapping
from app.schemas import WebsiteURL,ChatRequest,UserCreate
from app.rag_pipeline import ask
from sqlalchemy.orm import Session
from app.auth import hashing_password
from app.routes.website_routes import router
from app.routes.login import login_router

from app.routes.chat_routes import crouter



app = FastAPI()

app.include_router(router)
app.include_router(crouter)
app.include_router(login_router)


Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"message": "Database connected successfully"}



@app.post("/create_user")
def create_user(data:UserCreate,db:Session=Depends(get_db)):

    user=db.query(Users).filter(Users.email == data.email).first()

    if user:
        raise HTTPException(status_code=400,detail="email already exsisted")

    hash_password=hashing_password(data.password)

    new_user=Users(
        name=data.name,
        email=data.email,
        hashed_password=hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return {"message": "User created successfully", "user_id": str(new_user.id)}


