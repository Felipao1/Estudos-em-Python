n = float(input('Digite um número:\n'))
x = 0
y = 0

while(x < n):
    z = float(input('Digite um número:\n'))
    x+=1
    y+=z
    media = y/x
    
    
print('Média: {}/{} = {}.'.format(y, x, media))    
    
