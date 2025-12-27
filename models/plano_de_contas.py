from dataclasses import dataclass, field
from models.conta import Conta

@dataclass
class PlanoDeContas:
    contas: dict = field(default_factory = dict)
    
    def adicionar_conta(self, conta: Conta):
        if conta.codigo in self.contas:
            raise ValueError("Conta já existe")
        self.contas[conta.codigo] = conta
        
    def buscar(self, codigo: str) -> Conta:
        return self.contas[codigo]