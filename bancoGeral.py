from json import dump, load
from os import path

counter_bm = counter_bv = counter_bvia = True


def get_bm():
    # banco motorista
    global counter_bm, banco_Motorista
    if counter_bm:
        banco_Motorista = {44555888990: {"CPF": 44555888990, "nome": "João", "habilitacao": "AB"}}
        counter_bm = False
        return banco_Motorista
    else:
        return banco_Motorista


def get_bv():
    # banco veículos
    global counter_bv, banco_Veiculo
    if counter_bv:
        banco_Veiculo = {'2HBR220': {'placa': "2HBR220", 'tipo': "Carro", "motorista": 'João'},
                         "2HBTR78": {'placa': "2HBTR78", "tipo": "Moto", "motorista": None},
                         "2HBTR56": {'placa': "2HBTR56", "tipo": "Carro", "motorista": None}}
        counter_bv = False
    return banco_Veiculo


def get_bvia():
    # banco viajem
    global counter_bvia, bdViajem
    if counter_bvia:
        bdViajem = {'2HBR220': {'Veiculo': "2HBR220",'Destino':"Recife",'Status':True,'Periodo':"15.05 até 16.05"},
                    '2HBTR78': {'Veiculo': "2HBTR78",'Destino':"Recife",'Status':False,'Periodo':"15.05 até 16.05"}}
        counter_bvia = False
    return bdViajem


def get_bg():
    # banco geral
    bm = get_bm()
    bv = get_bv()
    bdViajem = get_bvia()
    banco_geral = {"banco_motorista": bm, "banco_veiculo": bv, "banco_viajem": bdViajem}
    return banco_geral


# ==============================Funções JSON====================================================================


def criar():
    # cria o JSON
    global banco_geral
    banco_geral = get_bg()
    if not path.exists("bdGeral.json"):
        with open("bdGeral.json", 'w') as f:
            dump(banco_geral, f, indent=4)


def escrever():
    # Escreve no JSON
    with open("bdGeral.json", 'w') as f:
        banco_geral = get_bg()
        dump(banco_geral, f, indent=4)


def ler():
    # Lê o JSON
    with open("bdGeral.json", 'r+') as f:
        global banco_geral, banco_Motorista, banco_Veiculo, bdViajem
        banco_geral = load(f)
        banco_Motorista = banco_geral["banco_motorista"]
        banco_Veiculo = banco_geral["banco_veiculo"]
        bdViajem = banco_geral["banco_viajem"]
