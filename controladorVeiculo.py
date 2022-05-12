from controladorMotorista import *

# ========================================= Veículo ===================================================================


def getBancoVeiculo():
    banco_Veiculo = {'2HBR220': {'placa': "2HBR220", 'tipo': "Carro", "motorista": 'João'},
                 "2HBTR78": {'placa': "2HBTR78", "tipo": "Moto", "motorista": None}}
    return banco_Veiculo


def cadastrarVeiculo():
    while True:
        print(f'{"Cadastro de Veículos":^40}')
        print('-=' * 20)
        placa = str(input("Insira a placa do seu veículo (ex: 2H6BR22): ")).upper()
        while len(placa) != 7 or not placa.isalnum():
            print("informação incorreta.")
            placa = str(input("Insira a placa do seu veículo com 7 caracteres(ex: 2H6BR22) "
                              "e somente letras e números: ")).strip().upper()
        if checagem(placa, 1):  # coloquei if not. porque ele só vai continuar se ele não existir (Que é False)
            tipo = str(input("Insira o tipo do seu veículo (moto ou carro): ")).strip().title()
            while tipo != "Moto" and tipo != "Carro":
                tipo = str(input("Infomação incorreta. Digite somente moto ou carro: ")).strip().title()
            veiculo = {"placa": placa, "tipo": tipo, "motorista": None}
            getBancoVeiculo()[placa] = veiculo
        else:
            print("Este veículo já está cadastrado.")
        if not continuar():
            return
        print()


def buscarVeiculo():
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    while True:
        print(f"{'Buscar Veículo':^40}")
        print('-=' * 20)
        placa = str(input("Insira a placa do seu veículo: ")).strip().upper()
        if placa in getBancoVeiculo():
            for veiculo in getBancoVeiculo().values():
                if veiculo.get("placa") == placa:
                    if veiculo.get("Motorista") is not None:
                        print('-=' * 20)
                        print(f'{"Placa":<15}{"Tipo":11}{"Motorista"}')
                        print(f"{veiculo.get('placa'):<15}{veiculo.get('tipo'):11}{veiculo.get('motorista')}")
                        print("-=" * 20)
                        print()
                    else:
                        print('-=' * 20)
                        print(f'{"Placa":<15}{"Tipo":}')
                        print(f"{veiculo.get('placa'):<15}{veiculo.get('tipo'):6}")
                        print("-=" * 20)
                        print()
        else:
            print(f"O veículo com a placa {placa} não está cadastrado.")
        if not continuar():
            return
        print()


def addMotoristaVeic():
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        while True:
            print("=-=-=-Adicionar Motorista=-=-=-")
            while True:
                placa = str(input("Digite a placa do veículo desejado: ")).strip().upper()
                existe = False
                for veiculo in getBancoVeiculo().keys():
                    if placa == veiculo:
                        existe = True
                if not existe:
                    print(f"Esse Veículo não existe. Tente novamente.\n")
                else:
                    break
            nome = str(input("Digite o nome do motorista que você deseja adicionar ao veículo: ")).title()
            nMotorista = False
            for veiculo in getBancoVeiculo().values():
                if veiculo.get("placa") == placa and nome == veiculo.get("motorista"):
                    print(f"O motorista {nome} já está vinculado a este veículo.\n")
                    nMotorista = True
            if not nMotorista:
                # Depois # verificar se a carteira dele é correspondente ao veículo. A - Carro, B - Moto, A/B Carro e Moto
                nMotorista = False
                for cpf in getBancoMotorista().values():
                    if nome == cpf.get("nome"):
                        for veiculo in getBancoVeiculo().values():
                            if placa == veiculo.get("placa"):
                                veiculo["motorista"] = nome
                                nMotorista = True
                if nMotorista:
                    print("Motorista vinculado ao veículo com sucesso!\n")
                else:
                    print("Esse motorista não existe.")
                if not continuar():
                    return
            else:
                if not continuar():
                    return
            # verificar se a carteira dele é correspondente ao veículo. A - Carro, B - Moto, A/B Carro e Moto


def removerMotoristaVeic():
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        print("=-=-=-Remover Motorista do Veículo=-=-=-")
        print('=-'*15)
        nMotoristas = 0
        while True:
            nome = str(input("Digite o nome do motorista que você deseja desvincular do veículo: ")).strip().title()
            for motorista in getBancoVeiculo().values():
                if motorista.get("motorista") == nome:
                    nMotoristas += 1
            if nMotoristas == 0:
                print(f"O motorista {nome} não está vinculado a nenhum veículo ou não existe.\n")
                if not continuar():
                    return
                else:
                    return removerMotoristaVeic()
            else:
                print(f"=-=-=-Veículo(s) de {nome}-=-=-=")
                print(f'{" " * 7}{"Placa":<12}{"Tipo":8}')
                for veiculo in getBancoVeiculo().values():
                    if nome == veiculo.get("motorista"):
                        print(f'{" " * 7}{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}')
                while True:
                    placa = str(input(f"Digite a placa do veículo que deseja desvincular "
                                      f"do motorista {nome}: ")).strip().upper()
                    for veiculo in getBancoVeiculo().values():
                        if veiculo.get("placa") == placa and veiculo.get("motorista") == nome:
                            opcao = str(input("Você tem certeza [S/N]? ")).strip().upper()
                            while opcao not in "SN":
                                opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                            print()
                            if opcao == "N":
                                return
                            else:
                                if veiculo.get('placa') == placa:
                                    veiculo["motorista"] = None
                                    print("Motorista desvinculado com sucesso!\n")
                                    return
                    print("Este veículo não existe. Tente novamente")
                    if not continuar():
                        return


def listarVeicCMotorista():
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        nMotoristas = 0
        for veiculo in getBancoVeiculo().values():
            if veiculo.get("motorista") is not None:
                nMotoristas += 1
        if nMotoristas == 0:
            print("Não existe motorista vinculado ao veículo.\n")
            return
        else:
            print("=-=-=-Veículos Com Motorista-=-=-=")
            print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
            for veiculo in getBancoVeiculo().values():
                if veiculo.get("motorista") is not None:
                    print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
            print('=-' * 17)
            print()


def listarVeicSMotorista():
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    nMotoristas = 0
    for veiculo in getBancoVeiculo().values():
        if veiculo.get("motorista") is None:
            nMotoristas += 1
    if nMotoristas == 0:
        print("Não existe motorista vinculado ao veículo.\n")
        return
    else:
        print("=-=-=-Veículos Sem Motorista-=-=-=")
        print(f'{" " * 9}{"Placa":<12}{"Tipo":8}')
        for veiculo in getBancoVeiculo().values():
            if veiculo.get("motorista") is None:
                print(f'{" " * 9}{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}')
        print('=-' * 17)
        print()


def removerVeiculo():
    print("=-=-=-Remover Veículo-=-=-=")
    if len(getBancoVeiculo()) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        placa = str(input("Digite a placa do veículo que deseja remover do cadastro: ")).strip().upper()
        cadastrado = False
        for veiculo in getBancoVeiculo():
            if placa == veiculo:
                cadastrado = True
        if cadastrado:
            for veiculo in getBancoVeiculo().values():
                if placa == veiculo["placa"]:
                    print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
                    print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
                    opcao = str(input("Você tem certeza [S/N]? ")).strip().upper()
                    while opcao not in "SN":
                        opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                    print()
                    if opcao == "N":
                        return
                    else:
                        del getBancoVeiculo()[placa]
                        print("Veículo removido com sucesso!")
                        return
        else:
            print("Este veículo ainda não está cadastrado.")
            if not continuar():
                return
            else:
                return removerVeiculo()

