from pydantic import BaseModel, Field, EmailStr
from dataclasses import dataclass, asdict

class Message(BaseModel):
    message: str = Field(..., description="The message to be sent")
    
class UserSchema(BaseModel):
    username: str = Field(..., description="The username of the user")
    email: EmailStr = Field(..., description="The email of the user")
    password: str = Field(..., description="The password of the user")