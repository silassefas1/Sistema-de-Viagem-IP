from funcoes import *  # aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções.
from controladorVeiculo import *
from bancoGeral import *


# ========================================= Viajem ===================================================================

placa = None
status = None


def criarViajem():
    while True:  # cadastro Veiculo===================================================================================
        print('Cadastro Viajem')
        cont = len(banco_Veiculo)
        for a in banco_Veiculo and bdViajem:
            cont -= 1
        if cont == 0:
            print('Não ha veiculos disponiveis.')
            opcao = int(input('Deseja cadastrar um novo veiculo?\n'
                              '1 - Sim\n'
                              '2 - Não\n '))
            if opcao == 1:
                cadastrarVeiculo()
            else:
                break

        else:
            # mostrar todos os veiculos do banco==========================================================================
            print('Selecione um veiculo para a viajem:')
            for veiculo in banco_Veiculo:
                if not veiculo in bdViajem:
                    print(veiculo)

            selecao_Veiculo = input('Insira a placa do veiculo para a viajem: ').upper()
            placa = selecao_Veiculo
            if not selecao_Veiculo in banco_Veiculo:
                print('Veiculo não cadastrado.')
                novamente = int(input('1 Cadastra um veiculo \n '
                                      '2 Tentar novamente.'))
                if novamente == 1:
                    cadastrarVeiculo()
                elif novamente == 2:
                    criarViajem()
            # cadastro rota===================================================================================
            print('Cadastro de Rota')
            rota = str(input('Digite o destino: '))

            # Data da viajem===================================================================================
            print('Cadastra datas da viajem')
            inicio_Data = float(input('Digite a data de inicio: na forma DD.MM ')) #formatar para o tipo data
            fim_Data = float(input('Digite a data de fim: na forma DD.MM '))
            periodo = f"{inicio_Data} até {fim_Data}"
            # atribuir status===================================================================================
            print('Viajem iniciada.')
            status = True
            # alimentar dicionario===================================================================================
            viagem = {'Veiculo': f"{placa}", 'Destino': f"{rota}", 'Status': status, 'Periodo':f"{inicio_Data} ate {fim_Data}"}
            bdViajem[placa] = viagem
            print(bdViajem)
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
    print('Qual Viajem você deseja finalizar: ')
    for a in bdViajem:
        print(a)
    placa = input('Digite a placa do veiculo em viajem: ')
    for a in bdViajem.values():
        if placa == a['Veiculo']:
            a['Status'] = False
    print('Viajem Finalizada com sucesso.')
    input('Presione enter para voltar ao menu.')


def viajemAtiva():
    print('Segue abaixo lista de viajens ativas: \n')
    for a in bdViajem.values():
        if a['Status']:
            print(a)
    input('Pressione enter para voltar ao menu. ')


def veiculoEmViajem(): # colocar aviso de sem veiculos em viajem
    print('Segue abaixo lista de veiculos em viajem: ')
    for b in bdViajem.values():  # tentar colocar o tipo do veiculo junto
        if b['Status']:
            print(b['Veiculo'])
    input('Pressione enter para voltar ao menu. ')


def veiculoDisponivel(): # colocar aviso de sem veiculos disponiveis
    print('Abaixo lista de veiculos disponiveis para viajem. ')
    for a in banco_Veiculo.values():
        b = a['placa']
        if not b in bdViajem.keys():
            print(banco_Veiculo.get('tipo'), b)

    input()


def todasAsViagens(): # mostar todas as viajens ================================================================
    for a in bdViajem.items():
        print(a)
    input('Pressione enter para voltar ao menu. ')


def vigemPorPeriodo():
    print(' Viajens por periodo.')
    periodoInicio = float(input('inicio: '))
    periodoFim = float(input('fim: '))
    for a in bdViajem.values():
        if a in bdViajem['Periodo'] >= periodoInicio and bdViajem['Periodo'] <= periodoFim:
            print(a)