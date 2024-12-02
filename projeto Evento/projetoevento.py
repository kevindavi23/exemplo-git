from funcoes import *
usuarios = [['kevin','kevin@gmail','123']]
eventos = [{'ANIMACZ','Um evento de anime que ocorre na cidade de Cajazeiras/PB, que reune varias atrações e competições de jogos e de cosplay. ','21/11/2024', 'Cajazeiras/PB', 25, 'kevin@gmail','mario','maria'},{'COMIC CON','A Comic Con Experience - CCXP , o maior evento para os amantes de quadrinhos, séries, filmes, literatura, games dentre outros âmbitos da cultura geek. A Comic Con Experience é uma convenção brasileira de entretenimento e quadrinhos de vários gêneros .', '05/12/2024', 'São paulo/SP', 100, 'kevin@gmail'},{'Jogatina XYZ', 'Um evento para jogadores de fifa se reúnirem e jogarem x1 para descubrirem quem é o melhor, o campeão ganhará um premio lendario digno de um proplayer.', '06/01/2025', 'Sousa/PB', 15, 'kevin@gmail'}]


op = -1
while(op != 0):
    print('\033[0;32m===================== EVENTIN =======================\033[m\n')

    print('1-Cadastrar usuário')
    print('2-Login')
    print('0-Sair do programa\n')
    op = int(input('Digite a opção desejada: '))
    if(op == 1):
        nome = input('Digite seu nome: ')
        email = input('digite seu e-mail: ')
        senha = input('digite sua senha: ')
        senha2 = input('Repita sua senha: ')
        if("@" in email):
            while(verificar_user_existente(email, usuarios)):
                email = input('digite novamente seu e-mail')
            while(not verificar_senha(senha, senha2)):
                print('dessa vez digite senhas iguais')
                senha = input('digite sua senha')
                senha2 = input('Repita sua senha')
            print('\033[0;32mUsuario cadastrado com sucesso. \033[m\n')
            usuarios.append([nome, email, senha])
        else:
            print('\033[0;31mEmail invalido, digite o @.\033[m\n')    
    elif(op == 2):
        validação1 = input('digite seu email: ')
        validação2 = input('digite sua senha: ')
        if(verificar_user_existente (validação1, usuarios) and verificar_senha_correta (validação2, usuarios)):
            opcao = -1
            print('\033[0;32mLogin feito com sucesso.\033[m\n')
            while(opcao != 8):
                print('1. Cadastrar novos eventos')
                print('2. Buscar eventos')
                print('3. Lista de eventos')
                print('4. Remover evento')
                print('5. Fazer inscrição em eventos')
                print('6. Lista de participantes e valor arrecardado do seu evento')
                print('7. Exibir ticke de suas inscrições em eventos')
                print('8. Voltar ao início\n')
                opcao = int(input('digite a opção desejada: '))
                if(opcao == 1):
                    opcao_1(eventos, validação1)

                elif(opcao == 2):
                    buscaev = input('Digite o nome do evento: ')
                    buscar_evento(buscaev, eventos)

                elif(opcao == 3):
                   opcao_3(eventos)

                elif(opcao == 4):
                    opcao_4(eventos, validação1)

                elif(opcao == 5):
                    opcao_5(eventos, validação1, usuarios)

                elif(opcao == 6):
                    opcao_6(eventos)

                elif(opcao == 7):
                    opcao_7(eventos, validação1, usuarios)                                                                                                                           
        else:
            print('\033[0;31mEmail ou senha incorreto.\033[m\n')    