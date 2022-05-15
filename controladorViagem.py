from funcoes import *
from controladorVeiculo import *
from bancoGeral import *

# aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções.
# ========================================= Viajem ===================================================================

placa= None

def cadastro_Viajem():
    while True:    # cadastro Veiculo
        print('Cadastro Viajem')
        print('Selecione um veiculo para a viajem:')
        # mostrar todos os veiculos do banco
        for i in banco_Veiculo:
            print(i)
        # armazenar o veiculo selecionado pela placa
        selecao_Veiculo=input('Insira a placa do veiculo para a viajem: ').upper()
        veiculo = selecao_Veiculo
        if not selecao_Veiculo in banco_Veiculo:
            print('Veiculo não cadastrado.')
            novamente = int(input('1 para cadastra um veiculo \n '
                                  '2 para tentar novamente.'))
            if novamente == 1:
                cadastrarVeiculo()
            elif novamente == 2:
                cadastro_Viajem()
        # cadastro rota
        inicio_Rota=input('Digite o local de saida: ')
        fim_Rota=input('Digite o destino final da viagem: ')
        rota = 'Viajem de '+ inicio_Rota + ' para ' + fim_Rota+'.'
        # Data da viajem
        print('Cadastra datas da viajem')
        inicio_Data=input('Digite a data de inicio: ')
        fim_Data=input('Digite a data de fim: ')
        periodo = inicio_Data + ' até '+ fim_Data
        # atribuir status
        print('Viajem iniciada.')
        status = True
        print('Viajem cadastrada.')
        viagem = {veiculo:{'Veiculo': veiculo, 'Rota': rota, 'Periodo': periodo, 'Status': status}}
        banco_Viajem[veiculo]=viagem
        novo_cadastro = int(input('Deseja fazer um novo cadastro? \n'
                                  '1 - Sim\n'
                                  '2 - Não\n'))

        if novo_cadastro == 1:
            return banco_Viajem
            cadastro_Viajem()
        else:
            print('Pressione enter para voltar ao menu...')
            input()
        break


def finalizar_Viajem():
    for veiculo in banco_Viajem.values():
        print(veiculo)
    viajem_Fim=input('Qual viajem você quer finalizar? ') # colocar verificação se a viajem existe
    opcao_Fim = int(input(f'Tem certeza que quer finalizar a viajem {viajem_Fim} ? \n'
                          f'1 - Sim\n'
                          f'2 - Não\n'))
    if opcao_Fim == 1:
        viajem_status={}
        viajem_status.get(banco_Viajem.items(viajem_Fim))
        print(viajem_status)


def listar_Viajem():
    for viajem in banco_Viajem.values():
        print(viajem)

