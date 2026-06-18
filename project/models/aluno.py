from pydantic import BaseModel, EmailStr

class AlunoBase(BaseModel):
    nome: str
    email: EmailStr

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True