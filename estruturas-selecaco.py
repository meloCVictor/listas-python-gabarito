# 1. Par ou Ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

# 2. Maior de Dois Números
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
if n1 > n2:
    print("O primeiro número é o maior.")
elif n2 > n1:
    print("O segundo número é o maior.")
else:
    print("Os dois números são iguais.")

# 3. Positivo ou Negativo
num = float(input("Digite um número: "))
if num > 0:
    print("O número é POSITIVO.")
elif num < 0:
    print("O número é NEGATIVO.")
else:
    print("O número é ZERO.")

# 4. Aumento Salarial
salario = float(input("Informe o salário do funcionário: R$ "))
if salario > 1500.00:
    novo_salario = salario * 1.10  # Aumento de 10%
else:
    novo_salario = salario * 1.15  # Aumento de 15%
print(f"O novo salário é de R$ {novo_salario:.2f}.")

# 5. Média e Situação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Média: {media:.1f}")
if media >= 7.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")

# 6. Triângulo Válido
l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos NÃO podem formar um triângulo.")

# 7. Classificação do Triângulo
# (Considerando que a verificação do exercício 6 foi feita)
l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Forma um triângulo ", end="")
    if l1 == l2 == l3:
        print("EQUILÁTERO.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("ISÓSCELES.")
    else:
        print("ESCALENO.")
else:
    print("Os segmentos NÃO podem formar um triângulo.")

# 8. Verificar Ano Bissexto
ano = int(input("Digite um ano para verificar: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} não é BISSEXTO.")

# 9. Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar (+, -, *, /)? ")
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

# 10. Classificação Etária
idade = int(input("Digite a idade: "))
if idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")