from menu import *
from Controlador import *


def mainMotorista():
    while True:
        opcaomenu = menuMotorista()
        print()
        if opcaomenu == 1:
            cadastro_Motorista()
        elif opcaomenu == 2:
            pass
        elif opcaomenu == 3:
            pass
        elif opcaomenu == 4:
            pass
        elif opcaomenu == 5:
            pass
        elif opcaomenu == 6:
            pass
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
            pass
        elif opcaomenu == 2:
            pass
        elif opcaomenu == 3:
            pass
        elif opcaomenu == 4:
            pass
        elif opcaomenu == 5:
            pass
        elif opcaomenu == 6:
            pass
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
