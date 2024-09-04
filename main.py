from sistemaBancario import *
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

conta = Conta("1182", "1191-0", 1000)

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            conta.depositar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > 0:
            conta.sacar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
        print(f"\nSaldo: R$ {conta.saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")