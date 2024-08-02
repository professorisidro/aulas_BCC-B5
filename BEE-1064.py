qtdePositivos = 0
somaPositivos = 0
for cont in range(0,6):
    valor = float(input(""))
    if valor > 0:
        qtdePositivos = qtdePositivos + 1
        somaPositivos = somaPositivos + valor
        
print(qtdePositivos,"valores positivos")
media = somaPositivos / qtdePositivos
print("%.1f"%media)