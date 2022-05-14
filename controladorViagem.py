from funcoes import *
# aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções e os dicionários.
from controladorVeiculo import *
# ========================================= Viajem ===================================================================
banco_Viajem={}


def cadastro_Viajem():
    while True:    # cadastro Veiculo
        print('Cadastro Viajem')
        print('Selecione um veiculo para a viajem:')
        # mostrar todos os veiculos do banco
        for i in banco_Veiculo:
            print(i)
        # armazenar o veiculo selecionado pela placa
        selecao_Veiculo=input('Insira a placa do veiculo para a viajem: ').upper()
        placa = selecao_Veiculo
        veiculo = selecao_Veiculo in banco_Veiculo
        if not selecao_Veiculo in banco_Veiculo:
            print('Veiculo não cadastrado.')
            novamente = int(input('1 para cadastrar um veículo. \n '
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
        print('Cadastrar datas da viajem')
        inicio_Data=input('Digite a data de inicio: ')
        fim_Data=input('Digite a data de fim: ')
        periodo = inicio_Data + ' até '+ fim_Data
        # atribuir status
        print('Viajem iniciada.')
        status = True
        print('Viajem cadastrada.')
        viagem = {'Veiculo':veiculo,'Rota':rota,'Periodo':periodo,'status':status}
        banco_Viajem[veiculo]=viagem
        novo_cadastro = int(input('Deseja fazer um novo cadastro? \n'
                                  '1 - Sim\n'
                                  '2 - Não\n'))
        if novo_cadastro == 1:
            cadastro_Viajem()
        else:
            print('Voltando ao menu principal...')
            input()
        break