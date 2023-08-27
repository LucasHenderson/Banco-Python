contas = {'adm@gmail.com': ['ADM', '123', 1000.00]}
chave = True



#FUNCTIONS------------------------------------------------------------
def login() -> str:
    email = input('---------------------------\nDigite seu email: ')
    senha = input('---------------------------\nDigite sua senha: ')
    if verificarEmail(email):
        if verificarLogin(email, senha):
            print(f'\n\nBem vindo {contas[email][0]}!\n---------------------------\n')
            return email
        else:
            print('\nEmail ou senha inválido!\n')
    else:
        print('\nO email não segue o padrão "@gmail.com"!\n')


def verificarLogin(email: str, senha: str) -> bool:
    if email in contas.keys() and senha == contas[email][1]:
        return True
    else:
        return False
 


def verificarEmail(email: str) -> bool:
    if not '@' in email:
        return False
    email = email.split('@')
    if email[1] == 'gmail.com':
        return True
    else:
        return False



def emailJahExistente(email: str) -> bool:
    if email in contas.keys():
        return True
    else:
        return False



def cadastrar() -> bool:
    email = input('Digite um email: ')
    if not verificarEmail(email):
        print('\nO email não segue o padrão "@gmail.com"!')
        return False
    elif emailJahExistente(email):
        print('\nInforme outro email!')
        return False
    else:
        senha = input('Digite uma senha: ')
        nome = input('Digite seu nome: ')
        contas[email] = [nome, senha, 0]
        print('\nConta cadastrada!')
        return True



def verSaldo(email: str):
    print(f'\nSeu saldo atual é de: {round(contas[email][2], 2)}\n')



def depositar(email: str):
    valor = float(input('\nDigite o valor que deseja depositar: '))
    if valor <= 0:
        print('\nO valor informado não pode ser depositado!\n')
    else:
        contas[email][2] = contas[email][2] + valor
        print('\nDepósito feito!\n')



def sacar(email: str):
    valor = float(input('\nDigite o valor que deseja sacar: '))
    if valor <= 0 or valor > contas[email][2]:
        print('\nO valor informado não pode ser sacado!\n')
    else:
        contas[email][2] = contas[email][2] - valor
        print('\nSaque feito!\n')



def tranferir(email):
    emailTransferencia = input('\nDigite o email para transferência: ')
    if emailTransferencia == email or emailTransferencia not in contas.keys():
        print('\nInforme um email válido!\n')
    else:
        valorTransferencia = float(input('Digite o valor que deseja transferir: '))
        if 0 >= valorTransferencia or valorTransferencia > contas[email][2]:
            print('\nNão é possível transferir o valor informado, tente novamente!\n')
        else:
            contas[email][2] = contas[email][2] - valorTransferencia
            contas[emailTransferencia][2] = contas[emailTransferencia][2] + valorTransferencia
            print('\nTransferência realizada!\n')



def menu(email: str):
    logado = True
    while logado:
        resposta = int(input('---------------------------\n1 - SALDO\n2 - DEPÓSITO\n3 - SAQUE\n4 - TRANSFERÊNCIA\n5 - SAIR\n---------------------------\n'))
        if resposta == 1:
            verSaldo(email)
        elif resposta == 2:
            depositar(email)
        elif resposta == 3:
            sacar(email)
        elif resposta == 4:
            tranferir(email)
        elif resposta == 5:
            logado = False
        else:
            print('\nOpção inválida, tente novamente!\n')
#---------------------------------------------------------------------



while chave:
    resposta = int(input('---------------------------\n1 - LOGIN\n2 - CADASTRO\n3 - ENCERRAR PROG.\n---------------------------\n'))
    if resposta == 1:
        email = login()
        if email != None:
            menu(email)
    elif resposta == 2:
        cadastrar()
    elif resposta == 3:
        chave = False
    else:
        print('Tente novamente!')