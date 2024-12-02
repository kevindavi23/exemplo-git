#questão 16
a = float(input("Digite o valor de a: "))

# Verifica se a é diferente de zero
if a == 0:
    print("A equação não é do segundo grau. Encerrando o programa.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    # Calcula o delta
    delta = b**2 - 4*a*c

    # Verifica as condições e imprime as raízes se aplicável
    if delta < 0:
        print("A equação não possui raízes reais. Encerrando o programa.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + (delta**0.5)) / (2*a)
        raiz2 = (-b - (delta**0.5)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")