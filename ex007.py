n1=float(input('digite um número '))
n2=float(input('digite outro número '))

operacao=input('Escolha uma operação ')
if operacao=='+':
    print(n1+n2)
elif operacao=='-':
    print(n1-n2)
elif operacao=='*':
    print(n1*n2)
elif operacao=='/':
    print(n1/n2)
elif operacao=='^':
    print(n1**n2)
else:
    print('OPERAÇÃO INVÁLIDA')
operacao=input('Escolha uma operação ')



