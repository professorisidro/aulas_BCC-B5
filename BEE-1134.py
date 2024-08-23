numAlc = 0
numGas = 0
numDie = 0

while True:
    comb = int(input(""))
    if comb == 1:
        numAlc = numAlc + 1
    elif comb == 2:
        numGas = numGas + 1
    elif comb == 3:
        numDie = numDie + 1
    elif comb == 4:
        break
    
print("MUITO OBRIGADO")    
print("Alcool:", numAlc)
print("Gasolina:", numGas)
print("Diesel:", numDie)