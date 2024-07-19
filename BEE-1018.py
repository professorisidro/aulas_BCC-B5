# entrada
# valor do saque
VALOR = int(input(""))

# processamento
Q100  = VALOR // 100
RESTO = VALOR  % 100

Q50   = RESTO // 50
RESTO = RESTO % 50

Q20   = RESTO // 20
RESTO = RESTO % 20

Q10   = RESTO // 10
RESTO = RESTO % 10

Q5    = RESTO // 5
RESTO = RESTO % 5

Q2    = RESTO // 2
Q1    = RESTO % 2

print(VALOR)
print(Q100,"nota(s) de R$ 100,00")
print(Q50, "nota(s) de R$ 50,00")
print(Q20, "nota(s) de R$ 20,00")
print(Q10, "nota(s) de R$ 10,00")
print(Q5,  "nota(s) de R$ 5,00")
print(Q2,  "nota(s) de R$ 2,00")
print(Q1,  "nota(s) de R$ 1,00")