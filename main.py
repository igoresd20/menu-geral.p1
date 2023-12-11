usuarios = []
noticias = []



def cadastrar_adm ():
    linha()
    nome = input('digit seu nome :')
    linha()
    email = input('digite seu email :')
    linha()
    senha = input('digite a senha')
    linha()
    administrador = {'nome': nome, 'email': email, 'senha': senha}
    linha()

    print ('Administrador cadastrado com sucesso!')

    menu_adm()



def login ():
    email = input ('digite seu nome : ')
    senha = input ('digite seu email :' )
    usuario = { 'email': email, 'senha': senha}


def linha():
    print('--'*10)


def linha_menu():

    print('*'* 20)




def cadastrar_usuar ():
    linha()
    email = input('digite seu email :')
    linha()
    senha = input('digite a senha')
    linha()
    usuario = {'email': email, 'senha': senha}
    linha()
    menu_usua()
    linha()

def email_existe(email):
    # Verificar se o email já existe na lista de usuários
    for user in usuarios:
        if user['email'] == email:
            return True
    return False

def menu_adm():
    linha_menu()
    print('menu principal do adm : ')
    linha_menu()
    print('1. Inserir noticías ')
    linha()
    print('2.Listar notícias')
    linha()
    print('3. Excluir noticias')
    linha()
    print('4. Editar noticias')
    linha()
    print('5. Buscar  noticias')
    linha()
    print('6. Buscar  noticias')
    linha()

    escolha = input(print('escolha uma opção : '))

    if escolha == '1':
        inserir_noticias
    else: print('sair do programa')



def menu_usua():
    linha_menu()
    print('menu principal do usua : ')
    linha_menu()
    print('1. Buscar noticías ')
    linha()
    print('2.Comentar notícias')
    linha()
    print('3. Curtir noticias')
    linha()

    escolha = input(print('escolha uma opção : '))







def inserir_noticias ():

       titulo = str(input('Título da noticia : '))
       noticia = str(print('escreva a sua noticia '))
       noticias = {'titulo':titulo,'noticia':noticia}





def menu_principal ():
    linha_menu()
    print('menu principal ')
    linha_menu()
    print('1. cadastrar adm ')
    linha()
    print('2.login')
    linha()
    print('3. cadastrar usuario')
    linha()
    print('0. sair do sistema')
    linha()

    escolha = input('escolha uma opção : ')

    if escolha == '1':
        cadastrar_adm()
    elif escolha == '2':
        login()
    elif escolha == '3':
         cadastrar_usuar()
    elif escolha == '0':
        print('saindo do sistema')

menu_principal()












