import funcoes

def app():

    print("\n--- App ---")
    print("1. Listar colaboradores.")
    print("2. Relatório em ordem alfabética.")
    print("3. Relatório por ordem salarial.")
    print("4. Lista de cargos disponíveis")
    print("5. Listar por cargo.")
    print("6. Sair.")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            funcoes.listar_colaboradores()
        elif opcao == "2":
            funcoes.lista_alfabetica()
        elif opcao == "3":
            funcoes.ordem_salario()
        elif opcao == "4":
            funcoes.listar_cargos()
        elif opcao == "5":
            funcoes.listar_por_cargo()
        elif opcao == "6": 
            break
        else:
            print("Opção inválida. Tente novamente.")

app()
