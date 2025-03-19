# Notas separadas por média 1 (M1) e média 2 (M2)

m1 = float(input("Digite sua nota da M1: "))
m2 = float(input("Digite sua nota da M2: "))

# A conta para a média semestral

ms = (m1 + m2 * 2) / 3

# Usando if, elif e else para comparar com a média da escola/universidade, nesse caso, média 5, com reprovação abaixo de 3

if ms >=5:
    print("Você passou de semestre, parabéns!!")
elif 3<= ms < 5:
    print("Você ficou de recuperação, estude para próxima prova.")
else:
    print("Sinto muito, você reprovou.")