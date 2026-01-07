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
    
    erro = []
    
    if not codigo:
        erro.append("o código da conta é obrigatório")
        
    if not nome:
        erro.append("o nome da conta é obrigatório")
            
    if tipo not in ["ATIVO", "PASSIVO", "PATRIMONIO", "RECEITA", "DESPESA"]:
        erro.append("o tipo de conta inválido")
            
    try:
        float(saldo_inicial)
        if saldo_inicial < 0:
            erro.append("o saldo inicial da conta não pode ser negativo")
    except ValueError:
        erro.append("o campo saldo_inicial aceita somente números decimais")
            
    if erro:
        return templates.TemplateResponse("conta.html", {"request": request, "erro": erro})
    
    else:
        encapslamento = Conta(codigo=codigo,nome=nome, tipo=tipo, saldo=saldo_inicial, descricao=descricao, ativa=ativa)
        inserir_dado = inserir_conta(encapslamento)
        return templates.TemplateResponse("conta.html", {"request":request, "insert": inserir_dado, "sucesso": "Registro salvo com sucesso"})
    


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
    