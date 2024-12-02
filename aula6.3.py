#questão 9
n1= int(input("digite um numero:"))
n2= int(input("digite outro numero:"))
n3= int(input("digite outro numero:"))
maior= n1
if(n2>maior):
    maior>n2
if(n3>maior):
    maior>n2
menor= n1
if(n2<menor):
    menor= n2
if(n3<menor):
    menor= n3
meio= n1
if(n1 != maior and n2 != menor):
    meio=n1
if(n2 != maior and n2 != menor):
    meio =n2
if(n3 != maior and n3 != menor):
    meio=n3
print("o maior é", maior)
print("o meio é", meio)
print("o menor é", menor)                       
#questão 10
t= input("qual turno você estuda:")    
if(t=="m"):
    print("BOM DIA")
elif(t=="v"):
    print("BOA TARDE")
elif(t=="n"):
    print("BOA NOITE") 
else:
    print("valor invalido")       