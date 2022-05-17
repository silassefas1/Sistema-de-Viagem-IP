from funcoes import continuar, checagem
from bancoGeral import ler, escrever, get_bm
# aqui ele já está importando o banco Geral porque no arquivo funções ele já está importando
# e eu estou importando as funções.
# =================================================== Motorista =====================================================


def cadastro_Motorista():
    ler()
    print("=-=-Cadastro do Motorista=-=-=-")
    print("=-" * 15)
    while True:
        cpf = input("Insira um CPF com 11 dígitos: ").strip()
        while not cpf.isdigit() or len(cpf) != 11:
            cpf = input("Informação incorreta. Digite somente números ou um CPF válido (com 11 dígitos): ").strip()
        if not checagem(cpf):
            nome = str(input("Insira o nome do motorista: ")).strip().title()
            while not nome.isalpha():
                nome = input("Informação incorreta. Insira somente letras: ").strip().title()
            habilitacao = str(input(f"Insira a carteira de habilitação de {nome} (A, B ou AB): "))
            while habilitacao not in "ABab":
                habilitacao = str(input(f"Informação incorreta. Digite somente uma carteira A, B ou AB: "))
            motorista = {"CPF": cpf, "nome": nome, "habilitacao": habilitacao.strip().upper()}
            get_bm()[cpf] = motorista
            escrever()
            print(f"Motorista {nome} cadastrado com sucesso!")
            if not continuar():
                return
            print("=-" * 15)
        else:
            for pessoa, motorista in get_bm().items():
                if pessoa == cpf:
                    print(f'O CPF {cpf} pertence ao motorista {motorista.get("nome")} e já está cadastrado.')
                    break
            if not continuar():
                return
            cadastro_Motorista()


def buscarMotorista():
    ler()
    if len(get_bm()) == 0:
        print("Ainda não existe nenhum motorista cadastrado.")
        return
    else:
        while True:
            print('-=-=-=-=Buscar Motorista-=-=-=-=')
            cpf = input("Insira um CPF com 11 dígitos do motorista que você deseja busca: ").strip()
            while not cpf.isdigit() or len(cpf) != 11:
                cpf = input("Informação incorreta. Digite somente números ou um CPF válido (com 11 dígitos): ").strip()
            if cpf in get_bm():
                for motorista in get_bm().values():
                    if motorista.get("CPF") == cpf:
                        print('-=' * 25)
                        print(f'{"CPF":<18}{"Nome":10}{"Habilitação"}')
                        print(f"{motorista.get('CPF'):<18}{motorista.get('nome'):<10}{motorista.get('habilitacao')}")
                        print("-=" * 25)
                        print()
            else:
                print(f"O CPF {cpf} não está cadastrado.")
            if not continuar():
                return
            print()


def editarMotorista():
    ler()
    if len(get_bm()) == 0:
        print("Ainda não existe nenhum motorista cadastrado.")
        return
    else:
        while True:
            print('-=-=-=-=Editar Motorista-=-=-=-=')
            cpf = input("Insira um CPF com 11 dígitos do motorista que você deseja editar: ").strip()
            while not cpf.isdigit() or len(cpf) != 11:
                cpf = input("Informação incorreta. Digite somente números ou um CPF válido (com 11 dígitos): ").strip()
            if cpf in get_bm():     # Saber se o motorista existe ou não
                for motorista in get_bm().values():
                    if cpf == motorista.get('CPF'):
                        print('=-'*15)
                        print(f"Nome: {motorista.get('nome')}\nCarteira de Habilitação: {motorista.get('habilitacao')}")
                        print('=-' * 15)
                        while True:
                            newNome = str(input("Insira o novo nome do motorista: ")).strip().title()
                            while not newNome.isalpha():
                                newNome = input("Informação incorreta. Insira somente letras: ").strip().title()
                            habilitacao = str(input(f"Insira a nova carteira de habilitação de {newNome} (A, B ou AB): "))
                            while habilitacao not in "ABab":
                                habilitacao = str(input(f"Informação incorreta. Digite somente uma carteira A, B ou AB: "))
                            motorista = {"CPF": cpf, "nome": newNome, "habilitacao": habilitacao.strip().upper()}
                            print('=-' * 15)
                            print(f"Novas Informações:\nNome: {newNome}\nCarteira de Habilitação: {habilitacao.upper()}")
                            print('=-' * 15)
                            opcao = str(input("Tem certeza que deseja editar [S/N]? ")).strip().upper()
                            while opcao not in "SN":
                                opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                            if opcao == "S":
                                get_bm()[cpf] = motorista
                                escrever()
                                print("Motorista editado com sucesso.\n")
                            break
            else:
                print(f"O CPF {cpf} não está cadastrado.")
            if not continuar():
                return
            print()


