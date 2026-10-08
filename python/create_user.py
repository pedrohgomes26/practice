def name_user():
    nome_usuario = input("Escolha seu nome de usuario: ")
    confirmar_username = input("Vai ser esse nome mesmo: ")

    if confirmar_username == "não":
        nome_usuario = input("Escolha outro nome: ")




def senha():
    registrar_senha = input("Defina sua senha: ")
    confirmacao = input("Confirme sua senha: ")

    if registrar_senha != confirmacao:
        while confirmacao != registrar_senha:
            confirmacao = input("Senha incorreta tente de novo: ")

    deseja_autenticacao = input("Desejar ativar a verificação em 2 fatores: ")

    if deseja_autenticacao == "sim":
        doisfatores = input("Escolha um palavra para ser sua autenticação: ")
        confirmardoisfatores = input("confirme sua palavra de autenticação: ")

    if confirmardoisfatores != doisfatores:
        while confirmardoisfatores != doisfatores:
            confirmardoisfatores = input("Palavra incorreta digite novamente: ")

confirmar_user = input("Terminar de criar usuario: ")

if confirmar_user == "nao":
    name_user()
    senha()