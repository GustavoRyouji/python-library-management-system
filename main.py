from sistema.interface import *
from sistema.livro import *
from sistema.clientes import *
from sistema.emprestimos import *
import sqlite3
import os
import time

caminho = os.path.join(os.path.dirname(__file__), "sistema", "biblioteca.db")
conexao = sqlite3.connect(caminho)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY,
            Título TEXT,
            Autor TEXT,
            Categoria TEXT,
            Ano_Publicação INTEGER,
            Quantidade INTEGER)""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY,
               Nome TEXT,
               CPF TEXT,
               Telefone TEXT)""")



cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimos (
               id INTEGER PRIMARY KEY,
               id_clientes INTEGER,
               id_livros INTEGER,
               data_emprestimo DATE,
               data_devolucao DATE,
               status TEXT,
               valor_multa TEXT )""")



conexao.commit()

cabeçalho('SISTEMA DE GESTÃO DE LIVROS')
while True:
    escolha = menu(['Livros',
          'Clientes', 
          'Empréstimo', 
          'Sair do Programa'])
    

    if escolha == 1:
        while True:
            opc = retornar(['Cadastrar Livro', 
            'Listar Livros', 
            'Buscar Livro',
            'Editar Livro Cadastrado', 
            'Excluir Livro', 'Menu Principal'], 'MENU DE LIVROS')
            if opc == 1:
                while True:
                    cadastrarLivro(conexao)
                    time.sleep(2)
                    res = retornar(['Cadastrar novo livro', 'Menu de Livros', 'Menu Principal'], 
                                'Deseja cadastrar novo livro?: ')
                    if res == 2:
                        break
                    if res == 3:
                        break
                if res ==3:
                    break

            if opc == 2:
                cabeçalho('LISTA DE LIVROS')
                visualizarDB(conexao)
                time.sleep(2)
                res = retornar(['Menu de Livros', 'Menu Principal'], 'Retornar ao menu?')
                if res == 2:
                    break                   
    
            if opc == 3:
                while True:
                    buscarLivro(conexao)
                    time.sleep(2)
                    res = retornar(['Refazer Busca', 'Menu de Livros', 'Menu Principal'], 'Retornar ao Menu?')
                    if res == 2:
                        break
                    if res == 3:
                        break
                if res == 3:
                    break
        
            if opc == 4:
                while True:
                    editarLivros(conexao)
                    time.sleep(2)
                    res = retornar(['Editar Outro Livro', 'Menu de Livros'
                                    , 'Menu Principal'], 'Deseja Editar Outro Livro? ')
                    if res == 2:
                        break
                    if res == 3:
                        break
                if res == 3:
                    break

            if opc == 5:
                while True:
                    excluirLivro(conexao)
                    time.sleep(2)
                    res = retornar(['Menu de Livros', 'Menu Principal'], 'Deseja voltar ao menu?')
                    if res == 1:
                        break
                    if res == 2:
                        break
                if res == 2:
                    break


            if opc == 6:
                break




    if escolha == 2:
        while True:
            opc = retornar(['Cadastrar Clientes', 'Listar Clientes', 
                    'Buscar Clientes', 'Editar Informações de Clientes',
                    'Excluir Clientes', 'Voltar ao Menu Principal'],'Menu de Clientes')
            
            if opc == 1:
                while True:
                    cadastrarCliente(conexao)
                    time.sleep(2)
                    res = retornar(['Cadastrar Novo Cliente', 'Menu de Clientes'], 
                            'Retornar ao Menu?')
                    if res == 2:
                        break

            if opc == 2:
                cabeçalho('LISTA DE CLIENTES')
                visualizarClientes(conexao)
                time.sleep(2)
                res = retornar(['Menu de Clientes', 'Menu Principal'], 'Retornar ao menu?')
                if res == 2:
                    break

            if opc == 3:
                while True:
                    buscarCliente(conexao)
                    time.sleep(2)
                    res = retornar(['Refazer Busca', 'Menu de Clientes'], 'Retornar ao Menu?')
                    if res == 2:
                        break

            if opc == 4:
                while True:
                    editarClientes(conexao)
                    res = retornar(['Editar Outro Cliente', 'Menu de Clientes'
                                    , 'Menu Principal'], 'Deseja Editar Outro cliente? ')
                    if res == 2:
                        break
                    if res == 3:
                        break
                if res == 3:
                    break

            if opc == 5:
                while True:
                    excluirCliente(conexao)
                    time.sleep(2)
                    res = retornar(['Menu de Clientes', 'Menu Principal'], 'Deseja voltar ao menu?')
                    if res == 1:
                        break
                    if res == 2:
                        break
                if res == 2:
                    break


            if opc == 6:
                break




    if escolha == 3:
        while True:
            opc = retornar(['Novo Empréstimo', 'Lista de Empréstimos', 
            'Devolução de Livros', 'Menu Principal'], 'MENU DE EMPRÉSTIMOS')
            if opc == 1:
                while True:
                    emprestarLivros(conexao)
                    time.sleep(2)
                    res = retornar(['Novo empréstimo', 'Menu de Empréstimos'],
                                'Deseja voltar ao Menu?')
                    if res == 2:
                        break
            if opc == 2:
                while True:
                    listarEmprestimo(conexao)
                    time.sleep(2)
                    res = retornar(['Novo empréstimo', 'Menu de Empréstimos'],
                                'Deseja voltar ao Menu?')
                    if res == 2:
                        break
            if opc == 3:
                while True:
                    devolverLivro(conexao)
                    time.sleep(2)
                    res = retornar(['Nova devolução', 'Menu de Empréstimos'],
                                    'Deseja voltar ao Menu?')
                    if res == 2:
                        break
            if opc == 4:
                break

        