def removerMotorista():
    ler()
    if len(get_bm()) == 0:
        print("Ainda não existe nenhum motorista cadastrado.")
        return
    else:
        print("=-=-=-Remover Motorista=-=-=-")
        print('=-'*15)
        while True:
            cpf = input("Insira um CPF com 11 dígitos do motorista que você deseja remover: ").strip()
            while not cpf.isdigit() or len(cpf) != 11:
                cpf = input("Informação incorreta. Digite somente números ou um CPF válido (com 11 dígitos): ").strip()
            if cpf in get_bm():  # Saber se o motorista existe ou não
                for motorista in get_bm().values():
                    if cpf == motorista.get('CPF'):
                        print('-=' * 25)
                        print(f'{"CPF":<18}{"Nome":10}{"Habilitação"}')
                        print(f"{motorista.get('CPF'):<18}{motorista.get('nome'):<10}{motorista.get('habilitacao')}")
                        print("-=" * 25)
                        opcao = str(input("Tem certeza que deseja deletar [S/N]? ")).strip().upper()
                        while opcao not in "SN":
                            opcao = str(input("Opção incorreta. Digite somente s - Sim ou n - Não: ")).strip().upper()
                        if opcao == "S":
                            del get_bm()[cpf]
                            escrever()
                            print("Motorista deletado com sucesso.\n")
                            break
                break
            else:
                print(f"O CPF {cpf} não está cadastrado.")


def listarMotoristasCNH():
    ler()
    if len(get_bm()) == 0:
        print("Ainda não existe nenhum motorista cadastrado.")
        return
    else:
        print('-=-=-=Motoristas Por Tipo de Carteira-=-=-=')
        habilitacao = str(input(f"Insira a carteira de habilitação (A, B ou AB): ")).strip().upper()
        while habilitacao not in "ABab":
            habilitacao = str(input(f"Informação incorreta. Digite somente uma carteira A, B ou AB: ")).strip().upper()
        contCNH = 0
        for motorista in get_bm().values():
            if motorista.get('habilitacao') == habilitacao:
                contCNH += 1
        if contCNH != 0:
            print(f"=-=-Motoristas Com Carteira {habilitacao}=-=-")
            print(f'{"CPF":<18}{"Nome":10}{"Habilitação"}')
            for motorista in get_bm().values():
                if habilitacao == motorista.get("habilitacao"):
                    print(f"{motorista.get('CPF'):<18}{motorista.get('nome'):<10}{motorista.get('habilitacao')}")
            print("-=" * 25)
        else:
            print(f"Não existem motoristas com carteira de habilitação {habilitacao} cadastrados.")
        if not continuar():
            return
        listarMotoristasCNH()


def listarMotoristas():
    ler()
    if len(get_bm()) == 0:
        print("Ainda não existe nenhum motorista cadastrado.")
        return
    else:
        print('-=-=-=-=-=Motoristas-=-=-=-=-=')
        print(f'{"CPF":<18}{"Nome":10}{"Habilitação"}')
        for motorista in get_bm().values():
            print(f"{motorista.get('CPF'):<18}{motorista.get('nome'):<10}{motorista.get('habilitacao')}")
        print("-=" * 25)
