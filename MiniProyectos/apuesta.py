#Proyecto de minijuego que da cara o cruz

import random

elePlayer = input('Por cual apuestas cara o cruz (c,x): ')
keepPlay = True

while keepPlay:
    coin = random.randrange(0,2)
    
    if elePlayer != 'c' and elePlayer !='x':
        print('No has escrito una elección adecuada, vuelve a elegir')
        elePlayer = input('Por cual apuestas cara o cruz (c,x): ')

    if elePlayer == 'c' and coin == 0:
        print('Enhorabuena, has acertado!!')
    elif elePlayer == 'x' and coin == 1:
        print('Enhorabuena, has acertado!!')
    else:
        print('Has fallado')

    playerKeep = input('Quieres seguir jugando? (s,n): ')

    if playerKeep == 's':
        keepPlay = True
        elePlayer = input('Por cual apuestas cara o cruz (c,x): ')
    elif playerKeep == 'n':
        keepPlay = False
        break
    else:
        playerKeep = input('No has elegido bien, quieres seguir jugando? (s,n): ')
        
if not keepPlay:
    print('Se ha terminado de jugar')