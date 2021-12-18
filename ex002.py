print('Histórico Escolar Anual')
notaPrimeirobimestre=float(input('Informe a primeira nota'))
notaSegundobimestre=float(input('Informe a segunda nota'))
notaTerceirobimestre=float(input('Informe a terceira nota'))
notaQuartobimestre=float(input('Informe a quarta nota'))
notaFinal=((notaPrimeirobimestre+notaSegundobimestre+notaTerceirobimestre+notaQuartobimestre)/4)
print(notaFinal)
if(notaFinal)>=7.0: print('Aluno aprovado')
if(notaFinal)<7.0:print('Aluno em recuperação')
   


