from controller import ControllerCadastro, ControllerLogin


while True:
    print("========== [MENU] ==========")
    print("----------------------------")
    
    decisao = int(input("Digite 1 para se cadastrar\n"
                        "Digite 2 para entrar no sistema\n"
                        "Digite 3 para sair\n"))
    
    if decisao == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        resultado = ControllerCadastro().cadastrar(nome, email, senha)

        if resultado == 2:
            print("Tamnho do nome digitado é inválido")
        elif resultado == 3:
            print("E-mail inválido, maior que 200 caracteres")
        elif resultado == 4:
            print("Tamanho da senha é inválido")
        elif resultado == 5:
            print("Esse e-mail já está em uso!")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastrado com sucesso!")

    elif decisao == 2:
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        resultado = ControllerLogin().login(email, senha)

        if not resultado:
            print("E-mail ou senha incorretos, tente novamente.")

        else:
            print(resultado)

    else:
        break