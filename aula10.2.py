numero = 1
soma = 0
while(numero != 0 ):
    numero = int(input("digite um numero:"))
    if(numero % 2 == 0 or numero % 3 ==0 ):
        soma = soma + numero
print("valor é:", soma)