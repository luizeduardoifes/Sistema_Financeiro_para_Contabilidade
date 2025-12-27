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
    
    def registrar(self):
        if self.valor <= 0:
            raise ValueError("O valor de lançamento tem que ser maior do que o 0.")
        
        self.conta_debito.debitar(self.valor)
        self.conta_credito.creditar(self.valor)
        
        
    