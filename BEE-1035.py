#
# Leia 4 valores inteiros A, B, C e D. 
# A seguir, 
# se B for maior do que C (1)  e 
# se D for maior do que A,(2)  e 
# a soma de C com D for maior que a soma de A e B (3) e 
# se C e D, ambos, forem positivos (4) e 
# se a variável A for par (5)

# (1)   B > C
# (2)   D > A
# (3)   C + D > A + B
# (4)   C > 0 and D > 0
# (5)   A % 2 == 0

TA,TB,TC,TD = input().split(" ")
A = int(TA)
B = int(TB)
C = int(TC)
D = int(TD)
if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
