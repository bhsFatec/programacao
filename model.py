def decibeis():
    print ('Voce usa EPI adequado?')
    print()
    opcao= input ('1 sim ; 2 nao: ')
    print()
    if opcao=='1':
        nivel =float(input('insira o valor RRfs: '))
        print()
        decibel =float (input('insira valor em decibeis: '))
        decibeis = decibel-nivel
        print()
    elif opcao =='2':
        decibeis =float(input('Insira valor em decibeis: '))


    if decibeis<=85:
        print('Tempo de exposicao: 8h')
        
    elif decibeis==86:
        print('Tempo de exposicao: 7h')
        
    elif decibeis==87:
        print('Tempo de exposicao: 6h')
        
    elif decibeis==88:
        print('Tempo de exposicao: 5h')
        
    elif decibeis==89:
        print('Tempo de exposicao: 4h 30min')
        
    elif decibeis==90:
        print('Tempo de exposicao: 4h')
        
    elif decibeis==91:
        print('Tempo de exposicao: 3h 30min')
        
    elif decibeis==92:
        print('Tempo de exposicao: 3h')
        
    elif decibeis==93:
        print('Tempo de exposicao: 2h 40min')
        
    elif decibeis==94:
        print('Tempo de exposicao: 2h 15min')
        
    elif decibeis==95:
        print('Tempo de exposicao: 2h')

    elif decibeis==96:
        print('Tempo de exposicao: 1h 45min')
        
    elif decibeis<=98:
        print('Tempo de exposicao: 1h 15min')
        
    elif decibeis<=100:
        print('Tempo de exposicao: 1h')

    elif decibeis<=102:
        print('Tempo de exposicao: 45min')
            
    elif decibeis<=104:
        print('Tempo de exposicao: 35min')
            
    elif decibeis==105:
        print('Tempo de exposicao: 30min')
            
    elif decibeis==106:
        print('Tempo de exposicao: 25min')
            
    elif decibeis<=108:
        print('Tempo de exposicao: 20min')
            
    elif decibeis<=110:
        print('Tempo de exposicao: 15min')
            
    elif decibeis<=112:
        print('Tempo de exposicao: 10min')
            
    elif decibeis<=114:
        print('Tempo de exposicao: 8min')
            
    elif decibeis>=115:
        print('Tempo de exposicao: 7min')

def ajuda():
    print('Insira o valor em decibeis e o nivel de protecao NRRsf de seu EPI,\
caso não saiba este ultimo insira apenas o numero em decibeis.')
