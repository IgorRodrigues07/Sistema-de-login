
usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc456"
}



def exibir_menu():
    print("\n" + "="*35)
    print("       SISTEMA DE LOGIN")
    print("="*35)
    print("  1 - Fazer login")
    print("  2 - Cadastrar novo usuário")
    print("  0 - Sair")
    print("="*35)

def login():
    print("\n── LOGIN ──")
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha   = input("Senha:   ")

        if usuario in usuarios:
            if usuarios[usuario] == senha:
                print(f"\nBem-vindo, {usuario}! Login realizado com sucesso.")
                return usuario
            else:
                tentativas -= 1
                print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        else:
            tentativas -= 1
            print(f"Usuário não encontrado! Tentativas restantes: {tentativas}")

    print("\nMuitas tentativas incorretas. Acesso bloqueado.")
    return None

def cadastrar():
    print("\n── CADASTRO ──")

    novo_usuario = input("Escolha um nome de usuário: ")

    if novo_usuario in usuarios:
        print("Esse usuário já existe! Tente outro nome.")
        return

    nova_senha = input("Escolha uma senha: ")
    confirmacao = input("Confirme a senha: ")

    if nova_senha != confirmacao:
        print("As senhas não coincidem! Cadastro cancelado.")
        return

    usuarios[novo_usuario] = nova_senha
    print(f"\nUsuário '{novo_usuario}' cadastrado com sucesso!")

def area_restrita(usuario_logado):
    print(f"\n── ÁREA RESTRITA ── Olá, {usuario_logado}!")
    print("Você está dentro do sistema.")
    print("(Em um sistema real, aqui ficariam as funcionalidades)")
    input("\nPressione Enter para voltar ao menu...")

 
logado = False
usuario_atual = ""

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "0":
        print("\nAté logo!")
        break

    elif escolha == "1":
        usuario_atual = login()
        if usuario_atual:
            logado = True
            area_restrita(usuario_atual)

    elif escolha == "2":
        cadastrar()

    else:
        print("Opção inválida!")