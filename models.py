from sqlalchemy import String,Column,Integer,ForeignKey,DateTime,Text
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,index=True)
    name = Column(String)
    email = Column(String,index=True,unique=True,nullable=False)
    hashed_password=Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)

    websites = relationship("Websites",back_populates="user")
    chats = relationship("ChatHistory",back_populates="user")


class Websites(Base):
    __tablename__ = "websites"

    id= Column(Integer,nullable=False,primary_key=True,index=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    url = Column(String)
    status=Column(String,default="processing")
    created_at=Column(DateTime,default=datetime.utcnow)

    user = relationship("Users",back_populates="websites")

class ChatHistory(Base):
    __tablename__ ="chat_history"

    id=Column(Integer,primary_key=True,index=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    message=Column(String)
    response=Column(String)
    mode=Column(String)
    time_stamp=Column(DateTime,default=datetime.utcnow)

    user = relationship("Users",back_populates="chats")


