import mysql.connector
# Função para iniciar conexão com o mysql
def criarConexaoInicial(endereco, usuario, senha):
    return mysql.connector.connect(
        host=endereco,
        user=usuario,
        password=senha
    )
# Função para finalizar conexão com o mysql
def encerrarBancoDados(connection):
    connection.close()
def criarBancoDados(connection, nome_bd):
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_bd}")
    cursor.close()
def criarTabela(connection, nome_tabela, campos, nome_banco_dados):
    cursor = connection.cursor()
    cursor.execute(f"USE {nome_banco_dados}")
    sql = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({', '.join(campos)})"
    cursor.execute(sql)
    cursor.close()
    print(f"Tabela '{nome_tabela}' criada ou já existente.")
def listarTabelas(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    cursor.close()
    return tabelas
# Função para inserir dados na tabela
def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id
# Função para listar dados da tabela
def listarBancoDados(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results
# Função para atualizar dados na tabela
def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas
# Função para excluir dados da tabela
def excluirBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas