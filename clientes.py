# Lista para armazenar os nomes dos clientes
clientes = []

while True:
    print("\n--- GESTÃO DE CLIENTES ---")
    print("1. Registar novo cliente")
    print("2. Listar todos os clientes")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Pede o nome e adiciona à lista
        nome = input("Digite o nome completo do cliente: ")
        clientes.append(nome)
        print(f"Cliente {nome} registado com sucesso!")

    elif opcao == "2":
        # Verifica se a lista está vazia antes de mostrar
        print("\n--- Lista de Clientes ---")
        if not clientes:
            print("Nenhum cliente registado ainda.")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i}. {cliente}")

    elif opcao == "3":
        print("A sair da gestão de clientes...")
        break # Sai do loop while

    else:
        print("Opção inválida! Tente novamente.")