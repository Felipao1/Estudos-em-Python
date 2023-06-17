# Solicita ao usuário para informar um valor N
N = int(input("Informe um valor para N: "))

# Inicializa a variável soma com zero
soma = 0

# Pede ao usuário para digitar N números e calcula a soma
for i in range(N):
    numero = float(input("Digite um número: "))
    soma += numero

# Calcula a média aritmética dos números digitados
media = soma / N

# Imprime a média
print("A média aritmética dos números digitados é:", media)