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


cadastro_Motorista()
print()

# ========================================= Veículo ===================================================================
banco_Veiculo = {}


def cadastrarVeiculo():
    while True:
        print(f'{"Cadastro de Veículos":^40}')
        print('-=' * 20)
        placa = int(input("Insira a placa do seu veículo: "))
        if not checagem(placa, 1):  # coloquei if not. porque ele só vai continuar se ele não existir (Que é False)
            tipo = str(input("Insira o tipo do seu veículo (moto ou carro): ")).lower()
            motorista = None  # O motorista inicialmente deverá ser None e depois que deverá referenciar com o motorista do bdMotoristas
            veiculo = {placa, tipo, motorista}
            banco_Veiculo[placa] = veiculo
        else:
            print("Este veículo já está cadastrado.")
        if not continuar():
            return
        print()


def buscarVeiculo():
    while True:
        print(f"{'Buscar Veículo':^40}")
        print('-=' * 20)
        
