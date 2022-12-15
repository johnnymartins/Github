# variáveis globais
#------------------#

cont_id = 1000 # variável com valor pré estabelecido pra determinar número inicial pra variável acumulador de Id
lista_func = [] # declarada lista que irá armazenar os dicionários corresponde aos funcionários e suas informações

#------------------#


def cadastrar_funcionario(id):  # função em que é feito o cadastro de funcionário na lista
  print('---------------------Menu de cadastro de funcionários----------------------''\n')
  print('Código de funcionário: {}'.format(id)) # retorna ao console o código acrescido de 1 pra cada novo cadastro
  nome_func = input('Informe o nome do funcionário: ') # variável que recebe o nome do funcionário
  set_func = input('Informe o setor: ') # variável que recebe o setor do funcionário
  set_func = set_func.upper() # torna a letra do setor maiúscula pra padronizar o formato
  sal_func = int(input('Informe o salário (R$): ')) # variável que recebe o salário do funcionário
  dic_func = {'Id': id, # determina o valor recebido da variável acumulador de Id como valor correspondente à chave "Id"
              'Nome' : nome_func, # determina o valor recebido da variável nome_func como valor
              # correspondente à chave "Nome"
              'Setor' : set_func, # determina o valor recebido da variável set_func como valor
              # correspondente à chave "Setor"
              'Salário' : sal_func}  # determina o valor recebido da variável sal_func como valor correspondente à
# chave "Salário"
  lista_func.append(dic_func.copy()) # insere na lista (lista_func) os dicionários criados pela funcão de cadastro
# de funcionários


def consultar_funcionarios():  # função em que é feita a consulta de funcionário da lista
  while True:
    print('---------------------Menu de consulta de funcionários----------------------''\n')
    consulta_func = input('1 - Consultar todas os funcionários''\n'+
                          '2 - Consultar funcionário por Id''\n'+
                          '3 - Consultar funcionário(s) por setor''\n'+
                          '4 - Retornar''\n'+
                          '>> ')

    if consulta_func == '1': # caso o usuário escolha a opção de consultar todos os funcionários
      print('--------------------------Todos os funcionários----------------------------')
      for func in lista_func: # busca na lista todos os itens
        print('-'*75)
        for chave, valor in func.items(): # pra cada item/dicionário na lista, retorna a chave e respectivo valor
          print('{}: {}'.format(chave, valor))

    elif consulta_func == '2': # caso o usuário escolha a opção de consultar funcionários por Id
      print('---------------------------Funcionários por Id-----------------------------')
      try: # trata a possibilidade de o usuário inserir valor que não seja número inteiro
        opcao_id = int(input('Qual Id deseja consultar?''\n'+
                      '>> '))
        for func in lista_func: # busca na lista todos os itens
          if func['Id'] == opcao_id: # se o valor inserido na variável opcao_id for encontrado como sendo
            # correspondente à uma chave "Id", entra no dicionário
            for chave, valor in func.items(): # encontra o funcionário correspondente à Id inserida na variável opcao_id
              print('{}: {}'.format(chave, valor)) # retorna o funcionário correspondente à Id inserida na
              # variável opcao_id
      except ValueError: # caso o usuário insira valor que não seja número inteiro, apresenta a mensagem abaixo e
        # continua no laço
        print('Você digitou uma Id inválida.')

    elif consulta_func == '3': # caso o usuário escolha a opção de consultar funcionários por setor
      print('--------------------------Funcionários por setor---------------------------')
      opcao_setor = input('Qual setor deseja consultar?''\n'+
                      '>> ') # variável recebe a letra do setor inserida pelo usuário
      opcao_setor = opcao_setor.upper() # torna maiúscula a letra pra corresponder à existente no cadastro
      for func in lista_func: # busca na lista todos os itens
        print('-'*75)
        if func['Setor'] == opcao_setor: # se o valor inserido na variável opcao_setor for encontrado como sendo
            # correspondente à uma chave "Setor", entra no dicionário
          for chave, valor in func.items(): # encontra o funcionário correspondente ao Setor inserida na
            # variável opcao_setor
            print('{}: {}'.format(chave, valor)) # retorna o funcionário correspondente ao Setor inserida na
            # variável opcao_setor

    elif consulta_func == '4': # caso o usuário escolha a opção de retornar ao menu principal
      return # encerra o laço e retorna ao menu principal
    else: # caso o usuário insira qualquer valor não existente, recebe a mensagem abaixo e continua no laço
      print('Você selecionou uma opção inválida.')
      continue


def remover_funcionario(): # função em que é feita a remoção de funcionário da lista
  print('----------------------Menu para remover funcionários-----------------------')
  remove_id = int(input('Digite a Id do funcionário que deseja remover.''\n'+
                        '>> ')) # variável que recebe o valor de Id inserido pelo usuário
  for id in lista_func: # busca na lista todos os itens
    if id['Id'] == remove_id: # se o valor inserido na variável remove_id for encontrado como sendo correspondente à
        # uma chave "ID", seleciona o dicionário na lista
      lista_func.remove(id) # remove da lista o dicionário correspondente à Id inserida na variável remove_id

# progrma principal
# *--------------------------------------------------------------------------------------*


print('Bem vindo ao cadastro de funcionários de Jonathan de Oliveira Martins''\n')

while True: # inicia o programa com o menu principal estando num laço infinito
  print('------------------------------Menu principal-------------------------------''\n')
  opcao_menu = input('Escolha a opção desejada:''\n'+
                     '1 - Cadastrar funcionário''\n'+
                     '2 - Consultar funcionários(s)''\n'+
                     '3 - Remover funcionário''\n'+
                     '4 - Sair''\n'+
                     '>> ')
  if opcao_menu == '1': # caso o usuário insira a opção de cadastro de funcionário na variável opcao_menu
    cont_id += 1 # variável acumulador de Id pra cada novo cadastro
    cadastrar_funcionario(cont_id) # chama a função cadastrar_funcionario() já enviando a ela o valor da variável
# acumuladora de Id
  elif opcao_menu == '2': # caso o usuário insira a opção de consulta de funcionário na variável opcao_menu
    consultar_funcionarios() # chama a função consultar_funcionarios()
  elif opcao_menu == '3': # caso o usuário insira a opção de cadastro de funcionário na variável opcao_menu
    remover_funcionario() # chama a função remover_funcionario()
  elif opcao_menu == '4': # caso o usuário insira a opção de sair na variável opcao_menu
    print('Programa encerrado.')
    break # encerra o laço após apresentar a mensagem acima
  else: # caso o funcionário insira na variável opcao_menu um valor inexistente nas opções apresentadas no menu
# principal, recebe a mensagem abaixo e continua no laço
    print('Você escolheu uma opção inexistente.')
    continue
