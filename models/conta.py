from dataclasses import dataclass

@dataclass
class Conta:
    codigo: str
    nome: str
    tipo: str # -> (Ativo, Passivo, PL, Receita, Despesa)
    saldo: float = 0.0
    
    def debitar(self, valor: float):
        self.saldo += valor
        
    def creditar(self, valor: float):
        self.saldo -= valor
    