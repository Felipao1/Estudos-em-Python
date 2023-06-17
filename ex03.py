pares = 0
for i in range (5) :
    numero = int(input('Digite um número:\n'))
    if numero % 2 == 0:
        pares+=1
print ('{} números são pares.'.format(pares))