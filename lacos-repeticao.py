import time
import random

# --- Laços com for ---

# 1. Contagem Simples
print("Contagem de 1 a 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Números Pares
print("Números pares de 0 a 20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# 3. Tabuada
num_tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {num_tabuada}:")
for i in range(1, 11):
    print(f"{num_tabuada} x {i} = {num_tabuada * i}")

# 4. Soma de Números
soma_total = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    soma_total += num
print(f"A soma total dos números é: {soma_total}")

# 5. Contagem Regressiva
print("Contagem regressiva:")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # Pausa de 1 segundo
print("FIM!")

# 6. Soma dos Pares
soma_pares = 0
print("Digite 6 números:")
for i in range(6):
    num = int(input(f"{i+1}º número: "))
    if num % 2 == 0:
        soma_pares += num
print(f"A soma dos números pares digitados é: {soma_pares}")

# 7. Fatorial
num_fatorial = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
if num_fatorial >= 0:
    for i in range(1, num_fatorial + 1):
        fatorial *= i
    print(f"O fatorial de {num_fatorial} é {fatorial}")
else:
    print("Não existe fatorial de número negativo.")

# 8. Média de Notas
qtd_alunos = int(input("Digite a quantidade de alunos: "))
soma_notas = 0
for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma_notas += nota
media_turma = soma_notas / qtd_alunos
print(f"A média da turma é: {media_turma:.2f}")

# --- Laços com while ---

# 9. Senha Correta
while True:
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Acesso Permitido")
        break
    else:
        print("Senha incorreta. Tente novamente.")

# 10. Validação de Nota
while True:
    nota_valida = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota_valida <= 10:
        print(f"Nota {nota_valida} registrada com sucesso.")
        break
    else:
        print("Valor inválido. A nota deve ser entre 0 e 10.")

# 11. Soma Até Zero
soma_ate_zero = 0
print("Digite números para somar. Digite 0 para parar.")
while True:
    num = float(input("Número: "))
    if num == 0:
        break
    soma_ate_zero += num
print(f"A soma total foi: {soma_ate_zero}")

# 12. Menu Simples
while True:
    print("\n--- MENU ---")
    print("1 - Saudar")
    print("2 - Mostrar número secreto")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Olá! Tenha um ótimo dia!")
    elif opcao == '2':
        print("O número secreto é 42.")
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# 13. Contador Crescente/Decrescente
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

if inicio < fim:
    # Contagem crescente
    for i in range(inicio, fim + 1):
        print(i, end=" ")
elif inicio > fim:
    # Contagem decrescente
    for i in range(inicio, fim - 1, -1):
        print(i, end=" ")
else:
    print("Os números são iguais.")
print()

# 14. Número Secreto
numero_secreto = random.randint(1, 100)
print("Adivinhe o número secreto entre 1 e 100!")
while True:
    palpite = int(input("Qual o seu palpite? "))
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é Maior.")
    else:
        print("O número secreto é Menor.")

# 15. Média com Quantidade Indeterminada
notas_validas = []
print("Digite as notas. Digite um valor negativo para calcular a média.")
while True:
    nota = float(input("Nota: "))
    if nota < 0:
        break
    notas_validas.append(nota)

if len(notas_validas) > 0:
    media_indeterminada = sum(notas_validas) / len(notas_validas)
    print(f"A média das {len(notas_validas)} notas válidas é {media_indeterminada:.2f}.")
else:
    print("Nenhuma nota válida foi digitada.")