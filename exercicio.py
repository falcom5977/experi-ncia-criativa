yes = True
usuarios = {}

while yes != False:
    print("menu\n")
    print("1. Cadastrar\n")
    print("2.login\n")
    menu= int(input("qual vai ser sua escolha?: "))
    if menu == 1:
        new_user = input("qual é o usuario?: ")
        new_senha = input("qual é a senha?:")
        with open("dados.txt","a") as f:
            f.write(f"{new_user}:{new_senha}\n")
    elif menu ==2:
        tentativa = 3
        while tentativa >= 1:
            user_guess = input("qual é o usuario?: ")
            senha_guess = input("Qaul e a shenha?: ")
            with open("dados.txt", "r") as f:
                for linha in f:
                    usuario,senha = linha.strip().split(":")
                    usuario[usuario] = senha
            if user_guess in usuarios and usuarios[user_guess] == senha_guess:
                print("\nBem-vindo novamente")
                tentativa -= 1