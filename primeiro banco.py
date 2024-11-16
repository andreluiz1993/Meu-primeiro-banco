print("Bom dia!")

tentativas = 1
usuario_correto = "André"
senha_correta = 1234
saldo = 500

usuario = input("Por favor, insira seu nome: ")
senha = int(input("Por favor, insira sua senha: "))

while usuario != usuario_correto or senha_correta != senha:
    tentativas += 1
    if tentativas > 3:
        print()
        print("Número de tentativas excedida, acesso bloqueado!")
        exit()
    else:
        print("Usuário e/ou senha incorretos! Tente novamente!")
        print()
        usuario = input("Por favor, insira seu nome: ")
        senha = int(input("Por favor, insira sua senha: "))
           
print()
print("Seja bem vindo ao Banco SN")

print("Escolha a opção desejada:")
print()
print("Saque: digite 1")
print("Depósito: digite 2")
print("Consultar Saldo: digite 3")
print("Sair: digite 4")
print()
opcao = int(input("O que você precisa? "))


while opcao != 4:
    try:
        if opcao == 1:
            saque = float(input("informe o valor que deseja sacar: "))
            if saque > saldo:
                print("Saldo insuficiente!, limite máximo para saque é de R$ ",saldo)
                print()
                opcao = int(input("Do que mais você precisa? "))
            else:
                saldo = saldo - saque
                print()
                opcao = int(input("Do que mais você precisa? "))
                
        if opcao == 2:
            deposito = float(input("informe o valor que deseja depositar: "))
            saldo = saldo + deposito
            print()
            opcao = int(input("Do que mais você precisa? "))
                
        if opcao == 3:
            print(f"O valor atual em conta é de R$ ",saldo)
            print()
            opcao = int(input("Do que mais você precisa? "))
        
        else:
            print("Opção inválida! Tente novamente!")
            opcao = int(input("Do que mais você precisa? "))
            print()
            
    except ValueError:
        print("Opção inválida! Tente novamente!")
        opcao = int(input("Do que mais você precisa? "))

print("Obrigado por utilizar nossos serviços, até a próxima!")