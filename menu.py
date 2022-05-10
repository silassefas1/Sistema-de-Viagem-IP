def menuPrincipal():
    print('-----------MENU---------')
    print('[1] - Menu de Motorista')
    print('[2] - Menu de Veículo')
    print('[3] - Menu de Viagem')
    print('[4] - SAIR')
    opcao = int(input("Digite uma opção: "))
    return opcao


def menuMotorista():
    print('-----------MENU MOTORISTAS---------')
    print('[1] - Cadastrar Motorista')
    print('[2] - Buscar Motorista por CPF')
    print('[3] - Editar Nome do Motorista') #antes Buscar por cpf o motorista
    print('[4] - Remover Motorista')
    print('[5] - Listar Todos os Motorista por Tipo da Carteira') #perguntar antes qual tipo da carteira ('A' - 'B' - 'AB')
    print('[6] - Listar Todos os Motorista')
    print('[7] - SAIR')
    opcao = int(input("Digite uma opção: "))
    return opcao


def menuVeiculo():
    print('-----------MENU---------')
    print('[1] - Cadastrar Veículo')
    print('[2] - Buscar Veículo por Placa')
    print('[3] - Adicionar Motorista ao Veículo')
    print('[4] - Remover Motorista do Veículo')
    print('[5] - Listar Veículos com Motoristas')
    print('[6] - Listar Veículos sem Motoristas')
    print('[7] - Remover Veículo')
    print('[8] - SAIR')
    opcao = int(input("Digite uma opção: "))
    return opcao


def menuViagem():
    print('-----------MENU---------')
    print('[1] - Criar Viagem')
    print('[2] - Finalizar Viagem por Placa')  # - Aqui muda somente o status de True para False
    print('[3] - Viagens Ativas')
    print('[4] - Veiculos que Estão em Viagem')
    print('[5] - Veiculos que Estão Disponíveis para Viagem')
    print('[6] - Listar Todas as viagens')
    print('[7] - Listar Todas as Viagens por Período')  # - data inicial e final (todas as viagens deste período)
    print('[8] - SAIR')
    opcao = int(input("Digite uma opção: "))
    return opcao
