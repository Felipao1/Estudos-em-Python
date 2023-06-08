numeroTabuada = int(input('Digite um número'))
i = 0 
f = 10 
p = 1

cont = i


while cont<= f:
  resultado=(cont*numeroTabuada)
  print('{} x {} = {}'.format(numeroTabuada, cont, resultado))
  
  cont+=p
  

