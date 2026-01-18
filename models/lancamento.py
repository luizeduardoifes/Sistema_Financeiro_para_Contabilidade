from dataclasses import dataclass
from datetime import date
from models.conta import Conta

@dataclass
class Lancamento:
    data: date
    conta_debito: Conta
    conta_credito: Conta
    valor: float
    historico: str
    

        
        
    