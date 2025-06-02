#Nome da equipe: Guilherme Giovannetti de Andrades

import hashlib

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

    senha_md5 = hashlib.md5(senha.encode()).hexdigest()

    if nome in usuarios:
        print("Usuário já existe!")
    else:
        with open("dados.txt", "a") as f:
            f.write(f"{nome}:{senha_md5}\n")
        print("Usuário cadastrado com sucesso!")

def autenticar_usuario():
    usuarios = carregar_usuarios()
    print("\n--- Autenticação de usuário ---")
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

    senha_md5 = hashlib.md5(senha.encode()).hexdigest()

    if nome in usuarios and usuarios[nome] == senha_md5:
        print("\nLogin bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

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
