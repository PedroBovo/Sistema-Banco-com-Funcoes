import textwrap
def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário 
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):  
    while valor<=0:
        valor = float(input("Impossivel depositar essa quantia, digite outro valor: "))
    if valor > 0:
        saldo+= valor  
        print(f"Saldo atual = R${saldo:.2f}")
        print()
        extrato += f"Deposito:\t R${valor}\n"
    
    return saldo, extrato

def saque(*, saldo, valor, valor_sacado ,extrato):
        
    while (valor > saldo) or (valor > 500):
        valor = float(input("Valor negado digite outro valor: "))
    if ((valor < saldo) or (valor < 500) ) and (valor > 0):
        saldo -= valor
        print(f"Saldo atual = R${saldo:.2f}")
        valor_sacado += valor 
        print(valor_sacado)
        extrato += f"Saque:\t\t R${valor_sacado}\n "                   

    return saldo, extrato

def gerar_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite seu cpf(apenas numeros):\t")
    usuario = valida_cpf(usuarios, cpf)
    if usuario:
        print("Usuario ja cadastrado")
        return

    nome = input("digite seu nome:\t")
    data_nascimento = input("Digite sua data de nascimento dd/MM/YY:\t")
    
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})

def valida_cpf(usuarios,cpf):
    filtrar_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtrar_usuario[0] if filtrar_usuario else None           

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf(apenas numeros):\t")
    usuario = valida_cpf(usuarios, cpf)

    if usuario:
        print("Conta Criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    

    print("Usuário nao encontrado, fluxo encerrado")

def listar_conta(contas):
    for conta in contas:
        lista = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(lista)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo= 1450.0
    valor_deposito = 0.0
    valor_sacado = 0
    numero_saques = 0
    limite = 500
    extrato =""
    usuarios = []
    contas = []
    numero_conta = 0

    while True:

        opcao = int(menu())
        if opcao == 1:
            valor = float(input("Qual valor deseja depositar? "))
            saldo, extrato =  depositar(saldo, valor, extrato)
            
                
        elif opcao == 2:
            if numero_saques < LIMITE_SAQUE:
                valor =float(input(f"Qual valor você vai querer sacar, lembrando que o valor maximo por saque é R$ {limite}: "))
                saldo, extrato = saque(saldo=saldo, valor=valor,extrato=extrato, valor_sacado= valor_sacado)
                numero_saques +=1
            else:
                print("Quantade de saque por dia foi excedida") 
                
        elif opcao == 3:
            gerar_extrato(saldo, extrato=extrato)
            
        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  
            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_conta(contas)  
    
        elif opcao == 0:
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
             
main()

        

