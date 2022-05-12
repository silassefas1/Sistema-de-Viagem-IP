from controladorVeiculo import *
# =-=-=-=-=-=-=-=-=-=-=-=-=-Funções Fundamentais -=-=-==-=-==-=--==-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-


def checagem(item, codigo=0):  # 0 é motorista, 1 é veículo. Função de checagem
    if codigo == 0:  # motorista
        if item in getBancoMotorista():
            return True   # Se o CPF já existir ele retorna True
        else:
            return False  # Se não existir ele retorna False
    elif codigo == 1:  # veículo
        if item in getBancoVeiculo():  # Se o veículo já existir ele retorna True
            return False
        else:  # Se não existir ele retorna False
            return True




def continuar():  #Função para a opção de continuar
    while True:
        opcao = str(input("Deseja continuar [S/N]? ")).strip().upper()
        while opcao not in "SN":
            opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
        print()
        if opcao == "S":
            return True  # se a opcao for S, ele retorna True
        else:  # se a opcao for N, ele retorna False
            return False