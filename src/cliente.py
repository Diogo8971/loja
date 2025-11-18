def menu_cliente():
    while True:
        print("\n--- Menu Cliente ---")
        print("1 - Ver catálogo")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Ver carrinho")
        print("4 - Remover do carrinho")
        print("5 - Filtrar produtos por preço")
        print("6 - Finalizar compra")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_ao_carrinho()
        elif opcao == "2":
            filtrar_produtos()
        elif opcao == "3":
            finalizar_compra()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def adicionar_ao_carrinho():
    print(" Produto adicionado ao carrinho!")


def filtrar_produtos():
    print(" Filtrando produtos por preço...")


def finalizar_compra():
    print(" Compra finalizada com sucesso!")