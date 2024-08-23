# meu programa executa "pra sempre"
# esse while True indica que a condição do while nunca vai mudar

while True:
    tX, tY = input("").split()
    X = int(tX)
    Y = int(tY)

    # quando ele para a repeticao?
    if X == 0 or Y ==0:
        break  # esse é o responsável por parar o programa
    
    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X < 0 and Y < 0:
        print("terceiro")
    elif X > 0 and Y < 0:
        
        print("quarto")