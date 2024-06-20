# Lista para armazenar dados simulados em memória
pacientes = []
medicos = []
consultas = []
procedimentos = []

# Função para adicionar um novo paciente
def adicionar_novo_paciente():
    print("### Adicionar Novo Paciente ###")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")

    # Validar campos obrigatórios
    if not cpf or not nome or not idade or not endereco or not telefone:
        print("Por favor, preencha todos os campos obrigatórios.")
        return

    # Verificar se paciente já está cadastrado
    for paciente in pacientes:
        if paciente['cpf'] == cpf:
            print("Operação falhou: paciente já cadastrado.")
            return

    pacientes.append({
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'endereco': endereco,
        'telefone': telefone
    })
    print("Novo paciente cadastrado com sucesso!")

# Função para adicionar um novo médico
def adicionar_novo_medico():
    print("### Adicionar Novo Médico ###")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    crm = input("CRM: ")
    telefone = input("Telefone: ")

    # Validar campos obrigatórios
    if not nome or not especialidade or not crm or not telefone:
        print("Por favor, preencha todos os campos obrigatórios.")
        return

    # Verificar se médico já está cadastrado
    for medico in medicos:
        if medico['crm'] == crm:
            print("Operação falhou: médico já cadastrado.")
            return

    medicos.append({
        'nome': nome,
        'especialidade': especialidade,
        'crm': crm,
        'telefone': telefone
    })
    print("Novo médico cadastrado com sucesso!")

# Função para pesquisar paciente por CPF
def pesquisar_paciente_por_cpf():
    print("### Pesquisar Paciente por CPF ###")
    cpf = input("Digite o CPF do paciente: ")

    for paciente in pacientes:
        if paciente['cpf'] == cpf:
            print(f"CPF: {paciente['cpf']}, Nome: {paciente['nome']}, Idade: {paciente['idade']}, Endereço: {paciente['endereco']}, Telefone: {paciente['telefone']}")
            return
    print("Paciente não encontrado.")

# Função para pesquisar médico por CRM
def pesquisar_medico_por_crm():
    print("### Pesquisar Médico por CRM ###")
    crm = input("Digite o CRM do médico: ")

    for medico in medicos:
        if medico['crm'] == crm:
            print(f"Nome: {medico['nome']}, Especialidade: {medico['especialidade']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
            return
    print("Médico não encontrado.")

# Função para excluir paciente pelo CPF
def excluir_paciente_por_cpf():
    print("### Excluir Paciente por CPF ###")
    cpf = input("Digite o CPF do paciente a ser excluído: ")

    for paciente in pacientes:
        if paciente['cpf'] == cpf:
            pacientes.remove(paciente)
            print("Registro excluído com sucesso!")
            return
    print("Operação falhou: paciente não encontrado.")

# Função para excluir médico pelo CRM
def excluir_medico_por_crm():
    print("### Excluir Médico por CRM ###")
    crm = input("Digite o CRM do médico a ser excluído: ")

    for medico in medicos:
        if medico['crm'] == crm:
            medicos.remove(medico)
            print("Registro excluído com sucesso!")
            return
    print("Operação falhou: médico não encontrado.")

# Função para agendar consulta
def agendar_consulta():
    print("### Agendar Consulta ###")
    paciente_cpf = input("CPF do paciente: ")
    medico_crm = input("CRM do médico: ")
    data = input("Data da consulta: ")
    hora = input("Hora da consulta: ")

    # Verificar se paciente e médico existem
    paciente_existente = False
    medico_existente = False

    for paciente in pacientes:
        if paciente['cpf'] == paciente_cpf:
            paciente_existente = True
            break

    for medico in medicos:
        if medico['crm'] == medico_crm:
            medico_existente = True
            break

    if not paciente_existente or not medico_existente:
        print("Operação falhou: paciente ou médico não encontrado.")
        return

    consultas.append({
        'paciente_cpf': paciente_cpf,
        'medico_crm': medico_crm,
        'data': data,
        'hora': hora
    })
    print("Consulta agendada com sucesso!")

# Função para registrar procedimento médico
def registrar_procedimento_medico():
    print("### Registrar Procedimento Médico ###")
    medico_crm = input("CRM do médico que realizou o procedimento: ")
    paciente_cpf = input("CPF do paciente que recebeu o procedimento: ")
    data = input("Data do procedimento: ")
    descricao = input("Descrição do procedimento realizado: ")

    # Verificar se paciente e médico existem
    paciente_existente = False
    medico_existente = False

    for paciente in pacientes:
        if paciente['cpf'] == paciente_cpf:
            paciente_existente = True
            break

    for medico in medicos:
        if medico['crm'] == medico_crm:
            medico_existente = True
            break

    if not paciente_existente or not medico_existente:
        print("Operação falhou: paciente ou médico não encontrado.")
        return

    procedimentos.append({
        'medico_crm': medico_crm,
        'paciente_cpf': paciente_cpf,
        'data': data,
        'descricao': descricao
    })
    print("Procedimento médico registrado com sucesso!")

# Função principal para mostrar o menu e executar operações
def main():
    while True:
        print("\n### Sistema de Gerenciamento Médico ###")
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
        elif opcao == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
