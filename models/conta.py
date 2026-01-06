from dataclasses import dataclass
from typing import Optional

from fastapi import Form

@dataclass
class Conta:
    codigo: str
    nome: str
    tipo: str # -> (Ativo, Passivo, PL, Receita, Despesa)
    saldo: float = 0.0
    descricao : Optional[str] = None
    ativa: Optional[bool] = Form(None)
    
    def debitar(self, valor: float):
        self.saldo += valor
        
    def creditar(self, valor: float):
        self.saldo -= valor
    