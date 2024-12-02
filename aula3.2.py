print("bem vindo ao sistema de media:")
nota1 = int(input("digite uma nota:"))
nota2 = int(input("digite uma nota:"))
nota3 = int(input("digite uma nota:"))
soma = (nota1+nota2+nota3)/3
print("sua media é:",soma)
print(soma >= 7,"parabens você foi aprovado")
print(soma < 7,"infelizmente você foi reprovado")