#questão 7
n1= int(input("digite um numero:"))
n2= int(input("digite outro numero:"))
n3= int(input("digite outro numero:"))
if(n1<n2<n3):
    print(n1)
elif(n2<n1<n3):
    print(n2)
else:
    print(n3)    
    # questão 8
preço1= float(input("qual o preço do ovo:")) 
preço2= float(input("qual o preço do suco:"))
preço3= float(input("qual o preço da carne:"))
if(preço1<preço2<preço3):
    print("compre o ovo")
elif(preço2<preço1<preço3):
    print("compre o suco")
else:
    print("compre a carne")                  