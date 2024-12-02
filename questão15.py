#questão 15
l1= float(input("digite um numero:"))
l2= float(input("digite outro numero:"))
c= (l1*l1) + (l2*l2)
if(l1==l2==c):
    print("Triângulo Equilátero")
elif(l1==l2):
    l1==c
    l2==c
    print("Triângulo Isósceles")
elif(l1!=l2!=c):
    print("Triângulo Escaleno")        