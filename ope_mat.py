# Receber dois numeros, um tipo de operação (+, -, *, /) e retornar o resultado da operação.
def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "Operação inválida"
    return "Operação inválida"

# Exemplo de uso
if __name__ == "__main__":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")
    
    resultado = calcular(n1, n2, op)
    print(f"O resultado da operação é: {resultado}")