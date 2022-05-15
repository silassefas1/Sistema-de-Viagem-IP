from funcoes import *
from controladorVeiculo import *
from bancoGeral import *


# aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções.
# ========================================= Viajem ===================================================================
bdViajem = {'2HBR220': {'Veiculo': "2HBR220",'Destino':"Recife",'Status':True,'Periodo':"15/05 ate 16/05"}
            }
placa = None
status = None

def criarViajem():
    while True:    # cadastro Veiculo===================================================================================
        print('Cadastro Viajem')
        print('Selecione um veiculo para a viajem:')
        # mostrar todos os veiculos do banco==========================================================================
        for veiculo in banco_Veiculo:
            if not veiculo in bdViajem:
                print(veiculo)

        selecao_Veiculo=input('Insira a placa do veiculo para a viajem: ').upper()
        placa = selecao_Veiculo
        if not selecao_Veiculo in banco_Veiculo:
            print('Veiculo não cadastrado.')
            novamente = int(input('1 Cadastra um veiculo \n '
                                  '2 Tentar novamente.'))
            if novamente == 1:
                cadastrarVeiculo()
            elif novamente == 2:
                cadastro_Viajem()
        # cadastro rota===================================================================================
        print('Cadastro de Rota')
        rota = str(input('Digite o destino: '))

        # Data da viajem===================================================================================
        print('Cadastra datas da viajem')
        inicio_Data=input('Digite a data de inicio: ')
        fim_Data=input('Digite a data de fim: ')
        periodo = f"{inicio_Data} até {fim_Data}"
        # atribuir status===================================================================================
        print('Viajem iniciada.')
        status = "True"
        # alimentar dicionario===================================================================================
        viagem = {placa: {'Veiculo': f"{placa}",'Destino':f"{rota}",'Status':f"{status}",'Periodo':f"{periodo}"}}
        bdViajem[placa] = viagem

        print('Viajem cadastrada.')

        # Nova Viajem===================================================================================
        novo_cadastro = int(input('Deseja fazer um novo cadastro? \n'
                                  '1 - Sim\n'
                                  '2 - Não\n'))

        if novo_cadastro == 1:
            return bdViajem
            cadastro_Viajem()
        else:
            print('Pressione enter para voltar ao menu...')
            input()
        break

def fimViajem():

    for a in bdViajem:
        print(a)
    placa = input()
    print(bdViajem[placa])
    for a in bdViajem.values():
        if placa == a['Veiculo']:
            a['Status'] = False
    print(bdViajem[placa])

def listarViagem():
    for a in bdViajem.items():
        print(a)
        input('Enter para voltar ao menu')