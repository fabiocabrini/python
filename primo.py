N = int(input("Digite o número: "))
cont = 0
i = 2
while i < N:
    R = N % i
    if R == 0:
        cont += 1
    i += 1
if cont == 0:
    print("{} é primo!".format(N))
else:
    print("{} não é primo" .format(N))
