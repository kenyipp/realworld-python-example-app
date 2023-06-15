from pydantic import BaseModel, EmailStr
from typing import Optional

class ApiInputRegistration(BaseModel):
    username: str
    email: str
    password: str
    image: Optional[str]
