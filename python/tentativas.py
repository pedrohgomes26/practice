email = "emailpessoa@gmail.com"

senha = input("Defina sua senha: ")

senha_confirma = input("Coloque sua senha: ")

tentativa = 3

while (tentativa > 0):
    if senha == senha_confirma:
        print("senha correta")
        break
    else:
        print("senha incorreta")
        tentativa -= 1
        senha_confirma = input("Coloque sua senha: ")

if tentativa == 0:
    print("emmail bloqueado")