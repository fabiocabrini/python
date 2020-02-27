N = int(input("Digite N: "))
i = 2
while i < N:
    R = N % i
    if R == 0:
        print("{} não é primo".format(N))
        break
    i += 1
else:
    print("{} é primo!".format(N))
