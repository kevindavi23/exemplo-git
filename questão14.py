#questão 14
n1= float(input("digite uma nota:"))
n2= float(input("digite outra nota:"))
media= (n1+n2)/2
if(media > 9 and media <=10):
    print(media,"A : aprovado")
elif(media>=7.5 and media <=9):
    print(media,"B : aprovado")
elif(media>=6 and media <=7.5):
    print(media,"C : aprovado")
elif(media>=4 and media <=6):
    print(media,"D : reprovado")
elif(media>=0 and media <=4):
    print(media,"E : reprovado")                