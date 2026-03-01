# --- NOSSAS LISTAS (Onde os dados ficam guardados) ---
clientes = []
quartos = []
reservas = []

while True:
    print("\n========== HOTEL PYTHON ==========")
    print("1. Gerir Clientes")
    print("2. Gerir Quartos")
    print("3. Gerir Reservas")
    print("0. Sair do Sistema")
    
    opcao_principal = input("Escolha uma área: ")

    # --- ÁREA DE CLIENTES ---
    if opcao_principal == "1":
        while True:
            print("\n--- MENU CLIENTES ---")
            print("1. Registar Cliente")
            print("2. Listar Clientes")
            print("0. Voltar")
            op = input("Opção: ")
            if op == "1":
                nome = input("Nome do cliente: ")
                clientes.append(nome)
                print("Cliente guardado!")
            elif op == "2":
                print(f"Lista: {clientes}")
            elif op == "0":
                break

    # --- ÁREA DE QUARTOS ---
    elif opcao_principal == "2":
        while True:
            print("\n--- MENU QUARTOS ---")
            print("1. Adicionar Quarto")
            print("2. Listar Quartos")
            print("0. Voltar")
            op = input("Opção: ")
            if op == "1":
                num = input("Número do quarto: ")
                quartos.append(num)
                print("Quarto adicionado!")
            elif op == "2":
                print(f"Quartos: {quartos}")
            elif op == "0":
                break

    # --- ÁREA DE RESERVAS ---
    elif opcao_principal == "3":
        while True:
            print("\n--- MENU RESERVAS ---")
            print("1. Criar Reserva")
            print("2. Listar Reservas")
            print("0. Voltar")
            op = input("Opção: ")
            if op == "1":
                c = input("Nome do cliente: ")
                q = input("Número do quarto: ")
                reservas.append({"cliente": c, "quarto": q})
                print("Reserva concluída!")
            elif op == "2":
                for r in reservas:
                    print(f"Reserva: {r['cliente']} -> Quarto {r['quarto']}")
            elif op == "0":
                break

    # --- SAIR ---
    elif opcao_principal == "0":
        print("A sair do sistema...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")