from cmath import log

folgaAnterior = str(input("Qual foi sua folga anterior? ")).lower()


if folgaAnterior == "é meu primeiro dia" or folgaAnterior == "terça-feira" or folgaAnterior == "quarta-feira":
    print("Sua próxima folga será domingo")
elif folgaAnterior == "domingo":
    folgaAntesdedomingo = str(input("Qual foi sua folga antes de domingo?"))
    if folgaAntesdedomingo == "terça-feira":
        print("Sua próxima folga será quinta-feira")
    elif folgaAntesdedomingo == "quarta-feira":
        print("Sua próxima folga será sexta-feira")
        
    else: print("Tente novamente. Opções válidas: \"terça-feira\", \"quarta-feira\"")

elif folgaAnterior == "quinta-feira":
    print("Sua próxima folga será terça-feira")
elif folgaAnterior == "sexta-feira":
    print("Sua próxima folga será quarta-feira")    
       
else: print("Tente novamente. Opções válidas: \"é meu primeiro dia\", \"terça-feira\", \"quarta-feira\" ou \"domingo\"")