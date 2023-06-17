listaNumeros = []

while True:
    numero = float(input('Digite um número:\n'))
    if numero > 0:
        listaNumeros.append(numero)
    else:
        break
    mediaNumeros = (min(listaNumeros)*max(listaNumeros))**0.5
print(listaNumeros)
print ('A média geométrica da lista é entre {} e {}, que resultará em {}.'. format(min(listaNumeros), max(listaNumeros),mediaNumeros))
    
    


