import random

l_accounts = open('./accounts.txt')
lista = l_accounts.read().splitlines()
pin_list = None
index = 0

#Register
lista_register = []

def validation(usr):
    global pin_list
    global index
    index = 0

    for l in lista:
        if usr == l.split('|')[1]:
            pin_list = l.split('|')[2]
            return 'Ok'
        index = index + 1
    
    return 'Retry'

def validation_pin(pin):
    if pin == pin_list:
        return 'Ok'
    else:
        return 'Retry'

def register_gui(get, n):
    lista_register.append(get)

    if n == 1:
        lista_register[1] = lista_register[1].replace(' ', '')

        nCuenta = []
    
        for i in range(1,11):
            nCuenta.append(str(random.randint(1,9)))

        l_accounts = open('./accounts.txt', 'a')
        l_accounts.write('\n' + lista_register[0] + '|' + ''.join(nCuenta) + '|' + lista_register[1] + '|' + '0')
        l_accounts.close()

        return ''.join(nCuenta)

def get_balance():
    l_accounts = open('./accounts.txt')
    lista = l_accounts.read().splitlines()
    lista = lista[index].split('|')

    return str(lista[3])

def get_usr():
    l_accounts = open('./accounts.txt')
    lista = l_accounts.read().splitlines()
    lista = lista[index].split('|')

    return str(lista[0])

def get_id():
    return index

def desglosador(monto):
    results = []
    monto = int(monto)

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
        return 'No Number'

def depositar_fn(id, monto):

    if to_str(monto) == 'No Number':
        return 'No Number'

    results = desglosador(monto)
    if type(id) == int:  
        monto = int(monto)
        
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
    return results

def retirar_fn(id, monto):

    if to_str(monto) == 'No Number':
        return 'No Number'

    results = desglosador(monto)
    if type(id) == int:  
        monto = int(monto)
        
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
    return results