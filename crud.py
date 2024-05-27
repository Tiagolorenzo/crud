'''
Crie um programa que tenha as opções:
- inserir pessoa na lista
- listar pessoa cadastrada
- pesquisar pelo nome de uma pessoa
- ordenar a lista por ordem alfabetica
- atualizar nome
- deletar nome da lista
- sair do programa
'''
lista = ['Argentino', 'Espanhol', "Cubano"]

while True:
    print('Menu:')
    print('1. Inserir nome na lista')
    print('2. Listar nomes cadastrados')
    print('3. Pesquisar por nome')
    print('4. Ordenar lista por ordem alfabética')
    print('5. Atualizar nome na lista')
    print('6. Deletar nome na lista')
    print('7. Sair do programa')
    opcao = input('Escolha uma opção: ')

    # Inserir pessoa na lista
    if opcao == '1':
        nome = input('Digite o nome: ')
        lista.append(nome)
        print(f'{nome} foi adicionado.')

    # Listar pessoas cadastradas
    elif opcao == '2':
        if lista:
            print('Nomes cadastrados:')
            for i, pessoa in enumerate(lista, 1):
                print(f'{i}. {pessoa}')
        else:
            print('Nenhum nome cadastrado.')

    # Pesquisar pelo nome de uma pessoa
    elif opcao == '3':
        nome = input('Digite o nome a ser pesquisado: ')
        if nome in lista:
            print(f'{nome} está na lista.')
        else:
            print(f'{nome} não foi encontrado na lista.')

    # Ordenar a lista por ordem alfabética
    elif opcao == '4':
        lista.sort()
        print('Lista em ordem alfabética:')
        for pessoa in lista:
            print(pessoa)

    # Atualizar nome
    elif opcao == '5':
        nome_antigo = input('Digite o nome a ser atualizado: ')
        if nome_antigo in lista:
            novo_nome = input('Digite o novo nome: ')
            index = lista.index(nome_antigo)
            lista[index] = novo_nome
            print(f'O nome {nome_antigo} foi atualizado para {novo_nome}.')
        else:
            print(f'{nome_antigo} não foi encontrado na lista.')

    # Deletar nome da lista
    elif opcao == '6':
        nome = input('Digite o nome a ser deletado: ')
        if nome in lista:
            lista.remove(nome)
            print(f'{nome} foi removido da lista.')
        else:
            print(f'{nome} não foi encontrado na lista.')

    # Sair do programa
    elif opcao == "7":
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida, tente novamente!')