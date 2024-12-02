
ligado = True
tarefas = []
tarefasfeitas = []
while(ligado):
    print('\n', tarefas, '\n')
    opcao = int(input('Digite uma das opções:\n1 - adicionar\n2 - buscar\n3 - atualizar\n4 - apagar\n0 - sair\n\nOpção:'))
    if(opcao == 1):
        afazer = input('Digite uma tarefa para adicionar: ')
        if(afazer in tarefas):
            print('Esse tarefa já foi cadastrado antes')
        else:
            tarefas.append(afazer)
           
    elif(opcao == 2):
        tarefas = input('Digite uma tarefa para buscar')
        if(tarefas in afazer):
            print('tarefa encontrado na lista', tarefas)
        else:
            print('A tarefa buscado não existe na lista')
    elif(opcao == 3):
        nomedatarefa = input('Digite a tarefa antiga')

        if(nomedatarefa not in tarefas):
            tarefas.append(nomedatarefa)
        else:
            tarefanova = input('Digite o nome novo')
            contador = 0
            for tarefasBusca in tarefas:
                if(nomedatarefa == tarefasBusca):
                    break
                contador += 1

            tarefas[contador] = tarefanova
    elif(opcao == 4):
        tarefaApagar = input('Digite uma tarefa  que deseja apagar')

        if(tarefaApagar not in tarefas):
            print('Não foi possível apagar, pois a tarefa não está na lista')
        else:
            tarefas.remove(tarefaApagar)
    elif(opcao == 5):
            tarefasfeitas = input("digite as tarefas realizadas")
            if(tarefasfeitas not in tarefas):
                tarefasfeitas.append(tarefasfeitas)
                tarefas.remove(tarefasfeitas)
    elif(opcao == 0):
        ligado = False
    else:
        print('Opção inválida')
        