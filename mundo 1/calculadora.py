
# ==================================
# PROJETO: CALCULADORA PYTHON
# FASE 1 - VERSAO INICIAL
# ==================================

print("================================")
print("       CALCULADORA PYTHON")
print("================================")

# Entrada dos numeros
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

# Menu de operacoes
print("\nEscolha uma operacao:")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

operacao = input("Digite a opcao desejada: ")

# Processamento
if operacao == "1":

    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "2":

    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "3":

    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "4":

    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)

    else:
        print("Erro: divisao por zero!")

else:

    print("Operacao invalida!")
