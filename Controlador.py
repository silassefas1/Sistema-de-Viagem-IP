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
banco_Motorista={}


def cadastro_Motorista():
    while True:
        dic_Motorista={}
        cpf=input("insira um CPF: ")
        #criar uma função que verifique se o cpf ja existe
        nome=input("Insira o nome do funcionario: ")
        habilitacao=input("Insira a carteira de habilitação: ")
        dic_Motorista ={cpf,nome,habilitacao}
        opcao= input("Deseja continuar")
        if opcao != 1:
            break
    return dic_Motorista


print()

# ========================================= Veículo ===================================================================
banco_Veiculo = {'2HBR220': {'placa': "2HBR220", 'tipo': "Carro"},
                 "2HBTR78": {'placa': "2HBTR78", "tipo": "Moto"}}


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
            veiculo = {"placa": placa, "tipo": tipo}
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


def addMotorista():
    if len(banco_Veiculo) == 0:
        print("Ainda não existe nenhum veículo cadastrado.\n")
        return
    else:
        print("=-=-=-Adicionar Motorista=-=-=-")
        print('=-'*15)
        cont = 1
        print(f'{"Opção":<10}{"Placa":<12}Tipo')
        for veiculo in banco_Veiculo.values():
            print(f' [{cont}]      {veiculo.get("placa"):<12}{veiculo.get("tipo")}')
            cont += 1
        while True:
            opcao = int(input("Digite a opção: "))
            if 1 < opcao > len(banco_Veiculo):
                print(f"Opção incorreta. Digite somente a opção de 1 a {len(banco_Veiculo)}.\n")
            else:
                break
        motorista = str(input("Digite o nome do motorista que você deseja adicionar ao veículo: "))
