from menu import *
from controladorMotorista import *
from controladorVeiculo import *
from controladorViagem import *


def mainMotorista():
    while True:
        opcaomenu = menuMotorista()
        print()
        if opcaomenu == 1:
            cadastro_Motorista()
        elif opcaomenu == 2:
            buscarMotorista()
        elif opcaomenu == 3:
            editarMotorista()
        elif opcaomenu == 4:
            removerMotorista()
        elif opcaomenu == 5:
            listarMotoristasCNH()
        elif opcaomenu == 6:
            listarMotoristas()
        elif opcaomenu == 7:
            break
        else:
            print("Opção incorreta. Digite Novamente")


def mainVeiculo():
    while True:
        opcaomenu = menuVeiculo()
        print()
        if opcaomenu == 1:
            cadastrarVeiculo()
        elif opcaomenu == 2:
            buscarVeiculo()
        elif opcaomenu == 3:
            addMotoristaVeic()
        elif opcaomenu == 4:
            removerMotoristaVeic()
        elif opcaomenu == 5:
            listarVeicCMotorista()
        elif opcaomenu == 6:
            listarVeicSMotorista()
        elif opcaomenu == 7:
            removerVeiculo()
        elif opcaomenu == 8:
            break
        else:
            print("Opção incorreta. Digite Novamente")


def mainViagem():
    while True:
        opcaomenu = menuViagem()
        print()
        if opcaomenu == 1:
            criarViajem()
        elif opcaomenu == 2:
            fimViajem()
        elif opcaomenu == 3:
            viajemAtiva()
        elif opcaomenu == 4:
            veiculoEmViajem()
        elif opcaomenu == 5:
            veiculoDisponivel()
        elif opcaomenu == 6:
            todasAsViagens()
        elif opcaomenu == 7:
            pass
        elif opcaomenu == 8:
            break
        else:
            print("Opção incorreta. Digite Novamente")


def main():
    while True:
        opcaomenu = menuPrincipal()
        print()
        if opcaomenu == 1:
            mainMotorista()
        elif opcaomenu == 2:
            mainVeiculo()
        elif opcaomenu == 3:
            mainViagem()
        elif opcaomenu == 4:
            print("Finalizando...")
            break
        else:
            print("Opção incorreta. Digite Novamente")


main()
