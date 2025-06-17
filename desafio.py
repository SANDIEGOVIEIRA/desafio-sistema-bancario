menu_principal = """
Escolha uma operação:

[1] Adicionar fundos
[2] Realizar saque
[3] Ver extrato
[0] Encerrar

>>> """

saldo_atual = 0
limite_saque = 500
registro_movimentacoes = ""
contagem_saques = 0
MAX_SAQUES_DIARIOS = 3

while True:
    escolha = input(menu_principal)

    if escolha == "1":
        deposito = float(input("Digite o valor para depósito: "))

        if deposito > 0:
            saldo_atual += deposito
            registro_movimentacoes += f"Depósito realizado: R$ {deposito:.2f}\n"
        else:
            print("Depósito inválido. Insira um valor positivo.")

    elif escolha == "2":
        saque = float(input("Digite o valor para saque: "))

        if saque > saldo_atual:
            print("Saldo insuficiente para realizar o saque.")

        elif saque > limite_saque:
            print(f"Saque acima do limite permitido (R$ {limite_saque:.2f}).")

        elif contagem_saques >= MAX_SAQUES_DIARIOS:
            print("Você atingiu o número máximo de saques diários.")

        elif saque > 0:
            saldo_atual -= saque
            registro_movimentacoes += f"Saque efetuado: R$ {saque:.2f}\n"
            contagem_saques += 1
        else:
            print("Saque inválido. Insira um valor positivo.")

    elif escolha == "3":
        print("\n========== HISTÓRICO DE TRANSAÇÕES ==========")
        print("Nenhuma movimentação registrada." if not registro_movimentacoes else registro_movimentacoes)
        print(f"Saldo disponível: R$ {saldo_atual:.2f}")
        print("==============================================")

    elif escolha == "0":
        print("Sessão encerrada. Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida do menu.")
