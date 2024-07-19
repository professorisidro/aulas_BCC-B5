# entrada
# ate agora vimos que as entradas eram separadas por um "ENTER". O problema é que o python não consegue
# diferenciar espaços em branco para diferentes variáveis.
# portanto precisamos ler as 3 variáveis de uma vez (sempre em formato TEXTO), porém dividindo (seprando)
# essa entrada pelo caractere que a gente precisa (neste caso será um espaço em branco). 
# por isso usamos o SPLIT (poderia por exemplo ser um ; um # um |)

TC1, TQ1, TP1 = input("").split(" ")
C1 = int(TC1)
Q1 = int(TQ1)
P1 = float(TP1)
TC2, TQ2, TP2 = input("").split(" ")
C2 = int(TC2)
Q2 = int(TQ2)
P2 = float(TP2)

# processamento
TOTAL = Q1 * P1 + Q2 * P2

# saida
print("VALOR A PAGAR: R$ %.2f" % TOTAL)

