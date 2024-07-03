from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str

class GetUser(BaseModel):
    id:int
    name: str
    email: str
    password: str