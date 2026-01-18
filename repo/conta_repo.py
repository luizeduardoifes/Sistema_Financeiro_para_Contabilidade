from db.connection import obter_conexao
from models.conta import Conta
from sql.conta_sql import *


def criar_tabela_conta():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_CONTA)
    conexao.commit()
    conexao.close()
    
def inserir_conta(conta: Conta) -> Conta:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_CONTA,(conta.codigo, conta.nome, conta.tipo, conta.saldo, conta.descricao, conta.ativa))
    conta.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return conta

def atualizar_conta(conta: Conta) -> bool:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_CONTA,(conta.id,conta.codigo, conta.nome, conta.tipo, conta.saldo, conta.descricao, conta.ativa))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_conta() -> bool:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_CONTA)
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def checagem_conta(codigo: str, nome: str) -> bool:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CHECAGEM_CONTA, (codigo, nome))
    resultado = cursor.fetchone()  
    conexao.close()
    return resultado is not None  