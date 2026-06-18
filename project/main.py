from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API do Sistema Educacional Gamificado rodando com sucesso!"}