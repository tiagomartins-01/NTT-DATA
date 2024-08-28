import textwrap

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(deposito, saldo, extrato, /):
    if deposito < 0:
        print("Valor inválido, insira um valor válido.")

    else:
        saldo =+ deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        
    return saldo, extrato

def sacar(*, saque, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    if saque > saldo:
        print("Não é possível realizar o saque pois o usuário não tem saldo disponível")
        
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite de saque excedido")

    elif saque < limite:
        saldo -= saque
        extrato += f"Saque:\tR$ {saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")
        
    else:
        print("Saque inválido!")
               
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario(usuarios):
    cpf = str(input("Insira seu CPF: \n"))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    
    nome = str(input("Digite o seu nome e sobrenome: \n"))
    data_nasc = str(input("Insira sua data de nascimento: (dd-mm-yyyy) \n"))
    endereco = str(input("Insira seu endereço: \n"))

    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

        
    return usuario

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    return conta

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Insira a quantidade a ser depositada: "))
            saldo, extrato = depositar(deposito, saldo, extrato)
        
        elif opcao == "2":
            saque = float(input("Quanto deseja sacar? "))
            saldo, extrato = sacar(
            saque = saque,
            saldo = saldo,
            extrato = extrato,
            numero_saques = numero_saques,
            limite = limite,
            LIMITE_SAQUES = LIMITE_SAQUES,
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)
    
        elif opcao == "4":
            criar_usuario(usuarios=usuarios
            )
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()