import datetime

resposta = input("voce quer saber a hora atual (sim ou nao): ")

if resposta == "sim":
    hora = datetime.datetime.now()
    print("agora e ", hora)
if resposta == "s":
    hora = datetime.datetime.now()
    print("agora e ", hora)


else:
    print("ta bom")
