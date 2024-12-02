repetição = int(input("digite a quantidade de notas:"))
contador = 0
soma = 0
for valor in range (repetição):
    nota = float(input("digite uma nota:"))
    contador += 1 
    soma = soma + nota

print("soma", soma)
print("contador", contador)
media = soma / contador
print("media", media)
if(media>=7 and media<= 9.9):
    print("aluno aprovado")
elif(media == 10):
    print("aluno aprovado com exelencia")

else:
    print("aluno reprovado")          

