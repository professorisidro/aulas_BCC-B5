# entrada
TCx, TCy = input("").split()
x = float(TCx)
y = float(TCy)

# processamento + saída (porque a saída depende de eu decidir qual o quadrante que os valores se encontram)
if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif x != 0 and y == 0:    
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
else:
    print("Origem")