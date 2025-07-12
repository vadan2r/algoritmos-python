# Receber string e número, repetir a string o número de vezes
def repetir_string(s, n):
    return s * n

# Solicita os dados ao usuário
texto = input("Digite o texto a ser repetido: ")
numero = int(input("Digite o número de repetições: "))

# Chama a função e imprime o resultado
resultado = repetir_string(texto, numero)
print("O resultado da repetição é:", resultado)