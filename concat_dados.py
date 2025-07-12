# Receber dois dados diferentes e concatená-los
def concat_dados(dado1, dado2):
    """
    Concatena dois dados diferentes e retorna o resultado.

    Args:
        dado1 (str): O primeiro dado a ser concatenado.
        dado2 (str): O segundo dado a ser concatenado.

    Returns:
        str: A concatenação dos dois dados.
    """
    return dado1 + dado2

# Solicita os dados ao usuário
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Chama a função e imprime o resultado
resultado = concat_dados(dado1, dado2)
print("O resultado da concatenação é:", resultado)