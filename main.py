#MENU 
import model
opcao = 1

while opcao != '3':
    print()
    print('Escolha uma opção abaixo: ')
    opcao = input('1 - Inserir nivel de decibeis; 2 - Ajuda; 3 - Sair do programa: ')
    if opcao == '1':
        model.decibeis()

    elif opcao== '2':
        model.ajuda()

    elif opcao== '3':
        print('Saindo do programa')

    else:
        print('Opcao Invalida')
