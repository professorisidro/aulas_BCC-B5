# entrada - novamente seguindo padrão se fazer o SPLIT
TA, TB, TC = input("").split()
A = float(TA)
B = float(TB)
C = float(TC)

# processamento
# a) a área do triângulo retângulo que tem A por base e C por altura.
ATri = A * C / 2

# b) a área do círculo de raio C. (pi = 3.14159)
ACir = 3.14159 * C ** 2

# c) a área do trapézio que tem A e B por bases e C por altura.
ATra = (A + B) * C / 2

# d) a área do quadrado que tem lado B.
AQua = B ** 2

# e) a área do retângulo que tem lados A e B.
ARet = A * B

# saida
print("TRIANGULO: %.3f" % ATri)
print("CIRCULO: %.3f" % ACir)
print("TRAPEZIO: %.3f" % ATra)
print("QUADRADO: %.3f" % AQua)
print("RETANGULO: %.3f" % ARet)

