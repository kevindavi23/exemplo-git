#def aumentar_salario(nome, valor):
    #final = valor * 1.3
   # print(f'{nome} vai receber {final} reais')
#for i in range(5):
  #  texto = input('digite seu nome')    
   # salario = float(input('digite seu salario'))
    #aumentar_salario(texto, salario)
lunos = []
opcao = -1
while(opcao != 0):
    print('\n\n-----MENU---')
    print('1-cadastrar aluno')
    print('2-remover aluno')
    print('3-listar alunos')
    print('4-mudar nome de aluno')
    print('0-sair')

    opcao = int(input('digite a opçao desejada'))
    if(opcao == 1):
       nome = input('digite o nome do aluno')
       alunos.append(nome)
       print(f'{nome} foi inserido com sucesso\n')
    elif(opcao == 2):
        nome_aluno = input('digite o nome da pessoa para remover')
        if(nome_aluno in alunos):
            #index retorna o índice do elemento
            indice = alunos.index(nome_aluno)
            #remove o elemento por meio do índice
            alunos.pop(indice)
            print('aluno removido com sucesso')
        else:
            print('aluno nao presente na lista')

    elif(opcao == 3):
        for aluno in alunos:
            print(aluno)
    elif(opcao == 4):
        aluno = input('qual o nome do aluno que vc deseja atualizar')
        if (aluno in alunos):
            # index retorna o índice do elemento
            indice = alunos.index(aluno)
            novo_nome = input('digite o novo nome')
            #sobrescrever o elemento para atualizar
            alunos[indice] = novo_nome
        else:
            print('aluno nao encontrado')
