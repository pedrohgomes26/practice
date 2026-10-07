import hashlib

senha = "M1nh@_S3nh@"

hash_obj = hashlib.sha256(senha.encode(encoding='utf-8'))
hash_hex = hash_obj.hexdigest()
print(hash_hex)

digita_senha = input("Digite sua senha: ")

hash_digitar = hashlib.sha256(digita_senha.encode(encoding='utf-8')).hexdigest

print(hash_digitar)

if hash_digitar == hash_digitar:
    print("Acesso permitido")
else:
    print("Acesso negado")