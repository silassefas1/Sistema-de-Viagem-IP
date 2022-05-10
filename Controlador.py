# =-=-=-=-=-=-=-=-=-=-=-=-=-Funções Fundamentais -=-=-==-=-==-=--==-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-


def checagem(item, codigo=0):  # 0 é motorista, 1 é veículo. Função de checagem
    if codigo == 0:  # motorista
        if item in banco_Motorista:
            return True   # Se o CPF já existir ele retorna True
        else:
            return False  # Se não existir ele retorna False
    elif codigo == 1:  # veículo
        if item in banco_Veiculo:  # Se o veículo já existir ele retorna True
            return True
        else:  # Se não existir ele retorna False
            return False


def continuar():  #Função para a opção de continuar
    while True:
        opcao = str(input("Deseja continuar [S/N]? ")).upper()
        while opcao not in "SN":
            opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).upper()
        if opcao == "S":
            return True  # se a opcao for S, ele retorna True
        else:  # se a opcao for N, ele retorna False
            return False


# =================================================== Motorista =====================================================
banco_Motorista={44555888990: {"CPF": 44555888990, "nome": "João", "habilitacao": "AB"}}


def cadastro_Motorista():
    while True:
        cpf=input("insira um CPF: ")
        #criar uma função que verifique se o cpf ja existe
        nome=input("Insira o nome do funcionario: ").title()
        habilitacao=input("Insira a carteira de habilitação: ")
        dic_Motorista ={"CPF": cpf,"nome": nome, "hablitacao": habilitacao}
        banco_Motorista[cpf] = dic_Motorista
        opcao= input("Deseja continuar")
        if opcao != 1:
            return


print()

# ========================================= Veículo ===================================================================
banco_Veiculo = {'2HBR220': {'placa': "2HBR220", 'tipo': "Carro", "motorista": None},
                 "2HBTR78": {'placa': "2HBTR78", "tipo": "Moto", "motorista": None}}


def cadastrarVeiculo():
    while True:
        print(f'{"Cadastro de Veículos":^40}')
        print('-=' * 20)
        placa = str(input("Insira a placa do seu veículo (ex: 2H6BR22): ")).upper()
        while len(placa) != 7 or not placa.isalnum():
            print("informação incorreta.")
            placa = str(input("Insira a placa do seu veículo com 7 caracteres(ex: 2H6BR22) "
                              "e somente letras e números: ")).strip().upper()
            if placa.isalnum() and len(placa) == 7:
                break
        if not checagem(placa, 1):  # coloquei if not. porque ele só vai continuar se ele não existir (Que é False)
            tipo = str(input("Insira o tipo do seu veículo (moto ou carro): ")).strip().title()
            while tipo != "Moto" and tipo != "Carro":
                tipo = str(input("Infomação incorreta. Digite somente moto ou carro: ")).strip().title()
                if tipo == "Moto" or tipo == 'Carro':
                    break
            veiculo = {"placa": placa, "tipo": tipo, "motorista":None}
            banco_Veiculo[placa] = veiculo
        else:
            print("Este veículo já está cadastrado.")
        if not continuar():
            return
        print()


def buscarVeiculo():
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    while True:
        print(f"{'Buscar Veículo':^40}")
        print('-=' * 20)
        placa = str(input("Insira a placa do seu veículo: ")).strip().upper()
        if placa in banco_Veiculo:
            for veiculo in banco_Veiculo.values():
                if veiculo.get("placa") == placa:
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
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        while True:
            print("=-=-=-Adicionar Motorista=-=-=-")
            while True:
                placa = str(input("Digite a placa do veículo desejado: ")).strip().upper()
                existe = False
                for veiculo in banco_Veiculo.keys():
                    if placa == veiculo:
                        existe = True
                if not existe:
                    print(f"Esse Veículo não existe. Tente novamente.\n")
                else:
                    break
            nome = str(input("Digite o nome do motorista que você deseja adicionar ao veículo: ")).title()
            exite = False
            for cpf in banco_Motorista.values():
                if nome == cpf.get("nome"):
                    for veiculo in banco_Veiculo.values():
                        if placa == veiculo.get("placa"):
                            veiculo["motorista"] = nome
                    print("Motorista vinculado ao veículo com sucesso!\n")
                    if not continuar():
                        return
                    addMotoristaVeic()
            # verificar se a carteira dele é correspondente ao veículo. A - Carro, B - Moto, A/B Carro e Moto
            print("Esse motorista não existe.")
            if not continuar():
                return


def removerMotoristaVeic():
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        print("=-=-=-Remover Motorista do Veículo=-=-=-")
        print('=-'*15)
        nMotoristas = 0
        while True:
            nome = str(input("Digite o nome do motorista que você deseja desvincular do veículo: ")).title()
            for motorista in banco_Veiculo.values():
                if motorista.get("motorista") == nome:
                    nMotoristas += 1
            if nMotoristas == 0:
                print(f"O motorista {nome} não está vinculado a nenhum veículo.\n")
                return
            else:
                for veiculo in banco_Veiculo.values():
                    if nome == veiculo.get("motorista"):
                        print(f"=-=-=-Veículo(s) de {nome}-=-=-=")
                        print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
                        print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
                while True:
                    placa = str(input(f"Digite a placa do veículo que deseja desvincular "
                                      f"do motorista {nome}: ")).strip().upper()
                    for veiculo in banco_Veiculo.values():
                        if veiculo.get("placa") == placa and veiculo.get("motorista") == nome:
                            opcao = str(input("Tem certeza [S/N]? ")).upper()
                            while opcao not in "SN":
                                opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).upper()
                            if opcao == "S":
                                for veiculo in banco_Veiculo.values():
                                   if veiculo.get('placa') == placa:
                                       veiculo["motorista"] = None
                                print("Motorista desvinculado com sucesso!\n")
                                return
                        else:
                            print("Este veículo não existe. Tente novamente")
                if not continuar():
                    return


def listarVeicCMotorista():
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        nMotoristas = 0
        for veiculo in banco_Veiculo.values():
            if veiculo.get("motorista") is not None:
                nMotoristas += 1
        if nMotoristas == 0:
            print("Não existe motorista vinculado ao veículo.\n")
            return
        else:
            print("=-=-=-Veículos Com Motorista-=-=-=")
            print(f'{"Placa":<12}{"Tipo":8}{"Motorista"}')
            for veiculo in banco_Veiculo.values():
                if veiculo.get("motorista") is not None:
                    print(f'{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}{veiculo.get("motorista")}')
            print('=-' * 17)
            print()


def listarVeicSMotorista():
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        print("=-=-=-Veículos Sem Motorista-=-=-=")
        print(f'{" " * 9}{"Placa":<12}{"Tipo":8}')
        for veiculo in banco_Veiculo.values():
            if veiculo.get("motorista") is None:
                print(f'{" " * 9}{veiculo.get("placa"):<12}{veiculo.get("tipo"):8}')
        print('=-' * 17)
        print()
