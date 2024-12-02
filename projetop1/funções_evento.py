def verificar_senha(senha1, senha2):
    if(senha1 == senha2):
        return True
    else:
        return False
def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if(user[1] == email):
            existe = True
            break
    return existe
def verificar_senha_correta(senha, usuarios):
    existe = False
    for user in usuarios:
        if(user[2] == senha):
            existe = True
            break
    return existe
def buscar_evento(nomeev, eventos):
    existe = False
    for evs in eventos:
        if(evs[0] == nomeev):
            existe = True
            print('\033[0;32mEvento encontrado com sucesso\033[m\n')
            print(evs[0],"\n")
            print(f'Descrição do evento: {evs[1]}\n')
            print(f'Data do evento: {evs[2]}.\n')
            print(f'Local do evento: {evs[3]}.\n')
            print(f'Valor da inscrição: R${evs[4]}.\n')        
    if(existe == False):
        print('\033[0;31mEvento não encontrado\033[m\n')
    voltar = input('Digite qualquer coisa para voltar ao incio: ')
def retorna_nomes(email):
    for i in usuarios:
        if(i[1] == email):
            return i[0]