from json import dump, load
from os import path

counter_bm = counter_bv = counter_bg = True


def get_bm():
    global counter_bm, banco_Motorista
    if counter_bm:
        banco_Motorista = {}
        counter_bm = False
        return banco_Motorista
    else:
        return banco_Motorista



def get_bv():
    global counter_bv, banco_Veiculo
    if counter_bv:
        banco_Veiculo = {}
        counter_bv = False
    return banco_Veiculo


def get_bg():
    bm = get_bm()
    bv = get_bv()
    banco_geral = {"banco_motorista": bm, "banco_veiculo": bv}
    return banco_geral


# ==============================Funções JSON====================================================================


def criar():
    global banco_geral
    banco_geral = {}
    if not path.exists("bdGeral.json"):
        with open("bdGeral.json", 'w') as f:
            dump(banco_geral, f, indent=4)


def escrever():
    with open("bdGeral.json", 'w') as f:
        banco_geral = get_bg()
        dump(banco_geral, f, indent=4)


def ler():
    with open("bdGeral.json", 'r+') as f:
        global banco_geral, banco_Motorista, banco_Veiculo
        banco_geral = load(f)
        banco_Motorista = banco_geral["banco_motorista"]
        banco_Veiculo = banco_geral["banco_veiculo"]

banco_Motorista = {44555888990: {"CPF": 44555888990, "nome": "João", "habilitacao": "AB"}}
"""22366895108: {"CPF": 22366895108, "nome": "Paulo", "habilitacao": "B"},
22366895109: {"CPF": 22366895109, "nome": "Paulo", "habilitacao": "B"}}"""
banco_Veiculo = {'2HBR220': {'placa': "2HBR220", 'tipo': "Carro", "motorista": 'João'},
                 "2HBTR78": {'placa': "2HBTR78", "tipo": "Moto", "motorista": None}}
bdViajem = {'2HBR220': {'Veiculo': '2HBR220', 'Destino': 'Serra', 'Status': True, 'Periodo': {'inicio': {(10, 5)}, 'fim': {(20, 6)}}}}

