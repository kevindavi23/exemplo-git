#questão 5
n1= int(input("digite um numero:"))
n2= int(input("digite um numero:"))
n3= int(input("digite um numero:"))
media= (n1+n2+n3) /3
if(media==10):
    print("aprovado com distinção")
elif(media>=7):
    print("aprovado")
else:
    print("reprovado") 
#questão 6
n1= int(input("digite um numero:"))
n2= int(input("digite outro numero:"))
n3= int(input("digite outro numero:"))
if(n1>n2>n3):
    print(n1)
elif(n2>n1>n3):
    print(n2)
else:
    print(n3)            