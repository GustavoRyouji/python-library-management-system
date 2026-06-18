from sistema.interface import *
def cadastrarCliente(conexao):
    cabeçalho('CADASTRO DE CLIENTE')
    try:
        Nome = input('Nome["0" para cancelar]: ')
        if Nome == '0':
            print('Cadastro cancelado')
            return
        cpf = str(input('CPF: '))
        tel = str(input('Telefone com DDD: '))
        cursor = conexao.cursor()
        cursor.execute("""
                    INSERT INTO clientes (Nome, CPF, Telefone) VALUES (?, ?, ?)
                       """, (Nome, cpf, tel))
        conexao.commit()
    except ValueError as erro:
        print('Erro ao cadastrar cliente. Erro: ', erro.__class__.__name__)
    else:
        print(linha())
        print('Cliente Cadastrado com sucesso')
        print(linha())
    
def visualizarClientes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    cliente = cursor.fetchall()
    mostrarcliente(cliente)



def buscarCliente(conexao):
    filtro = retornar(['Filtrar por ID', 
              'Filtrar por nome', 
              'Filtrar por CPF', 
              'Filtrar por Telefone'], 
              'Como deseja filtrar a lista?')
    
    if filtro == 1:
        print('-' * 42)
        resposta = leiaInt('Digite o ID do Cliente: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id LIKE ?",
                        (f"%{resposta}%",))
        clientes = cursor.fetchall()
        if not clientes:
            print('Nenhum Cliente encontrado.')
            return
        mostrarcliente(clientes)

    elif filtro == 2:
        print('-' * 42)
        resposta = input('Digite o nome do nome do Cliente: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes WHERE Nome LIKE ?" ,
                       (f"%{resposta}%",))
        clientes = cursor.fetchall()
        if not clientes:
            print('Nenhum Cliente encontrado.')
            return
        mostrarcliente(clientes)

    elif filtro == 3:
        print('-' * 42)
        resposta = input('Digite o CPF do Cliente: ')
        print('-' * 42)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes WHERE CPF LIKE ?", 
                       (f"%{resposta}%",))
        clientes = cursor.fetchall()
        if not clientes:
            print('Nenhum Cliente encontrado.')
            return
        mostrarcliente(clientes)

    elif filtro == 4:
        print('-' * 42)
        resposta = input('Digite o Telefone do Cliente: ')
        print('=' * 42)

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes WHERE Telefone LIKE ?",
                       (f"%{resposta}%",))
        clientes = cursor.fetchall()
        if not clientes:
            print("Nenhum Cliente encontrado.")
            return
        mostrarcliente(clientes)





def mostrarcliente(clientes):
    print('-' * 100)
    print(f'{"ID":<5} {"Nome":<35} {"CPF":<20} {"Telefone":<25}')
    print('-' * 100)

    for cliente in clientes:
        nome = cliente[1][:28] + '..' if len(cliente[1]) > 28 else cliente[1]
        print(f'{cliente[0]:<5} {nome:<30} {formatarCPF(cliente[2]):<20} {formatarTelefone(cliente[3])}')
        print('-'*100)




def editarClientes(conexao):
    cabeçalho('EDITAR CLIENTE')
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM clientes"
    )
    mostrarcliente(cursor.fetchall())
    id_cliente = leiaInt('Digite o ID do Cliente(0 pra cancelar): ')
    if id_cliente == 0:
        print('Operação Cancelada.')
        return
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    clientes = cursor.fetchone()
    if clientes is None:
        print('Nenhum Cliente encontrado.')
        return
    mostrarcliente([clientes])

    campo = retornar(['Nome', 'CPF', 'Telefone'], 'O que deseja editar?: ')
    novo_valor = input('Novo Valor: ')

    colunas = {1: 'Nome', 2: 'CPF', 3: 'Telefone'}
    cursor.execute(f"UPDATE clientes SET {colunas[campo]} = ? WHERE id = ?",
                   (novo_valor, id_cliente))
    conexao.commit()
    print('Atualizado com sucesso.')


def excluirCliente(conexao):
    cabeçalho('EXCLUSÃO DE CLIENTES')
    cpf = input('Digite o CPF do cliente (0 para cancelar): ')
    if cpf == '0':
        print('Exclusão Cancelada.')
        return
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE CPF = ?", (cpf,))
    cliente = cursor.fetchone()
    if cliente is None:
        print('Nenhum Cliente encontrado.')
        return
    mostrarcliente([cliente])
    
    id = leiaInt('Digite o ID do cliente para excluir: ')
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    print(linha())
    print('Cliente excluído com sucesso')
    print(linha())

