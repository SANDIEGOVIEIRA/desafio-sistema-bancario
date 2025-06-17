import textwrap

def exibir_menu():
    opcoes = """\n
    ======== SISTEMA BANCÁRIO ========
    [1]\tAdicionar saldo
    [2]\tEfetuar saque
    [3]\tMostrar extrato
    [4]\tCadastrar nova conta
    [5]\tVisualizar contas
    [6]\tCadastrar cliente
    [0]\tEncerrar sessão
    => """
    return input(textwrap.dedent(opcoes))


def adicionar_saldo(saldo, valor, historico, /):
    if valor > 0:
        saldo += valor
        historico += f"Crédito:\tR$ {valor:.2f}\n"
        print("\n✔ Crédito realizado com sucesso!")
    else:
        print("\n⚠ Valor inválido para depósito.")

    return saldo, historico


def efetuar_saque(*, saldo, valor, historico, limite_diario, saques_hoje, max_saques):
    sem_saldo = valor > saldo
    acima_limite = valor > limite_diario
    excedeu_quantidade = saques_hoje >= max_saques

    if sem_saldo:
        print("\n⚠ Falha: Saldo insuficiente.")

    elif acima_limite:
        print("\n⚠ Falha: Limite de saque excedido.")

    elif excedeu_quantidade:
        print("\n⚠ Falha: Limite de saques diários atingido.")

    elif valor > 0:
        saldo -= valor
        historico += f"Débito:\t\tR$ {valor:.2f}\n"
        saques_hoje += 1
        print("\n✔ Saque efetuado com sucesso.")
    else:
        print("\n⚠ Valor de saque inválido.")

    return saldo, historico


def mostrar_extrato(saldo, /, *, historico):
    print("\n========== EXTRATO DE CONTA ==========")
    print("Sem movimentações registradas." if not historico else historico)
    print(f"\nSaldo disponível:\tR$ {saldo:.2f}")
    print("======================================")


def cadastrar_cliente(lista_clientes):
    cpf = input("Digite o CPF (apenas números): ")
    cliente = buscar_cliente_por_cpf(cpf, lista_clientes)

    if cliente:
        print("\n⚠ CPF já cadastrado no sistema.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, nº - bairro - cidade/UF): ")

    lista_clientes.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("✔ Cliente cadastrado com sucesso!")


def buscar_cliente_por_cpf(cpf, clientes):
    filtrados = [c for c in clientes if c["cpf"] == cpf]
    return filtrados[0] if filtrados else None


def gerar_conta(agencia_padrao, numero, clientes):
    cpf = input("Informe o CPF do titular: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if cliente:
        print("\n✔ Conta bancária criada com sucesso!")
        return {
            "agencia": agencia_padrao,
            "numero_conta": numero,
            "cliente": cliente
        }

    print("\n⚠ Cliente não encontrado. Processo cancelado.")


def exibir_contas(lista_contas):
    for c in lista_contas:
        dados = f"""\n
        Agência:\t{c['agencia']}
        Conta Nº:\t{c['numero_conta']}
        Titular:\t{c['cliente']['nome']}
        """
        print("=" * 80)
        print(textwrap.dedent(dados))


def iniciar_sistema():
    MAX_SAQUES = 3
    CODIGO_AGENCIA = "0001"

    saldo_total = 0
    limite_valor_saque = 500
    historico_transacoes = ""
    saques_realizados = 0
    clientes = []
    contas = []

    while True:
        escolha = exibir_menu()

        if escolha == "1":
            valor = float(input("Valor para crédito: "))
            saldo_total, historico_transacoes = adicionar_saldo(saldo_total, valor, historico_transacoes)

        elif escolha == "2":
            valor = float(input("Valor para saque: "))
            saldo_total, historico_transacoes = efetuar_saque(
                saldo=saldo_total,
                valor=valor,
                historico=historico_transacoes,
                limite_diario=limite_valor_saque,
                saques_hoje=saques_realizados,
                max_saques=MAX_SAQUES
            )

        elif escolha == "3":
            mostrar_extrato(saldo_total, historico=historico_transacoes)

        elif escolha == "6":
            cadastrar_cliente(clientes)

        elif escolha == "4":
            numero_conta = len(contas) + 1
            nova_conta = gerar_conta(CODIGO_AGENCIA, numero_conta, clientes)

            if nova_conta:
                contas.append(nova_conta)

        elif escolha == "5":
            exibir_contas(contas)

        elif escolha == "0":
            print("Encerrando o sistema bancário. Até logo!")
            break

        else:
            print("⚠ Opção inválida. Tente novamente.")


iniciar_sistema()
