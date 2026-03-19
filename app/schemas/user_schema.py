from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    passWord: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm: True