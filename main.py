from datetime import date

from models.conta import Conta
from models.lancamento import Lancamento
from models.plano_de_contas import PlanoDeContas

caixa = Conta("1.1.01", "Caixa", "ATIVO")
capital = Conta("3.1.01", "Capital Social", "PL")

plano = PlanoDeContas()
plano.adicionar_conta(caixa)
plano.adicionar_conta(capital)

lanc = Lancamento(
    data=date.today(),
    conta_debito=caixa,
    conta_credito=capital,
    valor=1000,
    historico="Integralização de capital"
)

lanc.registrar()

print(caixa.saldo)    # 1000
print(capital.saldo)  # -1000
