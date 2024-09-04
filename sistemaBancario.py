class Conta:
    limite_saques = 3
    valor_limite = 500
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Deposito realizado com sucesso!")

    def sacar(self, valor):
        if self.limite_saques > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.limite_saques -= 1
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                print("Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de saques excedido!")
    def imprimir_extrato(self):
        for movimentacao in self.extrato:
            print(movimentacao)