from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from repo.conta_repo import *
import uvicorn

criar_tabela_remetente()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def login(request: Request):
    return templates.TemplateResponse("conta.html", {"request": request})

@app.post("/contas")
def salvar_contas(request: Request, codigo: str = Form(...),nome: str = Form(...), tipo: str = Form(...), saldo_inicial: float = Form(...), descricao: str = Form(...), ativa: str = Form(...)):
    encapslamento = Conta(codigo=codigo,nome=nome, tipo=tipo, saldo=saldo_inicial, descricao=descricao, ativa=ativa)
    inserir_dado = inserir_conta(encapslamento)
    return templates.TemplateResponse("conta.html", {"request":request, "sucesso": inserir_dado})
    


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
    