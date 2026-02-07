from dataclasses import dataclass
from typing import Optional


@dataclass
class Conta:
    id: int
    codigo: str
    nome: str
    tipo: str # -> (Ativo, Passivo, PL, Receita, Despesa)
    saldo: float = 0.0
<<<<<<< HEAD
    descricao : Optional[str] = None
    ativa: bool
=======
    descricao: Optional[str] = None
    ativa: bool 
>>>>>>> 73f728e2ad4ff55feee9c545c4a5d9f52ec66389
    
    def debitar(self, valor: float):
        self.saldo += valor
        
    def creditar(self, valor: float):
        self.saldo -= valor
    
