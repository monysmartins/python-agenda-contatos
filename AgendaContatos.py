import sqlite3,time

conectar = sqlite3.connect(r'agenda.db')
c = conectar.cursor()

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone varchar, email text, data text)')


# Criando o Banco de Dados e Tabelas Caso não exista
try:
    criar_db()
except:
    print('Erro ao criar o banco de dados')
else:
    print('Banco de dados criado com sucesso')


def inserir(nome,tel,email):
    data = time.strftime('%d/%m/%Y')
    c.execute('INSERT INTO cadastro VALUES(?,?,?,?)',(nome,tel,email,data))
    conectar.commit()

def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql,(p,)):
        print('NOME: ',row[0])
        print('FONE: ',row[1])
        print('EMAIL: ',row[2])
        print('DATA: ',row[3])
        print()
        

def listarTodos():
    sql = 'SELECT * FROM cadastro'
    for row in c.execute(sql):
        print('NOME: ',row[0])
        print('FONE: ',row[1])
        print('EMAIL: ',row[2])
        print('DATA: ',row[3])
        print()
        

while True:

    fc = int(input(' 1 - Cadastrar \n 2 - Pesquisar \n 3 - Listar todos\n 4 - Sair \n O que você deseja fazer? \n'))
    
    if fc == 1:
        
        try:
            print('Cadastro da Agenda')
            time.sleep(2)
            nome = str(input("Digite Nome:"))
            tel = str(input("Digite Telefone:"))
            email = str(input("Digite Email:"))

            inserir(nome,tel,email)

        except:
            print('Erro ao Cadastrar!')
        else:
            print('Cadastrado com sucesso')
            
    elif fc==2:
        p = str(input('Digite o nome a ser buscado: '))
        print('Buscando...')
        time.sleep(1)
        pesquisar(p)

    elif fc == 3:
        print('TODOS OS CONTATOS')
        listarTodos()
    
    elif fc == 4:
        print('Finalizando...')
        time.sleep(3)
        break

    else:
        print('...')
        
