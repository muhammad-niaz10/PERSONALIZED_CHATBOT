from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str



class WebsiteURL(BaseModel):
    url: HttpUrl

class ChatRequest(BaseModel):
    message: str
