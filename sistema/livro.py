from sistema.interface import *

def cadastrarLivro(conexao):
    cabeçalho('CADASTRO DE LIVRO')
    try:
        titulo = str(input('Título("0" pra cancelar): '))
        if titulo == '0':
            print('Cadastro Cancelado.')
            return
        autor = str(input('Autor: '))
        categoria = str(input('Categoria: '))
        ano = int(input('Ano de Publicação: '))
        quant = int(input('Quantidade: '))
        cursor = conexao.cursor()

        cursor.execute(
            '''INSERT INTO livros (Título, Autor, Categoria, Ano_Publicação, Quantidade) 
            VALUES(?, ?, ?, ?, ?)
            ''',
            (titulo, autor, categoria, ano, quant)
        )

        conexao.commit()
    except ValueError as erro:
        print('Erro ao adicionar Livro. Erro: ', erro.__class__.__name__)
    else:
        print(linha())
        print('Livro adicionado com sucesso')
        print(linha())



def excluirLivro(conexao):
    cabeçalho('EXCLUSÃO DE LIVRO')
    titulo = input('Digite o Título do Livro (0 para cancelar):')
    if titulo == '0':
        print('Exclusão Cancelada.')
        return
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros WHERE Título LIKE ?",
                        (f"%{titulo}%",))
    livros = cursor.fetchall()
    mostrarLivros(livros)
    id = leiaInt('Digite o ID do livro que deseja excluir: ')

    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
    conexao.commit()
    print(linha())
    print('Livro excluído com sucesso')
    print(linha())








def visualizarDB(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    cursor.execute("SELECT * FROM livros ORDER BY id")
    livros = cursor.fetchall()
    mostrarLivros(livros)
    

def buscarLivro(conexao):
    filtro = retornar(['Filtrar por Título', 
              'Filtrar por Autor', 
              'Filtrar por Categoria', 
              'Filtrar por Ano de Publicação'], 
              'Como deseja filtrar a lista?')
    
    if filtro == 1:
        print('-' * 42)
        resposta = input('Digite o Título do livro: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros WHERE Título LIKE ?",
                        (f"%{resposta}%",))
        livros = cursor.fetchall()
        if not livros:
            print('Nenhum livro encontrado.')
            return
        mostrarLivros(livros)

    elif filtro == 2:
        print('-' * 42)
        resposta = input('Digite o nome do autor: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros WHERE Autor LIKE ?" ,
                       (f"%{resposta}%",))
        livros = cursor.fetchall()
        if not livros:
            print('Nenhum livro encontrado.')
            return
        mostrarLivros(livros)

    elif filtro == 3:
        print('-' * 42)
        resposta = input('Digite a Categoria do livro: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros WHERE Categoria LIKE ?", 
                       (f"%{resposta}%",))
        livros = cursor.fetchall()
        if not livros:
            print('Nenhum livro encontrado.')
            return
        mostrarLivros(livros)

    elif filtro == 4:
        print('-' * 42)
        resposta = int(input('Digite o Ano de Publicação do Livro: '))
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros WHERE Ano_Publicação LIKE ?", 
                       (resposta,))
        livros = cursor.fetchall()
        if not livros:
            print('Nenhum livro encontrado.')
            return
        mostrarLivros(livros)
        

def mostrarLivros(livros):
    print('-' * 100)
    print(f'{"ID":<5} {"Título":<35} {"Autor":<19} {"categoria":<20} {"Ano":<8} {"Qtd":<5}')
    print('-' * 100)

    for livro in livros:
        print(
            f'{livro[0]:<5}'
            f'{livro[1]:<35}'
            f'{livro[2]:<23}'
            f'{livro[3]:<20}'
            f'{livro[4]:<10}'
            f'{livro[5]:<5}')
        print('-'*100)

def editarLivros(conexao):
    cabeçalho('EDITAR LIVRO')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    mostrarLivros(cursor.fetchall())
    id_livro = leiaInt('Digite o ID do Livro (0 pra cancelar): ')
    if id_livro == 0:
        print('Operação Cancelada.')
        return
    cursor.execute("SELECT * FROM livros WHERE id = ?", (id_livro,))
    livro = cursor.fetchone()
    if livro is None:
        print('Livro não encontrado.')
        return
    mostrarLivros([livro])

    campo = retornar(['título', 'Autor', 'Categoria', 'Ano_Publicação'
                      , 'Quantidade'], 'O que dejesa editar? ')
    novo_valor = input('Novo Valor: ')

    colunas = {1: 'Título', 2: 'Autor', 3: 'Categoria', 4: 'Ano_Publicação'
    , 5: 'Quantidade'}
    cursor.execute(f"UPDATE livros SET {colunas[campo]} = ? WHERE id = ? ", 
                   (novo_valor, id_livro))
    conexao.commit()
    print('Atualizado com sucesso.')





