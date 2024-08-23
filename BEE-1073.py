N = int(input(""))

for num in range(1, N+1):
    if num % 2 == 0:
        print(num,"^2 = ", num**2, sep="")