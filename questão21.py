valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (
    valor < 10 or valor > 600
):  # Os parênteses não são necessários, mas vou passar a usá-los
    print("Valor inválido!")
else:
    cem = valor // 100  # Pegamos a centena com uma divisão inteira
    valor -= cem * 100  # Subtraímos as centenas retiradas do valor total
    cinquenta = valor // 50  # Idem para as outras coisas
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor  # Depois de subtrair as de cinco só sobram as de um
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")
