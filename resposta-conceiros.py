# 1. Exibir a frase
print("Seja bem-vindo ao mundo do Python!")

# 2. Mensagem de boas-vindas com nome
nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}, seja bem-vindo!")

# 3. Exibir idade
idade = input("Digite sua idade: ")
print(f"Você tem {idade} anos.")

# 4. Soma de dois números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}.")

# 5. Exibir nome e idade na mesma frase
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
print(f"{nome} tem {idade} anos.")

# 6. Dobro de um número decimal
num_decimal = float(input("Digite um número decimal: "))
dobro = num_decimal * 2
print(f"O dobro de {num_decimal} é {dobro}.")

# 7. Área de um quadrado
lado = float(input("Digite o lado do quadrado: "))
area = lado * lado
print(f"A área de um quadrado de lado {lado} é {area}.")

# 8. Produto com 10% de desconto
valor_produto = float(input("Digite o valor do produto: R$ "))
valor_com_desconto = valor_produto * 0.90
print(f"O valor com 10% de desconto é R$ {valor_com_desconto:.2f}.")

# 9. Preço do aluguel de carro
dias_alugados = int(input("Quantos dias o carro foi alugado? "))
km_percorridos = float(input("Quantos km foram percorridos? "))
valor_a_pagar = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f"O valor total a pagar é de R$ {valor_a_pagar:.2f}.")

# 10. Média de três notas
nome_aluno = input("Nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média de {nome_aluno} é {media:.1f}.")

# 11. Antecessor e sucessor
numero_int = int(input("Digite um número inteiro: "))
print(f"O antecessor de {numero_int} é {numero_int - 1}.")
print(f"O sucessor de {numero_int} é {numero_int + 1}.")

# 12. Conversor de metros
metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros}m corresponde a {centimetros:.0f}cm e {milimetros:.0f}mm.")

# 13. Dobro, triplo e raiz quadrada
import math
numero = int(input("Digite um número: "))
print(f"O dobro de {numero} é {numero * 2}.")
print(f"O triplo de {numero} é {numero * 3}.")
print(f"A raiz quadrada de {numero} é {math.sqrt(numero):.2f}.")

# 14. Operações básicas
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
if n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2:.2f}")
else:
    print("Não é possível dividir por zero.")

# 15. Conversor de temperatura
celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C corresponde a {fahrenheit:.1f}°F.")

# 16. Aumento de 15%
salario_atual = float(input("Qual é o salário do funcionário? R$ "))
novo_salario = salario_atual * 1.15
print(f"Um funcionário que ganhava R${salario_atual:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}.")

# 17. Cálculo de IMC
peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}.")

# 18. Preço da passagem
distancia_km = float(input("Qual a distância da viagem em km? "))
if distancia_km <= 200:
    preco_passagem = distancia_km * 0.50
else:
    preco_passagem = distancia_km * 0.45
print(f"O preço da sua passagem será de R${preco_passagem:.2f}.")

# 19. Situação do aluno
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Terceira nota: "))
nota_4 = float(input("Quarta nota: "))
media_aluno = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"A média do aluno foi {media_aluno:.1f}.")
if media_aluno >= 7.0:
    print("Situação: APROVADO")
elif media_aluno >= 5.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")

# 20. Maior de dois números
num_a = float(input("Primeiro número: "))
num_b = float(input("Segundo número: "))
if num_a > num_b:
    print("O primeiro valor é maior.")
elif num_b > num_a:
    print("O segundo valor é maior.")
else:
    print("Os dois valores são iguais.")