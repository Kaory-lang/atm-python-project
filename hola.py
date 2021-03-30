f = open('./dup.txt', 'r')

id = 0
index = 0
monto = 14349

lista = f.read().splitlines()
f.close()

for i in lista:
    print(i.split('|'))
    if id == index:
        lp = i.split('|')
        lp[3] = str(monto)
        lista[index] = lp
        lista[0] = '|'.join(lista[0])
        break
    index = index + 1

f = open('./dup.txt', 'w')
index = 0
for l in lista:
    if index == 0:
        f.write(l)
    else:
        f.write('\n' + l)
    index = index + 1
f.close()