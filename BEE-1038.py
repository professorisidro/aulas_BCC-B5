# entrada
TC, TQ = input("").split()
COD = int(TC)
QTD = int(TQ)
#processamento
if COD == 1:
    total = 4.00 * QTD
elif COD == 2:
    total = 4.50 * QTD
elif COD == 3:
    total = 5.00 * QTD
elif COD == 4:
    total = 2.00 * QTD
else:
    total = 1.50 * QTD
#saida
print("Total: R$ %.2f"%total)