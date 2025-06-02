#Nome da equipe: Guilherme Giovannetti de Andrades

from itertools import product
import hashlib
import string
import time

usuarios = {}
with open("dados.txt", "r") as f:
    for linha in f:
        linha = linha.strip()
        if not linha:
            continue
        usuario, senha_hash = linha.split(":")
        usuarios[usuario] = senha_hash

start_total = time.time()

caracteres = string.digits + string.ascii_lowercase

for intento in product(caracteres, repeat=4):
    user = ''.join(intento)
    if user in usuarios:
        start_senha = time.time()
        senha_encontrada = None
        for intento2 in product(caracteres, repeat=4):
            senha = ''.join(intento2)
            senha_md5 = hashlib.md5(senha.encode()).hexdigest()

            if usuarios[user] == senha_md5:
                tempo_senha = time.time() - start_senha
                print(f"O usuário é '{user}' e a senha é '{senha}'")
                print(f"Tempo para descriptografar essa senha: {tempo_senha:.4f} segundos\n")
                senha_encontrada = senha
                break
        if senha_encontrada is not None:
            continue

total_time = time.time() - start_total
print(f"Tempo total para encontrar todas as senhas: {total_time:.4f} segundos")
