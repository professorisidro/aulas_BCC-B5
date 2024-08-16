#entrada
TA, TB, TC = input("").split()
A = float(TA)
B = float(TB)
C = float(TC)

#processamento
# verificar se é triangulo
# se for, calcula o perimetro (soma dos lados)
# se nao for, calcula a area do trapezio: Area = (A + B)*C/2

if A+B>C and A+C>B and B+C>A:
    Per = A+B+C
    print("Perimetro = %.1f" % Per)
else:
    Are = (A + B)*C/2
    print("Area = %.1f" % Are)
    
    