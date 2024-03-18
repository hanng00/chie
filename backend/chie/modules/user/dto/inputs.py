from pydantic import BaseModel


class SignUpInput(BaseModel):
    email: str
    password: str


class SignInInput(BaseModel):
    email: str
    password: str
