'''
Faculdade de Informática e Administração Paulista - FIAP
Defesa Cibernética
Optimization for Security
Prof. Ms. Fábio Henrique Cabrini
3/2020
Equação do 2º grau 
'''
from math import sqrt
print("Cálculo da Equação do 2º grau genérica")
print("a.x^2+b.x+c=0")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
if a == 0 and b !=0 and c !=0:
    print("Equação do 1º grau")
    print("{0}.x + ({1}) = 0".format(b,c))
    x = -c/b
    print("O valor de x = {0:2.3f}".format(x))
    if b > 0:
        print("A reta é crescente! /")
    else:
        print("A reta é decrescente! \\")
elif a == 0 and b == 0:
    print("Não é uma equação!")
elif a != 0 and b !=0 and c == 0:
    print("A equação {0}.x^2 + ({1}).x = 0".format(a,b))
    x1 = 0
    x2 = -b/a
    print(" As raizes são x'={0:2.3f} e x''={1:2.3f}".format(x1,x2))
    if a > 0:
        print("A parábola tem concavidade para cima \\_/")
    else:
        print("A parábola tem concavidade para baixo /¨\\")
elif a != 0 and b == 0 and c != 0:
    print("A equação {0}.x^2 + ({1}) = 0".format(a,c))
    x1 = sqrt (-c/a)
    x2 = -sqrt (-c/a)
    print(" As raizes são x' = {0:2.3f} e x'' = {1:2.3f}".format(x1,x2))
    if a > 0:
        print("A parábola tem concavidade para cima \\_/")
    else:
        print("A parábola tem concavidade para baixo /¨\\")  
else:    
    print("Equação do 2º grau completa")
    print("A equação {0}.x^2 + ({1}).x + ({2}) = 0".format(a,b,c))
    delta = b**2 - 4*a*c
    print("O valor do delta é = {0:2.3f}".format(delta))
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        print("As raizes reais são x' = {0:2.3f} e x'' = {1:2.3f}".format(x1,x2)) 
        if a > 0:
            print("A parábola tem concavidade para cima \\_/")
        else:
            print("A parábola tem concavidade para baixo /¨\\")  
    elif delta == 0:
        x1 = -b/(2*a) 
        print("A raiz real é x' = {0:2.3f}".format(x1)) 
        if a > 0:
            print("A parábola tem concavidade para cima \\_/")
        else:
            print("A parábola tem concavidade para baixo /¨\\") 

    else:
        print("Não possui raiz real, a parábola não intersecta o eixo x.")

