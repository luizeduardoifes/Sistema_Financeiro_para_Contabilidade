from dataclasses import dataclass
from datetime import date

@dataclass
class Lancamento:
    data: date
    conta_debito: int
    conta_credito: int
    valor: float
    historico: str
    

        
        
    
