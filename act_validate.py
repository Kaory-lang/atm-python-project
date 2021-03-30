import random

def register():
    nombre = input('Introduce tu nombre y apellido>> ')
    pin = input('Introduce una clave/pin (Sin espacios, seran eliminados)>> ')
    pin = pin.replace(' ', '')

    nCuenta = []
    
    for i in range(1,11):
        nCuenta.append(str(random.randint(1,9)))

    print('Tu numero de cuenta es ' + ''.join(nCuenta) + ' No lo pierdas y apuntalo.\n')

    l_accounts = open('./accounts.txt', 'a')
    l_accounts.write('\n' + nombre + '|' + ''.join(nCuenta) + '|' + pin + '|' + '0')
    l_accounts.close()
    return validation()


def validation():
    nCuenta = input('Bienvenid@ al ATM\nIngrese su número de cuenta>>\nSi no tienes cuenta escribe -r para registrarte>> ')
    if nCuenta == '-r':
        return register()
        
    l_accounts = open('./accounts.txt')

    lista = l_accounts.read().splitlines()
    index = 0
    tries = 0
    pin = None

    for l in lista:
        if nCuenta == l.split('|')[1]:
            while pin != l.split('|')[2] and tries != 3:
                tries = tries + 1
                pin = input('Introduce el pin>> ')

            if pin == l.split('|')[2]:
                print('\nBienvenido ' + l.split('|')[0] + '. Su balance actual es = ' + l.split('|')[3])
                return index
        index = index + 1        
    return "Retry"

def desglosador(monto):
    results = []

    while monto >= 2000:
        monto = monto - 2000
        results.append(2000)
    while monto >= 1000:
        monto = monto - 1000
        results.append(1000)
    while monto >= 500:
        monto = monto - 500
        results.append(500)
    while monto >= 200:
        monto = monto - 200
        results.append(200)
    while monto >= 100:
        monto = monto - 100
        results.append(100)
    while monto >= 50:
        monto = monto - 50
        results.append(50)
    while monto >= 25:
        monto = monto - 25
        results.append(25)
    while monto >= 10:
        monto = monto - 10
        results.append(10)
    while monto >= 5:
        monto = monto - 5
        results.append(5)
    while monto >= 1:
        monto = monto - 1
        results.append(1)
    return results

def to_str(string):
    try:
        return int(string)
    except:
        print('No se permiten valores que no sean solo numeros\n')

def depositar(id):
    monto = None

    while type(monto) != int:
        monto = input('Introduce el monto a depositar>> ')
        monto = to_str(monto)

    results = desglosador(monto)

    print('\nTienes que depositar:\n')
    if results.count(2000) != 0:
        print(str(results.count(2000)) + ' Papeletas de 2000')
    if results.count(1000) != 0:
      print(str(results.count(1000)) + ' Papeletas de 1000')
    if results.count(500) != 0:
      print(str(results.count(500)) + ' Papeletas de 500')
    if results.count(200) != 0:
      print(str(results.count(200)) + ' Papeletas de 200')
    if results.count(100) != 0:
      print(str(results.count(100)) + ' Papeletas de 100')
    if results.count(50) != 0:
      print(str(results.count(50)) + ' Papeletas de 50')
    if results.count(25) != 0:
      print(str(results.count(25)) + ' Monedas de 25')
    if results.count(10) != 0:
      print(str(results.count(10)) + ' Monedas de 10')
    if results.count(5) != 0:
      print(str(results.count(5)) + ' Monedas de 5')
    if results.count(1) != 0:
        print(str(results.count(1)) + ' Monedas de 1')
    ########################################################

    f = open('./accounts.txt', 'r')
    index = 0

    lista = f.read().splitlines()
    f.close()

    for i in lista:
        if id == index:
            lp = i.split('|')
            lp[3] = str(int(lp[3]) + monto)
            lista[index] = lp
            lista[id] = '|'.join(lista[id])
            break
        index = index + 1

    f = open('./accounts.txt', 'w')
    index = 0

    for l in lista:
        if index == 0:
            f.write(l)
        else:
            f.write('\n' + l)
        index = index + 1
    f.close()
    print('\nSu nuevo balance es de =', lp[3])
    


def retirar(id):
    monto = None

    while type(monto) != int:
        monto = input('Introduce el monto a reitrar>> ')
        monto = to_str(monto)

    results = desglosador(monto)

    print('\nRecibiras:\n')
    if results.count(2000) != 0:
        print(str(results.count(2000)) + ' Papeletas de 2000')
    if results.count(1000) != 0:
      print(str(results.count(1000)) + ' Papeletas de 1000')
    if results.count(500) != 0:
      print(str(results.count(500)) + ' Papeletas de 500')
    if results.count(200) != 0:
      print(str(results.count(200)) + ' Papeletas de 200')
    if results.count(100) != 0:
      print(str(results.count(100)) + ' Papeletas de 100')
    if results.count(50) != 0:
      print(str(results.count(50)) + ' Papeletas de 50')
    if results.count(25) != 0:
      print(str(results.count(25)) + ' Monedas de 25')
    if results.count(10) != 0:
      print(str(results.count(10)) + ' Monedas de 10')
    if results.count(5) != 0:
      print(str(results.count(5)) + ' Monedas de 5')
    if results.count(1) != 0:
        print(str(results.count(1)) + ' Monedas de 1')
    ########################################################

    f = open('./accounts.txt', 'r')
    index = 0

    lista = f.read().splitlines()
    f.close()

    for i in lista:
        if id == index:
            lp = i.split('|')
            lp[3] = str(int(lp[3]) - monto)
            lista[index] = lp
            lista[id] = '|'.join(lista[id])
            break
        index = index + 1

    f = open('./accounts.txt', 'w')
    index = 0

    for l in lista:
        if index == 0:
            f.write(l)
        else:
            f.write('\n' + l)
        index = index + 1
    f.close()
    print('\nSu nuevo balance es de =', lp[3])