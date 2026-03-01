# Lista para armazenar as reservas (cada reserva será um par Cliente + Quarto)
reservas = []

while True:
    print("\n--- GESTÃO DE RESERVAS ---")
    print("1. Criar nova reserva")
    print("2. Listar todas as reservas")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Pedimos os dados para a reserva
        cliente_nome = input("Nome do cliente para a reserva: ")
        quarto_numero = input("Número do quarto a reservar: ")
        
        # Guardamos como um pequeno "pacote" (dicionário)
        nova_reserva = {"cliente": cliente_nome, "quarto": quarto_numero}
        reservas.append(nova_reserva)
        
        print(f"Reserva confirmada: {cliente_nome} no Quarto {quarto_numero}!")

    elif opcao == "2":
        print("\n--- Lista de Reservas Ativas ---")
        if not reservas:
            print("Não existem reservas registadas.")
        else:
            for i, res in enumerate(reservas, 1):
                # Acedemos aos dados dentro do dicionário usando as 'chaves'
                print(f"{i}. Cliente: {res['cliente']} | Quarto: {res['quarto']}")

    elif opcao == "3":
        print("A sair da gestão de reservas...")
        break

    else:
        print("Opção inválida! Tente novamente.")