import textwrap


def menu():
 menu = ''' \n
 ===================== menu =========================

 [d] \t depositar 
 [s] \t sacar
 [e] \t extrato
 [nc]\t nova conta
 [lc]\t listar contas
 [nu]\t novo usuario
 [q] \t sair
 => '''
 return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato, /):
  if valor > 0:
       saldo += valor 
       extrato += f'deposito: \t R$ {valor:2f}\n'
       print('\n== deposito realizado com sucesso ==')

  else: 
      print ('\n@@@operação falhou: o valor informado é inválido.@@@')

  return saldo, extrato


def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n@@@ operação falhou!! você não tem saldo suficiente.@@@')

    
    elif excedeu_limite:
        print('\n@@@operação falhou! o valor excede o seu limite diário.\n@@@')

    elif valor > 0:
        saldo -= valor 
        extrato += f'saque:\t\t R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print ('\n@@@operação falhou! o valor informado é invalido!\n@@@')
    return saldo, extrato


def exibir_extrato(saldo, /,*,extrato):
    print ('\n================ EXTRATO ==================')
    print ('não foram realizadas movimentas bancárias' if not extrato else extrato)
    print (f'\nSaldo:\t\t R$ {saldo:.2f}')
    print ('=========================================')


def criar_usuario(usuarios):
    cpf = input('informe o CPF (somente número):')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ já existe um usuário com esse CPF!@@@')
        return
    

    nome = input('informe o nome completo')
    data_nascimento = input('informe sua data de nascimento (dd-mm-aaaa):')
    endereço = input('informe o endereço (logradouro, nro- bairro - cidade/sigla estado):')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereço})

    print ('== Usuário criado com sucesso!!===')



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None





def criar_conta(agencia,numero_conta,usuarios):
    cpf = input ('informe o cpf do usuario:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print('\n=== conta criada com sucesso!====')
      return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print ('\n@@ usuário nçao encontrado, fluxo de criação de conta encerrado! @@@@')



def listar_(contas):
    for conta in contas:
        linha= f'''\
           agência:\t{conta['agencia']}
           C/C:\t\t{conta['numero_conta']}
           titular:\t{conta['usuario']['nome']}
        '''
        print('=' *100)
        print(textwrap.dedent(linha))
 








def main():
   limite_saques = 3
   agencia = '0001'

   saldo = 0
   limite = 500
   extrato = ''
   numero_saques = 0
   usuarios = []
   contas = []
   
   while True:
       opcao = menu()

       if opcao == 'd':
          valor = float(input('informe o valor do deposito:'))
          saldo, extrato = depositar(saldo,valor, extrato)
         
         
         
       elif opcao == 's':
           valor = float(input('informe o valor do saque:'))

           saldo, extrato = sacar(
                saldo=saldo,
                valor = valor,
                extrato= extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            ) 
       
       
       
       elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
       elif opcao =='nu':
            criar_usuario(usuarios)

       elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
             contas.append(conta)

       elif opcao == 'q':
           break
       else:
           print('operação invalida,por favor selecione novamente a operação desejada')

main()