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