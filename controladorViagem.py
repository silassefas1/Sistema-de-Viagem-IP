from funcoes import *  # aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções.
# ========================================= Viajem ===================================================================
#banco_Viajem={veiculo,rota,status[iniciada/finalizada],data[i/f]}


def cadastro_Viajem():
    while True:
        print('Cadastro Viajem')
        print('Selecione um veiculo para a viajem:')
        for i in banco_Veiculo: #mostrar todos os veiculos do banco
            print(i)
        veiculo=input('Insira a placa do veiculo para a viajem: ') # armazenar o veiculo selecionado pela placa
        print('Cadastro de rota')
        if veiculo in banco_Veiculo:
            return True
        else:
            print('Veiculo não cadastrado.')
            cadastro_Viajem()

        inicio=input('Digite o local de saida: ') # armazenar os valores de inicio e fim da viajem
        fim=input('Digite o destino final da viagem: ')
        rota ='Viajem de '+ inicio + ' para ' + fim+'.'
        status = True