from act_validate import *

def console():
    id = 'Retry'

    while id == 'Retry':
        print('\n!!!!!Cuenta no encontrada. Reintente.!!!!!\n')
        id = validation()

    while True:
        accion = input('\nQue quieres hacer?\nPara depositar: dep||Para reirar: ret\n>> ')

        if accion == 'dep':
            depositar(id)
        elif accion == 'ret':
            retirar(id)