# --- Vetores (Listas) ---

# 1. Preencher e mostrar vetor
vetor_5pos = []
for i in range(5):
    num = int(input(f"Digite o valor para a posição {i}: "))
    vetor_5pos.append(num)
print("Valores do vetor:", vetor_5pos)

# 2. Mostrar apenas os pares
vetor_10num = []
print("Digite 10 números:")
for _ in range(10):
    vetor_10num.append(int(input()))
print("Números pares digitados:")
for num in vetor_10num:
    if num % 2 == 0:
        print(num, end=" ")
print()

# 3. Mostrar maior e menor
vetor_8num = []
print("Digite 8 números:")
for _ in range(8):
    vetor_8num.append(int(input()))
print(f"Maior valor: {max(vetor_8num)}")
print(f"Menor valor: {min(vetor_8num)}")

# 4. Buscar nome na lista
nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Fernanda"]
nome_busca = input("Digite um nome para buscar na lista: ")
if nome_busca in nomes:
    print(f"O nome '{nome_busca}' está na lista!")
else:
    print(f"O nome '{nome_busca}' não foi encontrado.")

# 5. Média dos números em um vetor
vetor_media = []
print("Digite 10 números para calcular a média:")
for _ in range(10):
    vetor_media.append(int(input()))
media = sum(vetor_media) / len(vetor_media)
print(f"A média dos números é: {media}")

# 6. Mostrar na ordem inversa
vetor_inverso = []
print("Digite 5 números:")
for _ in range(5):
    vetor_inverso.append(int(input()))
print("Vetor na ordem inversa:", vetor_inverso[::-1])

# 7. Soma de dois vetores
vetor1 = [1, 2, 3, 4, 5]
vetor2 = [6, 7, 8, 9, 10]
vetor_soma = []
for i in range(len(vetor1)):
    vetor_soma.append(vetor1[i] + vetor2[i])
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor Soma: {vetor_soma}")

# 8. Contar positivos, negativos e zeros
numeros = []
print("Digite 7 números:")
for _ in range(7):
    numeros.append(float(input()))
positivos = sum(1 for n in numeros if n > 0)
negativos = sum(1 for n in numeros if n < 0)
zeros = sum(1 for n in numeros if n == 0)
print(f"Positivos: {positivos}, Negativos: {negativos}, Zeros: {zeros}")

# 9. Contar ocorrências de um número
vetor_ocorrencias = [5, 2, 3, 5, 8, 5]
print(f"Vetor: {vetor_ocorrencias}")
num_busca = int(input("Qual número você quer contar no vetor? "))
ocorrencias = vetor_ocorrencias.count(num_busca)
print(f"O número {num_busca} aparece {ocorrencias} vez(es).")

# 10. Pessoa mais velha
lista_nomes = ["João", "Maria", "Pedro", "Lia", "José"]
lista_idades = [25, 32, 28, 45, 38]
idade_maxima = max(lista_idades)
indice_mais_velho = lista_idades.index(idade_maxima)
nome_mais_velho = lista_nomes[indice_mais_velho]
print(f"A pessoa mais velha é {nome_mais_velho} com {idade_maxima} anos.")


# --- Matrizes ---

# 11. Preencher e mostrar matriz 3x3
matriz = []
print("Preencha a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz formatada:")
for linha in matriz:
    print(linha)

# 12. Soma de todos os elementos da matriz
# (Usando a matriz do exercício anterior)
soma_matriz = 0
for linha in matriz:
    soma_matriz += sum(linha)
print(f"\nA soma de todos os elementos é: {soma_matriz}")

# 13. Soma de linhas e colunas (Matriz 2x4)
matriz_2x4 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# Soma das linhas
for i, linha in enumerate(matriz_2x4):
    print(f"Soma da linha {i+1}: {sum(linha)}")
# Soma das colunas
for j in range(4): # 4 colunas
    soma_coluna = 0
    for i in range(2): # 2 linhas
        soma_coluna += matriz_2x4[i][j]
    print(f"Soma da coluna {j+1}: {soma_coluna}")

# 14. Elementos da diagonal principal (Matriz 3x3)
matriz_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nElementos da diagonal principal:")
for i in range(3):
    print(matriz_3x3[i][i], end=" ")
print()

# 15. Elementos da diagonal secundária (Matriz 3x3)
print("\nElementos da diagonal secundária:")
for i in range(3):
    print(matriz_3x3[i][2-i], end=" ")
print()

# 16. Maior elemento de cada linha (Matriz 4x4)
matriz_4x4 = [[1, 9, 3, 4], [5, 2, 8, 1], [7, 6, 5, 9], [0, 1, 2, 3]]
print("\nMaior elemento de cada linha:")
for i, linha in enumerate(matriz_4x4):
    print(f"Linha {i+1}: {max(linha)}")

# 17. Contar pares e ímpares (Matriz 3x3)
pares = 0
impares = 0
for linha in matriz_3x3:
    for num in linha:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f"\nNa matriz, há {pares} números pares e {impares} números ímpares.")

# 18. Soma dos elementos acima da diagonal principal
soma_acima = 0
for i in range(3):
    for j in range(3):
        if j > i:
            soma_acima += matriz_3x3[i][j]
print(f"\nSoma dos elementos acima da diagonal principal: {soma_acima}")

# 19. Soma dos elementos abaixo da diagonal principal
soma_abaixo = 0
for i in range(3):
    for j in range(3):
        if i > j:
            soma_abaixo += matriz_3x3[i][j]
print(f"Soma dos elementos abaixo da diagonal principal: {soma_abaixo}")

# 20. Buscar número na matriz 3x3
num_procurado = int(input("\nDigite um número para buscar na matriz 3x3: "))
encontrado = False
for i in range(3):
    for j in range(3):
        if matriz_3x3[i][j] == num_procurado:
            print(f"Número {num_procurado} encontrado na posição: linha={i+1}, coluna={j+1}")
            encontrado = True
if not encontrado:
    print(f"O número {num_procurado} não foi encontrado na matriz.")