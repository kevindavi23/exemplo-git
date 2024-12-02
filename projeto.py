administradores = {'admin': 'josuelima', 'senha': 'josue2024'}
usuarios = {'kevin':"123"}
filmes = [{"categorias":"Magia","filme":"harry potter e o prisioneiro de azkaban","sinopse":"É o início do terceiro ano na escola de bruxaria Hogwarts. Harry, Ron e Hermione têm muito o que aprender. Mas uma ameaça ronda a escola e ela se chama Sirius Black. Após doze anos encarcerado na prisão de Azkaban, ele consegue escapar e volta para vingar seu mestre, Lord Voldemort. Para piorar, os Dementores, guardas supostamente enviados para proteger Hogwarts e seguir os passos de Black, parecem ser ameaças ainda mais perigosas."},{"categorias": "Ação","filme":"o exterminador do futuro","sinopse":"Disfarçado de humano, o assassino conhecido como o Exterminador viaja de 2029 a 1984 para matar Sarah Connor. Enviado para proteger Sarah está Kyle Reese, que divulga a chegada do Skynet, um sistema de inteligência artificial que detonará um holocausto nuclear. Sarah é o alvo porque a Skynet sabe que seu futuro filho comandará a luta contra eles. Com o implacável Exterminador os perseguindo, Sarah e Kyle tentam sobreviver."},{"categorias":"Comedia","filme":"Aprovados","sinopse":"Após ser recusado por todas as faculdades em que se inscreveu, Bartleby Gaines inventa uma forma de enganar a todos para pensarem que ele vai estudar: abre sua própria universidade. O jovem e seus amigos em situação semelhante tomam um prédio abandonado, criam um site falso, contratam o tio de um amigo para posar como o reitor e, pronto, nasce uma escola."},{"categorias":"Terror","filme":"Jogos Mortais - O Final","sinopse":"Sobreviventes se reúnem devido aos traumas adquiridos. Entre eles, o psicólogo que controla o encontro e não é uma vítima como as outras, mas tem segredos que podem reiniciar os ataques do psicopata."},{"categorias":"Aventura","filme":"Mad Max: Estrada da Fúria","sinopse":"Em um mundo pós-apocalíptico, Max Rockatansky acredita que a melhor forma de sobreviver é não depender de ninguém. Porém, após ser capturado pelo tirano Immortan Joe e seus rebeldes, Max se vê no meio de uma guerra mortal iniciada pela Imperatriz Furiosa, que tenta salvar um grupo de garotas. Também tentando fugir, Max aceita ajudá-la."},{"categorias":"Drama","filme":"milagre na cela 7","sinopse":"Memo, um pastor de ovelhas com deficiência mental, vive com sua filha e avó em uma vila na costa turca do mar Egeu. Um dia, sua vida é virada de cabeça para baixo quando a filha do comandante morre e Memo é acusado do assassinato e condenado à morte.",},{"categorias":"Ficção cientifica","filme":"Eu sou a lenda: ","sinopse":"Robert Neville é um brilhante cientista e o único sobrevivente de uma epidemia que transformou os humanos em mutantes sedentos por sangue. Andando pela cidade de Nova York, ele procura por outros possíveis sobreviventes e tenta achar a cura da praga usando seu próprio sangue, que é imune."}]


print('========= Bem vindo ao CINE Sertão ========== \n\n Escolha uma das opções abaixo!\n')

while (True):
    print('1 - Cadastrar Usuário ou ADM')
    print('2 - Comprar ingressos')
    print('3 - Gerenciar Filmes')

    opcao = int(input('Digite uma opção: '))


    # Opção para cadastro de usuário ou administrador
    if opcao == 1:
        print('\n1 - Cadastro de ADM\n2 - Cadastro de Usuário')
        opcao2 = int(input('Digite uma opção: '))

        # Cadastro de administrador
        if opcao2 == 1:
            admin = input('\nNome de Administrador: ')
            if admin in administradores:
                print('Administrador já existe. Escolha outro nome.')
            else:
                senha = input('Crie uma senha para o administrador: ')
                confirmar_senha = input('Confirme a senha: ')
                if senha == confirmar_senha:
                    administradores[admin] = senha
                    print('\033[0;32mCadastro feito com sucesso\033[m\n')
                else:
                    print('\033[0;31mAs senhas não coincidem\033[m\n')

        # Cadastro de usuário
        elif opcao2 == 2:
            usuario = input('\nNome de Usuário: ')
            if usuario in usuarios:
                print('Usuário já existe. Escolha outro nome.')
            else:
                senha = input('Crie uma senha para o usuário: ')
                confirmar_senha = input('Confirme a senha: ')
                if senha == confirmar_senha:
                    usuarios[usuario] = senha
                    print('\033[0;32mCadastro feito com sucesso\033[m\n')
                else:
                    print('\033[0;31mAs senhas não coincidem\033[m\n')


    # Opção para comprar ingressos (login de usuário)
    elif opcao == 2:
        print('\nFaça login para prosseguir na compra do ingresso...')
        usuario2 = input('Usuário: ')
        senha_usuario = input('Senha: ')

        # Verifica se o usuário existe e a senha corresponde
        if usuario2 in usuarios and usuarios[usuario2] == senha_usuario:
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
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 2):
                for elemento in filmes:
                   if elemento["categorias"] == "Comedia":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 3):
                for elemento in filmes:
                   if elemento["categorias"] == "Terror":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 4):
                for elemento in filmes:
                   if elemento["categorias"] == "Aventura":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 5):
                 for elemento in filmes:
                    if elemento["categorias"] == "Drama":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 6):
                for elemento in filmes:
                    if elemento["categorias"] == "Magia":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")
            if(categorias == 7):
                for elemento in filmes:
                    if elemento["categorias"] == "Ficção cientifica":
                       print("\nfilme: ", elemento["filme"],"\n")
                       print("sinopse: ", elemento["sinopse"], "\n")
                       print("deseja comprar o ingresso para assistir esse filme:")
                       ingresso = int(input("1: sim\n2: não "))
                       if(ingresso == 1):
                           print("ingresso comprado com sucesso\n")


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
            opcao3 = int(input('Digite uma opção: '))
            # Implementar opções de gerenciamento de filmes conforme desejado
        else:
            print('\033[0;31mAdmin ou senha incorreto\033[m\n')
