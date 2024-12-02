administradores = {'jojo': '123'}
usuarios = {'kevin':"123" }
dados_usuarios = []
filmes = [{"categorias":"Magia","filme":"harry potter e o prisioneiro de azkaban","sinopse":"É o início do terceiro ano na escola de bruxaria Hogwarts. Harry, Ron e Hermione têm muito o que aprender. Mas uma ameaça ronda a escola e ela se chama Sirius Black. Após doze anos encarcerado na prisão de Azkaban, ele consegue escapar e volta para vingar seu mestre, Lord Voldemort. Para piorar, os Dementores, guardas supostamente enviados para proteger Hogwarts e seguir os passos de Black, parecem ser ameaças ainda mais perigosas.","sala":"5","horário de exibição do filme":"19:00 Hrs","capacidade":30,"valor do ingresso":15,"contador":0},
          {"categorias": "Ação","filme":"o exterminador do futuro","sinopse":"Disfarçado de humano, o assassino conhecido como o Exterminador viaja de 2029 a 1984 para matar Sarah Connor. Enviado para proteger Sarah está Kyle Reese, que divulga a chegada do Skynet, um sistema de inteligência artificial que detonará um holocausto nuclear. Sarah é o alvo porque a Skynet sabe que seu futuro filho comandará a luta contra eles. Com o implacável Exterminador os perseguindo, Sarah e Kyle tentam sobreviver.","sala":"6","horário de exibição do filme":"20:00 Hrs","capacidade":25,"valor do ingresso":12,"contador":0},
          {"categorias":"Comedia","filme":"aprovados","sinopse":"Após ser recusado por todas as faculdades em que se inscreveu, Bartleby Gaines inventa uma forma de enganar a todos para pensarem que ele vai estudar: abre sua própria universidade. O jovem e seus amigos em situação semelhante tomam um prédio abandonado, criam um site falso, contratam o tio de um amigo para posar como o reitor e, pronto, nasce uma escola.","sala":"7","horário de exibição do filme":"15:00 Hrs","capacidade":20 ,"valor do ingresso":10 ,"contador":0},
          {"categorias":"Terror","filme":"jogos Mortais - O Final","sinopse":"Sobreviventes se reúnem devido aos traumas adquiridos. Entre eles, o psicólogo que controla o encontro e não é uma vítima como as outras, mas tem segredos que podem reiniciar os ataques do psicopata.","sala":"8","horário de exibição do filme":"21:00 Hrs","capacidade":30 ,"valor do ingresso":16,"contador":0},
          {"categorias":"Aventura","filme":"mad max: estrada da fúria","sinopse":"Em um mundo pós-apocalíptico, Max Rockatansky acredita que a melhor forma de sobreviver é não depender de ninguém. Porém, após ser capturado pelo tirano Immortan Joe e seus rebeldes, Max se vê no meio de uma guerra mortal iniciada pela Imperatriz Furiosa, que tenta salvar um grupo de garotas. Também tentando fugir, Max aceita ajudá-la.","sala":"9","horário de exibição do filme":"20:00 Hrs","capacidade": 15,"valor do ingresso":10 ,"contador":0},
          {"categorias":"Drama","filme":"milagre na cela 7","sinopse":"Memo, um pastor de ovelhas com deficiência mental, vive com sua filha e avó em uma vila na costa turca do mar Egeu. Um dia, sua vida é virada de cabeça para baixo quando a filha do comandante morre e Memo é acusado do assassinato e condenado à morte.","sala":"10","horário de exibição do filme":"16:00 Hrs","capacidade":25 ,"valor do ingresso":12 ,"contador":0},
          {"categorias":"Ficção cientifica","filme":"Eu sou a lenda","sinopse":"Robert Neville é um brilhante cientista e o único sobrevivente de uma epidemia que transformou os humanos em mutantes sedentos por sangue. Andando pela cidade de Nova York, ele procura por outros possíveis sobreviventes e tenta achar a cura da praga usando seu próprio sangue, que é imune.","sala":"11","horário de exibição do filme":"22:00 Hrs","capacidade": 30,"valor do ingresso": 20 ,"contador":0}]
usuario2 = ""








print('=-=-=-=-=-=- Bem vindo ao CINE Sertão =-=-=-=-=-=-\n\n -> Escolha uma das opções abaixo!\n')

