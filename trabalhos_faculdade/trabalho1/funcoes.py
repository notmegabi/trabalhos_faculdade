#Lista de colaboradores
colaboradores = [
    {"nome": "LP", "cpf": "123.456.789-00", "cargo": "Vendedor", "salario": 2500.00},
    {"nome": "Godstrik", "cpf": "987.654.321-00", "cargo": "Gerente", "salario": 5000.00},
    {"nome": "Cavera", "cpf": "456.789.123-00", "cargo": "Vendedor", "salario": 2200.00},
    {"nome": "Yueko", "cpf": "321.654.987-00", "cargo": "Analista", "salario": 3500.00},
    {"nome": "Neat", "cpf": "321.654.987-00", "cargo": "Marketing", "salario": 1500.00},
]

#Funcao para listar os colaboradores
def listar_colaboradores():
    print("\n--- Lista de Colaboradores ---")
    for colaborador in colaboradores:
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['cpf']}, Cargo: {colaborador['cargo']}, Salário: {colaborador['salario']:.2f}")

#Funcao para listar em ordem alfabetica (nome)
def lista_alfabetica():
    print("\n--- Colaboradores em Ordem Alfabética ---")
    for colaborador in sorted(colaboradores, key=lambda x: x['nome']):
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['cpf']}, Cargo: {colaborador['cargo']}, Salário: {colaborador['salario']:.2f}")

#Funcao para listar em ordem alfabetica (salario)
def ordem_salario():
    print("\n--- Colaboradores em Ordem de Salario ---")
    for colaborador in sorted(colaboradores, key=lambda x: x['salario']):
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['cpf']}, Cargo: {colaborador['cargo']}, Salário: {colaborador['salario']:.2f}")

#Funcao para listar quais cargos existem
def listar_cargos():
    cargos = []
    for colaborador in colaboradores:
        cargo = colaborador['cargo']
        if cargo not in cargos:
            cargos.append(cargo)
    print("\n--- Cargos Disponíveis ---")
    for cargo in cargos:
        print(cargo)

#Funcao para listar por cargo digitado pelo usuario
def listar_por_cargo():
    while True:
        cargo = input("\n Digite o cargo para filtrar ou sair para voltar as opções: ")
        if cargo.lower() == "sair":
            print("Voltando as opções iniciais...")
            break
        
        print(f"\n--- Colaboradores com o Cargo '{cargo}' ---")
        cargo_desejado = []

        for colaborador in colaboradores:
            if colaborador['cargo'].lower() == cargo.lower():
                cargo_desejado.append(colaborador)

        if cargo_desejado:
            for colaborador in cargo_desejado:
                print(f"Nome: {colaborador['nome']}, CPF: {colaborador['cpf']}, Cargo: {colaborador['cargo']}, Salário: {colaborador['salario']:.2f}")
            break
        else:
            print("Nenhum colaborador encontrado com esse cargo.")



