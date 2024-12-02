# num = int(input('digite o numero: '))
#if(num > 0 and num < 11):
   # for k in range(1,11):
    #    valor = num * k 
    #    print(f'{num} x {k} = {valor}')

#for cadeira in range (1,4):
  #  print(cadeira)

#num = int(input('digite o numero: '))
#fat = 1
#for i in range(1, num + 1):
    #fat = fat * i
   # print(fat)

#ant = 0
#atual = 1
#n = int(input('digite o n da sequencia: '))
#for i in range (n):
    #aux = atual
    #print(f'o atual é {atual} e o anterior {ant}')
    #atual = atual + ant
    #ant = aux
    #print(f'o novo atual é {atual} e o anterior {ant}\n')

base = int(input('digite a base: '))
exp = int(input('digite o expoente: '))

resp = 1 
for i in range(exp):
    resp = resp * base
print(resp)