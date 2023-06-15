from typing import Optional

from pydantic import BaseModel


class ApiInputRegistration(BaseModel):
    username: str
    email: str
    password: str
    image: Optional[str]
