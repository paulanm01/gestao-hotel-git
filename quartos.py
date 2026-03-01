# Lista para armazenar os números dos quartos
quartos = []

while True:
    print("\n--- GESTÃO DE QUARTOS ---")
    print("1. Adicionar novo quarto")
    print("2. Listar todos os quartos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Pede o número do quarto e adiciona à lista
        numero_quarto = input("Digite o número ou nome do quarto (ex: 101): ")
        
        # Uma pequena validação para não repetir quartos iguais
        if numero_quarto in quartos:
            print("Erro: Esse quarto já existe no sistema!")
        else:
            quartos.append(numero_quarto)
            print(f"Quarto {numero_quarto} adicionado com sucesso!")

    elif opcao == "2":
        print("\n--- Lista de Quartos ---")
        if not quartos:
            print("Nenhum quarto registado.")
        else:
            for quarto in quartos:
                print(f"Quarto: {quarto}")

    elif opcao == "3":
        print("A sair da gestão de quartos...")
        break

    else:
        print("Opção inválida! Tente novamente.")