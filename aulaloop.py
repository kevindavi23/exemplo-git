valor = float(input('digite o valor inicial do seu investimento: '))
meses = int(input('digite a quantidade de meses do investimento: '))

for i in range(meses):
    valor = valor + valor * 1.0034
    print(valor)
    