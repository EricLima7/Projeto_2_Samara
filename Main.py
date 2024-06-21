import banco_dados

conexao = banco_dados.criarConexaoInicial("localhost", "root", "mine1029")

banco_dados.criarBancoDados(conexao, "hospital")

campos_paciente = [
        "cpf VARCHAR(20) PRIMARY KEY",
        "nome VARCHAR(100)",
        "idade INT",
        "endereco VARCHAR(50)",
        "telefone VARCHAR(50)"
    ]

banco_dados.criarTabela(conexao, "pacientes", campos_paciente, "hospital")

def adicionar_novo_paciente():
    print("-Adicionar Novo Paciente:")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")

    if not cpf or not nome or not idade or not endereco or not telefone:
        print("Por favor, preencha todos os campos obrigatórios.")
        return

    sql_inserir_paciente = "INSERT INTO pacientes (cpf, nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
    dados_paciente = (cpf, nome, idade, endereco, telefone)
    banco_dados.insertNoBancoDados(conexao, sql_inserir_paciente, dados_paciente )

campos_medicos = [
        "nome VARCHAR(100) ",
        "especialidade VARCHAR(50) ",
        "crm VARCHAR(50) Primary Key",
        "telefone VARCHAR(50)"
    ]

banco_dados.criarTabela(conexao, "medicos", campos_medicos, "hospital")
def adicionar_novo_medico():
    print("-Adicionar Novo Médico:")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    crm = input("CRM: ")
    telefone = input("Telefone: ")

    if not nome or not especialidade or not crm or not telefone:
        print("Por favor, preencha todos os campos obrigatórios.")
        return
    sql_inserir_medico = "INSERT INTO medicos (nome, especialidade, crm, telefone) VALUES (%s, %s, %s, %s)"
    dados_medico = (nome, especialidade, crm, telefone)
    banco_dados.insertNoBancoDados(conexao, sql_inserir_medico, dados_medico)

def pesquisar_paciente_por_cpf():
    print("-Pesquisar Paciente por CPF:")
    cpf = input("Digite o CPF do paciente: ")
    sql_pesquisarPaciente = f"SELECT * FROM pacientes WHERE cpf = {cpf}"
    pacientes = banco_dados.listarBancoDados(conexao, sql_pesquisarPaciente)
    print(f"cpf: {pacientes[0][0]}")
    print(f"nome: {pacientes[0][1]}")
    print(f"idade: {pacientes[0][2]}")
    print(f"endereco: {pacientes[0][3]}")
    print(f"telefone: {pacientes[0][4]}")

def pesquisar_medico_por_crm():
    print("-Pesquisar Médico por CRM:")
    crm = input("Digite o CRM do médico: ")
    sql_pesquisarMedico = f"SELECT * FROM medicos WHERE crm = {crm}"
    medicos = banco_dados.listarBancoDados(conexao, sql_pesquisarMedico)
    print(f"nome: {medicos[0][0]}")
    print(f"especialidade: {medicos[0][1]}")
    print(f"crm: {medicos[0][2]}")
    print(f"telefone: {medicos[0][3]}")

def excluir_paciente_por_cpf():
    print("-Excluir Paciente por CPF:")
    cpf = input("Digite o CPF do paciente a ser excluído: ")
    sql_delete = "DELETE FROM pacientes WHERE cpf = %s"
    dados_delete = (cpf,)
    linhas_afetadas = banco_dados.excluirBancoDados(conexao, sql_delete, dados_delete)
    print(f"{linhas_afetadas} linhas foram excluídas.")
def excluir_medico_por_crm():
    print("-Excluir Médico por CRM:")
    crm = input("Digite o CRM do médico a ser excluído: ")
    sql_delete = "DELETE FROM medicos WHERE crm = %s"
    dados_delete = (crm,)
    linhas_afetadas = banco_dados.excluirBancoDados(conexao, sql_delete, dados_delete)
    print(f"{linhas_afetadas} linhas foram excluídas.")

campos_agendar_consulta = [
        "id INT AUTO_INCREMENT PRIMARY KEY",
        "paciente_cpf VARCHAR(20) ",
        "medico_crm VARCHAR(100)",
        "data VARCHAR(1000) ",
        "hora VARCHAR(50)",
        "FOREIGN KEY (paciente_cpf) REFERENCES pacientes (cpf)",
        "FOREIGN KEY (medico_crm) REFERENCES medicos (crm)"
    ]

banco_dados.criarTabela(conexao, "consultas", campos_agendar_consulta, "hospital")
def agendar_consulta():
    print("-Agendar Consulta:")
    paciente_cpf = input("CPF do paciente: ")
    medico_crm = input("CRM do médico: ")
    data = input("Data da consulta: ")
    hora = input("Hora da consulta: ")

    sql_agendar_consulta = "INSERT INTO consultas (paciente_cpf, medico_crm, data, hora) VALUES (%s, %s, %s, %s)"
    dados_consulta = (paciente_cpf, medico_crm, data, hora)
    banco_dados.insertNoBancoDados(conexao, sql_agendar_consulta, dados_consulta)

campos_registrar_procedimento_medico = [
        "id INT AUTO_INCREMENT PRIMARY KEY",
        "medico_crm VARCHAR(20) ",
        "paciente_cpf VARCHAR(100)",
        "data INT",
        "descricao VARCHAR(50)",
        "FOREIGN KEY (medico_crm) REFERENCES medicos (crm)",
        "FOREIGN KEY (paciente_cpf) REFERENCES pacientes (cpf)",

    ]

banco_dados.criarTabela(conexao, "procedimentos", campos_registrar_procedimento_medico, "hospital")
def registrar_procedimento_medico():
    print("Registrar Procedimento Médico")
    medico_crm = input("CRM do médico que realizou o procedimento: ")
    paciente_cpf = input("CPF do paciente que recebeu o procedimento: ")
    data = input("Data do procedimento: ")
    descricao = input("Descrição do procedimento realizado: ")
    paciente_existente = False
    medico_existente = False

def excluir_procedimento():
    print("-Excluir procedimento médico:")
    crm = input("Digite o CRM do médico a ser excluído: ")
    sql_delete = "DELETE FROM medicos WHERE crm = %s"
    dados_delete = (crm,)
    linhas_afetadas = banco_dados.excluirBancoDados(conexao, sql_delete, dados_delete)
    print(f"{linhas_afetadas} linhas foram excluídas.")

def main():
    while True:
        print("\n----Sistema de Gerenciamento Médico----")
        print("1. Adicionar Novo Paciente")
        print("2. Adicionar Novo Médico")
        print("3. Pesquisar Paciente por CPF")
        print("4. Pesquisar Médico por CRM")
        print("5. Excluir Paciente pelo CPF")
        print("6. Excluir Médico pelo CRM")
        print("7. Agendar Consulta")
        print("8. Registrar Procedimento Médico")
        print("9. Sair do Sistema")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            adicionar_novo_paciente()
        elif opcao == '2':
             adicionar_novo_medico()
        elif opcao == '3':
             pesquisar_paciente_por_cpf()
        elif opcao == '4':
            pesquisar_medico_por_crm()
        elif opcao == '5':
            excluir_paciente_por_cpf()
        elif opcao == '6':
            excluir_medico_por_crm()
        elif opcao == '7':
            agendar_consulta()
        elif opcao == '8':
            registrar_procedimento_medico()
        # elif opcao == '10':
        # elif opcao == '11':
        elif opcao == '12':
            print("Saindo do sistema...")
            break
        else:
             print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
