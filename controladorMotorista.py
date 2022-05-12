from funcoes import *
# =================================================== Motorista =====================================================
def getBancoMotorista():
    banco_Motorista = {44555888990: {"CPF": 44555888990, "nome": "João", "habilitacao": "AB"},
                   22366895108: {"CPF": 22366895108, "nome": "Paulo", "habilitacao": "B"}}
    return banco_Motorista


def cadastro_Motorista():
    print("=-=-Cadastro do Motorista=-=-=-")
    print("=-" * 15)
    while True:
        cpf = input("Insira um CPF com 11 dígitos: ").strip()
        while not cpf.isdigit() or len(cpf) != 11:
            cpf = input("Informação incorreta. Digite somente números ou um CPF válido (com 11 dígitos): ").strip()
        cpf = int(cpf)
        if not checagem(cpf):
            nome = str(input("Insira o nome do funcionario: "))
            while not nome.isalpha():
                nome = input("Informação incorreta. Insira somente letras: ")
            habilitacao = str(input(f"Insira a carteira de habilitação de {nome} (A, B ou AB): "))
            while habilitacao not in "ABab":
                habilitacao = str(input(f"Informação incorreta. Digite somente uma carteira A, B ou AB: "))
            dic_Motorista = {"CPF": cpf, "nome": nome.strip().title(), "habilitacao": habilitacao.strip().upper()}
            banco_Motorista[cpf] = dic_Motorista
            if not continuar():
                return
            print("=-" * 15)
        else:
            for pessoa, motorista in banco_Motorista.items():
                print(motorista)
                if pessoa == cpf:
                    print(f'O CPF {cpf} pertence ao motorista {motorista.get("nome")} e já está cadastrado.')
                    break
            if not continuar():
                return
            return cadastro_Motorista()


def buscarMotorista():
    pass


