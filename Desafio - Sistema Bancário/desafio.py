menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        print("Depósito")
        deposito = float(input("Insira a quantidade a ser depositada: "))

        if deposito < 0:
            print("Valor inválido, insira um valor válido.")

        else:
            saldo =+ deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

    elif opcao == "2":

        print("Saque")
        saque = float(input("Quanto deseja sacar? "))

        if saque > saldo:
            print("Não é possível realizar o saque pois o usuário não tem saldo disponível")

        elif float(saque) < 500:
            while numero_saques < LIMITE_SAQUES:
                numero_saques += 1
                
                saldo = saldo - float(saque)
                extrato = f"- R$ {saque:.2f}\n"
                break
            
            if numero_saques == LIMITE_SAQUES:
                print("Limite de saque excedido")
        
        else:
            print("Saque inválido!")


    elif opcao == "3":
        print("Extrato")
        print(extrato)
        print(f"R$ {saldo:.2f}")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")