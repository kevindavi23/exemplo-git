inicial = int(input("digite o numero inicial:"))
final = int(input("digite o numero final:"))

for i in range(inicial, (final+1)):
    if(i % 2 == 0):
        print(i)
