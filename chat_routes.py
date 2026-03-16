from fastapi import APIRouter,Depends
from app.schemas import WebsiteURL,ChatRequest
from app.rag_pipeline import ask
from app.auth import get_current_user
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Users,ChatHistory

crouter=APIRouter()

@crouter.post("/chat")
def chat(data:ChatRequest,current_user:Users=Depends(get_current_user),db:Session=Depends(get_db)):

    response=ask(data.message,current_user,db)

    chat=ChatHistory(
        user_id=current_user.id,
        message=data.message,
        response=response["reply"],
        mode=response["mode"]
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)


    return {"reply": response["reply"], "mode": response["mode"]}
