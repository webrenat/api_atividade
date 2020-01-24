from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Bento', idade=20)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Renato').first()
    #print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bento').first()
    pessoa.idade = 23
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bento').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def exclui_usuario():
    usuario = Usuarios.query.filter_by(login='lud').first()
    usuario.delete()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('renato','123')
    #insere_usuario('lud', '321')
    #exclui_usuario()
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()