#questão 11

salario= float(input("digite o seu salario:"))
porc1= (20*salario)/100
porc2= (15*salario)/100
porc3= (10*salario)/100
porc4= (5*salario)/100
if(salario<=280):
    print(salario)
    print("20%")
    print(porc1)
    print(salario+porc1)
elif(salario<=700):
     print(salario)
     print("15%")
     print(porc1)
     print(salario+porc2)
elif(salario<=1500):
     print(salario)
     print("10%")
     print(porc3)
     print(salario+porc3)
elif(salario>1500):
     print(salario)
     print("5%")
     print(porc4)
     print(salario+porc4)            