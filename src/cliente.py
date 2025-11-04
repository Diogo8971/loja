def menu_cliente():
    while True:
        print("\n--- Menu Cliente ---")
        print("1 - Adicionar produto ao carrinho")
        print("2 - Filtrar produtos por preço")
        print("3 - Finalizar compra")
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