while True:
    print('1 - Cadastrar Usuário ou ADM')
    print('2 - Comprar ingressos')
    print('3 - Gerenciar Filmes')
    print('0 - Finalizar/Sair')

    opcao = int(input('Digite uma opção: '))


    # Opção para cadastro de usuário ou administrador
    if opcao == 1:
        print('\n1 - Cadastro de ADM\n2 - Cadastro de Usuário')
        opcao2 = int(input('Digite uma opção: '))

        # Cadastro de administrador
        if opcao2 == 1:
            print('\n---- Cadastro de Administrado ----_-\n')
            admin = input('\nNome de Administrador: ')
            email = str(input('Digite seu e-mail: '))

            # Verificar de o @ está no endereço de e-mail
            if '@' not in email or '.com' not in email:
                print('\033[0;31mE-mail inválido.\033[m\n')
            else:
                print('\033[0;32mE-mail verificado com sucesso!\033[m\n')
                dados_usuarios.append(email)

            if admin in administradores:
                print('Administrador já existe. Escolha outro nome.')
            else:
                senha = input('Crie uma senha para o administrador: ')
                confirmar_senha = input('Confirme a senha: ')
                if senha == confirmar_senha:
                    administradores[admin] = senha
                    dados_usuarios.append(administradores.copy())
                    print('\033[0;32mCadastro feito com sucesso\033[m\n')
                else:
                    print('\033[0;31mAs senhas não coincidem\033[m\n')

        # Cadastro de usuário
        elif opcao2 == 2:
            print('\n---- Cadastro de Usuários ----_-\n')
            usuario = input('\nNome de Usuário: ')
            email = str(input('Digite seu e-mail: '))

            # Verificar de o @ está no endereço de e-mail
            if '@' not in email or '.com' not in email:
                print('\033[0;31mE-mail inválido.\033[m\n')
            else:
                print('\033[0;32mE-mail verificado com sucesso!\033[m\n')
                dados_usuarios.append(email)
            if usuario in usuarios:
                print('Usuário já existe. Escolha outro nome.')
            else:
                senha = input('Crie uma senha para o usuário: ')
                confirmar_senha = input('Confirme a senha: ')

                if senha == confirmar_senha:
                    usuarios[usuario] = senha
                    dados_usuarios.append(usuarios.copy())
                    print(dados_usuarios)
                    print('\033[0;32mCadastro feito com sucesso\033[m\n')
                else:
                    print('\033[0;31mAs senhas não coincidem\033[m\n')


    # Opção para comprar ingressos (login de usuário)
    elif opcao == 2:
        print('\nFaça login para prosseguir na compra do ingresso...')
        usuario2 = input('Usuário: ')
        senha_usuario = input('Senha: ')

        # Verifica se o usuário existe e a senha corresponde
        if usuario2 in usuarios and senha_usuario == usuarios[usuario2]:
            print('\033[0;32mLogin feito com sucesso\033[m\n')
            print('====== Página de Usuários ======')
            print('selecione o genero do filme que você deseja assistir:')
            print ('Digite 1: Ação')
            print ('Digite 2: Comedia')
            print ('Digite 3: Terror')
            print ('Digite 4: Aventura')
            print ('Digite 5: Drama')
            print ('digite 6: Magia')
            print ('digite 7: Ficção cientifica')
            categorias = int(input("digite o numero da categoria escolhida: "))
            if(categorias == 1):
                for elemento in filmes:
                   if elemento["categorias"] == "Ação":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n") 
                       print("deseja comprar o ingresso para assistir esse filme:")  
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= (elemento["capacidade"]):
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '        Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")

            if(categorias == 2):
                for elemento in filmes:
                   if elemento["categorias"] == "Comedia":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= elemento["capacidade"]:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '                Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                             valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
            if(categorias == 3):
                for elemento in filmes:
                   if elemento["categorias"] == "Terror":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], " pessoas", "\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= elemento["capacidade"]:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '        Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
                                   
            if(categorias == 4):
                for elemento in filmes:
                   if elemento["categorias"] == "Aventura":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= elemento["capacidade"]:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '        Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
            if(categorias == 5):
                 for elemento in filmes:
                    if elemento["categorias"] == "Drama":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= elemento["capacidade"]:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '               Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
            if(categorias == 6):
                for elemento in filmes:
                    if elemento["categorias"] == "Magia":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] <= elemento["capacidade"]:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '        Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
            if(categorias == 7):
                for elemento in filmes:
                    if elemento["categorias"] == "Ficção cientifica":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("sala : ", elemento["sala"], "\n")
                       print("horário de exibição do filme :", elemento["horário de exibição do filme"], "\n")
                       print("capacidade :", elemento["capacidade"], "pessoas\n")
                       print("valor do ingresso :", elemento["valor do ingresso"], "R$\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           total = int(input("quantos ingressos você deseja comprar: "))
                           if total > 0 + elemento["contador"] < elemento["capacidade"]-1:
                                elemento["contador"] += total
                                precototal = total* elemento["valor do ingresso"]
                                print("\033[0;32mingresso comprado com sucesso\033[m\n")
                                print('-------------------------------------------  Cine Sertão  ------------------------------------')
                                print('\nsala : ', elemento["sala"],'                ========== Ticket de compra ========       cliente :',usuario2)
                                print('horário de exibição do filme : ',elemento["horário de exibição do filme"], '               Filme escolhido:', elemento["filme"] )
                                print("quantidade de ingresso (s):",total,              "                                  valor da compra:", precototal,"R$")
                                print('\n--------------------------------------Desejamos um ótimo filme!-------------------------------')
                           else :
                               print("\033[0;31mquantidade de ingressos indisponivel\033[m\n")
            
            

        else:
            print('\033[0;31mUsuário ou senha incorreto\033[m\n')

    # Opção para gerenciar filmes (login de administrador)
    elif opcao == 3:
        admin2 = input('Admin: ')
        senha_admin = input('Senha: ')

        # Verifica se o administrador existe e a senha corresponde
        if admin2 in administradores and administradores[admin2] == senha_admin:
            print('\033[0;32mLogin feito com sucesso\033[m\n')
            print('------ Página de Administradores ------')
            print('Gerenciamento de filmes:')
            print('1 - Cadastrar novo Filme')
            print('2 - Buscar Filmes')
            print('3 - Atualizar Filmes')
            print('4 - Remover Filmes')
            print('5 - alterar preços,horários,salas e capacidade')
            opcao3 = int(input('Digite uma opção: '))
            # Implementar opções de gerenciamento de filmes conforme desejado

            # Cadastrar filme
            if opcao3 == 1:

                adicionar_filme = input('\nDigite o nome do filme que deseja adicionar: ')
                categoriadofilme = input("\ndigite a categoria que você deseja adicionar o filme: ")
                sinopse = str(input('\nDigite a sinopse do filme: '))
                sala = input("\ndigite a sala do filme: ")
                horario = input("\ndigite o horario de exibição do filme: ")
                valor = int(input("\ndigite o valor do ingresso: "))
                capacidade = int(input("\ndigite a capacidade da sala: "))
                dicionario = {"filme":adicionar_filme,"sinopse":sinopse,"categorias":categoriadofilme,"sala":sala,"horário de exibição do filme":horario,"valor do ingresso":valor,"capacidade":capacidade, "contador":0}
                filmes.append(dicionario.copy())
                print('\n\033[0;32mFilme adicionado com sucesso\033[m\n')


            # Buscar filmes
            elif opcao3 == 2:
                buscar_filmes = input('Digite o filme que deseja buscar: ')

                # Verificar se o filme buscado existe
                achou = False
                for elemento in filmes:
                    if elemento["filme"] == buscar_filmes:
                        achou = True
                        print("\033[0;32mfilme encontrado com sucesso\033[m\n")

                if achou == False:
                    print('\033[0;31mFilme não encontrado, por favor digite outro título!!\033[m\n')


            # Atualizar filme
            elif opcao3 == 3:
                atualizar_filme = input('Digite o nome do filme que deseja atualizar: ')
                encontrou = False
                for elemento in filmes:
                    if elemento['filme'] == atualizar_filme:
                        encontrou = True
                        atualizar2 = input("digite o nome do novo filme: ")
                        elemento["filme"] = atualizar2
                        print("filme atualizado com sucesso")
                        atualizarsinopse = input("digite a nova sinopse: ")
                        elemento["sinopse"] = atualizarsinopse
                        print("sinospe atualizada com sucesso")
                
                if encontrou == False:
                    print("filme não encontrado")


            # Deletar filmes
            elif opcao3 == 4:
                deletar_filme = input('Digite o nome do filme que deseja Deletar: ')

                # verificar so o filme digitado exite
                achou2 = False
                for elemento in filmes:
                    if elemento["filme"] == deletar_filme:
                        achou2 = True
                        filmes.remove(elemento)
                        print('\n\033[0;32mFilme removido com sucesso!\033[m\n')
                if achou2 == False:
                    print('\n\033[0;31mO filme digitado não existe\033[m\n')
             #alterar preços e etc   
            elif opcao3 == 5:
                    alterar1 = input("digite o nome do filme: ")
                    achou = False
                    for elemento in filmes:
                        if alterar1 == elemento["filme"]:
                            achou = True
                            print("1- alterar preços dos ingressos")
                            print("2- alterar horários dos filmes")
                            print("3- alterar salas")
                            print("4- alterar capacidades das salas")
                            alterar = int(input("digite uma opção: "))
                    
                            if alterar == 1:
                                novopreço = float(input("digite o novo preço do ingresso: "))
                                elemento["valor do ingresso"] = novopreço
                                print("preço alterado com sucesso")

                            elif alterar == 2:
                                novohorario = float(input("digite o novo horário: "))  
                                elemento["horário de exibição do filme"] = novohorario
                                print("horário alterado com sucesso")

                            elif alterar == 3:
                                novasala = float(input("digite o novo numero da sala: "))
                                elemento["sala"] = novasala
                                print("sala alterada com sucesso")

                            elif alterar == 4:
                                novacapacidade = float(input("digite a nova capacidade da sala: "))
                                elemento["capacidade"] = novacapacidade
                                print("capacidade alterada com sucesso")
                    if(achou == False):
                        print("filme não encontrado")
                           




            

                    
                    

                    


        else:
            print('\033[0;31mAdmin ou senha incorreto\033[m\n')
    elif opcao == 0: 
        break

print('----------------------------------------------------------------------------------')
print('|--------------- CINE Sertão ---------- --------_-                               |')
print('|                                                                                |')
print('|   Obrigado pela preferência,         desejamos a todos um ótimo filme!!        |')
print('|                                                                                |')
print('|            ADM01 = Kevin Davi           ADM02 = Josue Lima                     |')
print('----------------------------------------------------------------------------------')

