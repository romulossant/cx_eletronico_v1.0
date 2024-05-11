menu = """
======================================
Qual operação deseja realizar? 

1. Saque
2. Depósito
3. Visualizar Extrato
0. Sair
======================================
"""
menu_extrato = """
Qual extrato deseja visualizar?

1. Saques
2. Depósitos
0. Sair
======================================
"""

from time import sleep

saldo = 0
total_saque = 0
extrato_deposito = []
extrato_saque = []


print("Seja bem vindo ao Banco Santana!")
while True:
    print(menu)
    opcao = int(input("-> "))

    #SAQUE CASO O SALDO SEJA = R$ 0,0
    if opcao == 1 and saldo == 0.0:
        if total_saque == 3:
            print("Você atingiu o limite de saques diários.")
            continue 
        print("Seu saldo é de R$ 0,0. Não é possível realizar saque.")
        continue 

    #SAQUE CASO O SALDO SEJA MAIOR QUE R$ 0,0
    elif opcao == 1 and saldo > 0.0:
        if total_saque == 3:
            print("Você atingiu o limite de saques diários.")
            continue    
        print(f"\nSeu saldo é: {saldo:.2f}.")
        saque = float(input("Digite o valor do saque: "))
        if saque > 500:
            while saque > 500:
                print("Você não pode sacar mais de R$ 500,00 por vez.")
                saque = float(input("Digite o novo valor do saque: "))
        elif saque > saldo:
            while saque > saldo:
                saque = float(input("Você não tem saldo suficiente. Digite o novo valor do saque: "))
        print("Processando...")
        sleep(2)
        print("Saque realizado.")
        extrato_saque.append(saque)
        saldo -= saque
        total_saque += 1

    if opcao == 2:
        print(f"\nO seu saldo é: {saldo:.2f}.")
        deposito = float(input("Digite o valor do depósito: "))
        if deposito < 0:
            while deposito < 0:
                deposito = float(input("Não é possível depositar um valor negativo. Digite o novo valor de depósito: "))
        saldo += deposito
        print("Processando...")
        sleep(2)
        print("Depósito realizado.")
        extrato_deposito.append(deposito)

    if opcao == 3:
        print(menu_extrato)
        opcao_extrato = int(input("-> "))
        if opcao_extrato == 1:
            print("Processando...\n")
            sleep(2)
            for c in range(0,len(extrato_saque)):
                print(f"{c+1}. R${extrato_saque[c]:.2f}")
        elif opcao_extrato == 2:
            print("Processando...\n")
            sleep(2)
            for c in range(0,len(extrato_deposito)):
                print(f"{c+1}. R${extrato_deposito[c]:.2f}")
        elif opcao_extrato == 0:
            break

    if opcao == 0:
        break

print("Obrigado por utilizar o nosso sistema!.")
        
                   


