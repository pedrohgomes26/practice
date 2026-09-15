senha = input("Digite a senha: ")

confirmar = input("Confirme a senha: ")

if senha == confirmar:
    print("Senha confirmada com sucesso!")
else:
    confirmar = input("As senhas não coincidem. Tente novamente.")
