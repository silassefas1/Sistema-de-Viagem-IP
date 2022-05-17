from controladorVeiculo import cadastrarVeiculo
from bancoGeral import get_bv, get_bvia, ler, escrever

# ========================================= Viajem ===================================================================

placa = None
status = None



def criarViajem():
    ler()
    while True:  # cadastro Veiculo===================================================================================
        print('Cadastro Viajem')
        cont = len(get_bv())
        for veiculo in get_bvia():
            if veiculo in get_bv():
                cont -= 1
        if cont == 0:
            print('Não ha veiculos disponiveis ou todos os veículos já estão em viagem.')
            opcao = int(input('Deseja cadastrar um novo veiculo?\n'
                              '1 - Sim\n'
                              '2 - Não\n'))
            if opcao == 1:
                cadastrarVeiculo()
            else:
                break

        else:
            # mostrar todos os veiculos do banco==========================================================================
            print('Selecione um veiculo para a viajem:')
            for veiculo in get_bv():
                if not veiculo in get_bvia():
                    print(veiculo)

            selecao_Veiculo = input('Insira a placa do veiculo para a viajem: ').upper()
            placa = selecao_Veiculo
            if not selecao_Veiculo in get_bv():
                print('Veiculo não cadastrado.')
                novamente = int(input('1 Cadastra um veiculo \n'
                                      '2 Tentar novamente.'))
                if novamente == 1:
                    cadastrarVeiculo()
                elif novamente == 2:
                    criarViajem()
            # cadastro rota===================================================================================
            print('Cadastro de Rota')
            rota = str(input('Digite o destino: ')).title()

            # Data da viajem===================================================================================
            print('Cadastra datas da viajem')
            global diaInicio, mesInicio
            diaInicio = int(input('Digite o dia do começo da viajem: '))
            dia(diaInicio)
            mesInicio = int(input('Digite o mes da viajem: '))
            mes(mesInicio)
            diaFim = int(input('Digite o dia do fim da viajem: '))
            dia(diaFim)
            mesFim =int(input('Digite o mes da viajem: '))
            mes(mesFim)
            inicio = diaInicio, mesInicio
            fim = diaFim, mesFim
            # atribuir status===================================================================================
            print('Viajem iniciada.')
            status = True
            # alimentar dicionario===================================================================================
            viagem = {'Veiculo': placa, 'Destino': rota, 'Status': status, 'inicio': inicio, 'fim': fim}
            get_bvia()[placa] = viagem
            escrever()
            print('Viajem cadastrada.')

            # Nova Viajem===================================================================================
            novo_cadastro = int(input('Deseja fazer um novo cadastro? \n'
                                      '1 - Sim\n'
                                      '2 - Não\n'))

            if novo_cadastro == 1:
                criarViajem()
            else:
                print('Pressione enter para voltar ao menu...')
                input()
            break


def fimViajem():
    ler()
    print('Qual Viajem você deseja finalizar: ')
    for a, b in get_bvia().items():
        if b.get('Status'):
            print(a)
    placa = input('Digite a placa do veiculo em viajem: ').upper()
    cadastrado = False
    for a in get_bvia().values():
        if placa == a.get("Veiculo"):
            cadastrado = True
            a['Status'] = False
            escrever()
    if cadastrado:
        print('Viajem Finalizada com sucesso.')
        input('Presione enter para voltar ao menu.')
    else:
        print("Esse veículo não existe ou não está cadastrado ainda.\n")


def viajemAtiva():
    ler()
    counter = 0
    for a in get_bvia().values():
        if a['Status']:
            counter += 1
    if counter != 0:
        print('Segue abaixo lista de viajens ativas: \n')
        print(f"{'Veículo':<16} {'Destino':<18} {'Status':<14} {'Período'}")
        for a in get_bvia().values():
            if a['Status']:
                print(f"{a['Veiculo']:<16} {a['Destino']:<18} {'Ativo':<14} {a['Periodo']}")
        print()
    else:
        print("Não existem viagens ativas nesse momento.")
    input('Pressione enter para voltar ao menu. ')



def veiculoEmViajem():
    ler()
    print('Segue abaixo lista de veiculos em viajem:')
    for a in get_bvia().values():  # tentar colocar o tipo do veiculo junto
        if a['Status']:
            print(a['Veiculo'])
    input('Pressione enter para voltar ao menu. ')


def veiculoDisponivel():
    ler()
    print('Segue abaixo lista de veiculos dispobiveis para Viajem: ')
    for a in get_bvia().values():  # tentar colocar o tipo do veiculo junto
        if not a['Status']:
            print(a['Veiculo'])
    input('Pressione enter para voltar ao menu. ')


def todasAsViagens():
    ler()
    for a in get_bvia().items():
        print(a)
    input('Pressione enter para voltar ao menu. ')


def viagemPorPeriodo():
    print('Viajens por periodo.\n')
    print('=-=-Periodo inicial=-=-')
    di = int(input('Dia inicial: '))
    mi = int(input('Mês inicial: '))
    print()
    print('=-=-Periodo final=-=-')
    df = int(input("Dia final: "))
    mf = int(input("Mês final: "))


def dia(a, i=0):
    if i == 1:
        if a < diaInicio:
            print("O dia do fim da viagem não pode ser menor que o dia de início.")
            criarViajem()
    if 1 > a < 31:
        print('Valor incorreto.')
        criarViajem()


def mes(b, i=0):
    if i == 1:
        if b < mesInicio:
            print("O mês do fim da viagem não pode ser menor que o mês do início.")
    if 1 > b < 12:
        print('Valor incorreto')
        criarViajem()

