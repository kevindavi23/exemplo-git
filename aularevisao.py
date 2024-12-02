nome = input("digite seu nome ")

t = len(nome)
if(t>=4):
    if(nome[0:2] == nome[t-2:t] ):
        print("são iguais")
    else:
        print("não são iguais")    
    