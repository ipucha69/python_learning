from pydantic import BaseModel, Field

class RegistrationUser(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=6, max_length=72)

class LoginUser(BaseModel):
    email: str
    password: str