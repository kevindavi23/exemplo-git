numerodealunos = int(input("digite o numero de alunos que vão comprar a camisa:"))
numerodamatricula = 1 
while(numerodamatricula <= numerodealunos):
    tamanho = int(input("digite o tamnanho (p,m ou g):"))
    if(tamanho == "p"):
        print("escolheu p")
        numerodealunos += 1
    elif(tamanho == "m"):
        print("escolheu m")
        numerodealunos += 1

    elif(tamanho == "g"):
        numerodealunos += 1 
        print("escolheu g")
    else:
        print("opção inavalida tente novamente")             