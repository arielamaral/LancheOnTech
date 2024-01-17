from pydantic import BaseModel, validator

class Cliente(BaseModel):

    id: int
    nome: str
    cpf: str
    email: str

    @validator('email')
    def validate_email(cls, v):
        if not '@' in v:
            raise ValueError('must be a valid email')
        return v