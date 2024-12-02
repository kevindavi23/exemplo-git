numerodebolinhascoloridas= 5
for valorintervalo in range(10):
    print("oi")

numerodevezes= int(input("digite o numero de notas:"))
soma= 0
for numerodenotas in range(numerodevezes):
    numero= float(input("digite a nota"))
soma= soma + numero
media= soma / numerodevezes
print("a soma é", soma)
print("a media é", media)