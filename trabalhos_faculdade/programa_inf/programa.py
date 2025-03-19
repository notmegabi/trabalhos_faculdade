print(f"{'Opcoes Disponiveis:':^50}")
print("Ola")
print("Qual o seu nome?")
print("Que horas sao?")

while True:
    inicio = input("Diga ola para iniciar ou sair para encerrar: ").strip().lower()
    if inicio == "ola":
        break
    elif inicio == "sair":
        print("Ate logo, usuario...")
        exit()
    else:
        print("Digite 'ola' para iniciar: ")

while True:
    opcao = input("Faca sua pergunta ou digite sair para encerrar: ").strip()

    if opcao.lower() == "ola":
        print("Ola, usuario")
    elif opcao.lower() == "qual o seu nome?":
        print("Meu nome e Sra. Python")
    elif opcao.lower() == "que horas sao?":
        print("Agora sao exatamente 20:00 no planeta Pytho")
    elif opcao.lower() == "sair":
        print("Ate logo, usuario...")
        break
    else:
        print("--Digitou algo errado, tente novamente--")