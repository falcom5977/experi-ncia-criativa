#Nome da equipe: Guilherme Giovannetti de Andrades
import hashlib
import time

def carregar_usuarios():
    usuarios = {}
    try:
        with open("dados.txt", "r") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(":")
                if len(partes) != 2:
                    print(f"Aviso: linha ignorada por formato inválido: {linha}")
                    continue
                usuario, senha_hash = partes
                usuarios[usuario] = senha_hash
    except FileNotFoundError:
        pass
    return usuarios

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    print("\n--- Cadastro de novo usuário ---")
    while True:
        nome = input("Digite o nome do usuário (4 caracteres): ")
        if len(nome) == 4:
            break
        print("O nome deve ter exatamente 4 caracteres.")

    while True:
        senha = input("Digite a senha (4 caracteres): ")
        if len(senha) == 4:
            break
        print("A senha deve ter exatamente 4 caracteres.")

    senha_hash = hash_senha(senha)

    if nome in usuarios:
        print("Usuário já existe!")
    else:
        with open("dados.txt", "a") as f:
            f.write(f"{nome}:{senha_hash}\n")
        print("Usuário cadastrado com sucesso!")

def autenticar_usuario():
    usuarios = carregar_usuarios()
    print("\n--- Autenticação de usuário ---")
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        nome = input("Digite o nome do usuário (4 caracteres): ")
        if len(nome) != 4:
            print("O nome deve ter exatamente 4 caracteres.")
            continue

        senha = input("Digite a senha (4 caracteres): ")
        if len(senha) != 4:
            print("A senha deve ter exatamente 4 caracteres.")
            continue

        senha_hash = hash_senha(senha)

        if nome in usuarios and usuarios[nome] == senha_hash:
            print("\nLogin bem-sucedido!")
            return
        else:
            tentativas += 1
            print(f"Usuário ou senha incorretos! ({tentativas}/{max_tentativas} tentativas)")
            if tentativas < max_tentativas:
                time.sleep(2 * tentativas)  # atraso progressivo: 2s, 4s, etc.

    print("\nMuitas tentativas incorretas. Tente novamente mais tarde.")

def main():
    print("\nBem-vindo ao programa de cadastro e autenticação!\n")
    while True:
        print("\nMenu:")
        print("1 - Cadastrar novo usuário")
        print("2 - Autenticar usuário")
        print("3 - Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            autenticar_usuario()
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
