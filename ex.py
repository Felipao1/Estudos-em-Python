rapazesMaiores = 0
somaIdadeMulheres = 0
mulheres = 0
mediaIdadeMulheres = 0
while True:
    sexo = input('Informe seu sexo [M|F]:')
    if sexo.upper() != 'M' and sexo.upper() != 'F':
        print('Opção de sexo inválida.')
        break
      
    idade = int(input('Informe a idade'))
    if idade < 0:
        break
    
    if sexo.upper() == 'M' and idade == 18:
        rapazesMaiores+=1
        
    elif sexo.upper() == 'F':
        somaIdadeMulheres += idade
        mulheres += 1
if mulheres > 0:       
    mediaIdadeMulheres = somaIdadeMulheres/mulheres       
print('Rapazes acima de 18 anos: {}'.format(rapazesMaiores))
print('Média da idade das moças: {}'.format(mediaIdadeMulheres))
    