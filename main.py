def calcular_juros_compostos_for(P, i, n):
    M = P


    for periodo in range(n):
        M += M * (i / 100)

P = int(input("Qual valor você deseja investir"))
i = 0.05
n = int(input("Quanto tempo você deseja investir"))


montante = calcular_juros_compostos_for(P, i, n)

print(f"Montante final após {n} períodos: R$ {montante:.2f}")
