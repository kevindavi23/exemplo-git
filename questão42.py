repetição = int(input("digite a quatidade de repetição:"))
contadorpar = 0
contadorimpar = 0
somapar = 0
somaimpar = 0
for valor in range(repetição):
    numero = int(input("digite um numero:"))
    if(numero % 2 == 0):
        contadorpar += 1
        somapar = somapar + numero
      
    elif(numero % 2 != 0):
        contadorimpar += 1
        somaimpar = somaimpar + numero
        

mediapar = somapar / contadorpar 
mediaimpar = somaimpar / contadorimpar     
print("soma par:",somapar)
print("contador par:", contadorpar)
print("media par:", mediapar)
print("somaimpar:",somaimpar)
print("contador impar:",contadorimpar)
print("media impar:", mediaimpar)
