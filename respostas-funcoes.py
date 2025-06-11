import math
from dataclasses import dataclass, field
from typing import List

# 1. Produto Simples
@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int

# Instância para o exercício 1
produto_exemplo = Produto(nome="Notebook", preco=3500.50, quantidade=10)
# print(produto_exemplo)

# 2. Exibindo um Livro
@dataclass
class Livro:
    titulo: str
    autor: str
    ano_publicacao: int

def descrever_livro(livro: Livro):
    print(f'O livro "{livro.titulo}" foi escrito por {livro.autor} e publicado em {livro.ano_publicacao}.')

# livro_teste = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
# descrever_livro(livro_teste)

# 3. Calculando Idade
@dataclass
class Usuario:
    nome: str
    ano_nascimento: int

def calcular_idade(usuario: Usuario, ano_atual: int) -> int:
    return ano_atual - usuario.ano_nascimento

# usuario_teste = Usuario("Ana", 1995)
# print(f"{usuario_teste.nome} tem {calcular_idade(usuario_teste, 2024)} anos.")

# 4. Círculo
@dataclass
class Circulo:
    raio: float

def calcular_area(circulo: Circulo) -> float:
    return math.pi * (circulo.raio ** 2)

# circulo_teste = Circulo(raio=5.0)
# print(f"A área do círculo é: {calcular_area(circulo_teste):.2f}")

# 5. Ponto no Plano
@dataclass
class Ponto:
    x: float
    y: float

ponto_origem = Ponto(x=0, y=0)
# print(f"Ponto na origem: {ponto_origem}")

# 6. Retângulo
@dataclass
class Retangulo:
    base: float
    altura: float

def calcular_perimetro(retangulo: Retangulo) -> float:
    return 2 * (retangulo.base + retangulo.altura)

# retangulo_teste = Retangulo(10, 5)
# print(f"O perímetro do retângulo é: {calcular_perimetro(retangulo_teste)}")

# 7. Estoque de Produto
def valor_total_estoque(produto: Produto) -> float:
    return produto.preco * produto.quantidade

# print(f"Valor total em estoque do {produto_exemplo.nome}: R${valor_total_estoque(produto_exemplo):.2f}")

# 8. Distância entre Pontos
def calcular_distancia(p1: Ponto, p2: Ponto) -> float:
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# ponto_a = Ponto(3, 4)
# ponto_b = Ponto(0, 0)
# print(f"A distância entre os pontos é: {calcular_distancia(ponto_a, ponto_b):.2f}")

# 9. Comparando Produtos
def produto_mais_caro(p1: Produto, p2: Produto) -> str:
    if p1.preco > p2.preco:
        return p1.nome
    elif p2.preco > p1.preco:
        return p2.nome
    return "Ambos têm o mesmo preço"

# produto1 = Produto("Celular", 2000.0, 5)
# produto2 = Produto("Tablet", 2500.0, 3)
# print(f"O produto mais caro é: {produto_mais_caro(produto1, produto2)}")

# 10. Lista de Compras
@dataclass
class ItemCompra:
    nome_produto: str
    valor: float

def custo_total(itens: List[ItemCompra]) -> float:
    return sum(item.valor for item in itens)

# lista_de_compras = [
#     ItemCompra("Arroz", 25.50),
#     ItemCompra("Feijão", 8.90),
#     ItemCompra("Carne", 45.00)
# ]
# print(f"Custo total da compra: R${custo_total(lista_de_compras):.2f}")

# 11. Aluno e Notas
@dataclass
class Aluno:
    nome: str
    notas: List[float]

def calcular_media(aluno: Aluno) -> float:
    if not aluno.notas:
        return 0.0
    return sum(aluno.notas) / len(aluno.notas)

# aluno1 = Aluno("Marcos", [8.5, 9.0, 7.5, 10.0])
# print(f"A média de {aluno1.nome} é: {calcular_media(aluno1):.1f}")

# 12. Atualizar Preço
from dataclasses import replace

def aumentar_preco_percentual(produto: Produto, percentual: float) -> Produto:
    novo_preco = produto.preco * (1 + percentual / 100)
    return replace(produto, preco=round(novo_preco, 2))

# produto_original = Produto("Mouse", 80.0, 50)
# produto_atualizado = aumentar_preco_percentual(produto_original, 15)
# print(f"Produto Original: {produto_original}")
# print(f"Produto com Aumento: {produto_atualizado}")

# 13. Filtrando Livros por Autor
def livros_do_autor(lista_livros: List[Livro], autor: str) -> List[Livro]:
    return [livro for livro in lista_livros if livro.autor == autor]

# livros = [
#     Livro("Duna", "Frank Herbert", 1965),
#     Livro("O Messias de Duna", "Frank Herbert", 1969),
#     Livro("Neuromancer", "William Gibson", 1984)
# ]
# livros_herbert = livros_do_autor(livros, "Frank Herbert")
# for livro in livros_herbert:
#     print(livro.titulo)

# 14. Verificar Status da Conta
@dataclass
class ContaBancaria:
    titular: str
    saldo: float
    limite: float = 500.0

def pode_sacar(conta: ContaBancaria, valor_saque: float) -> bool:
    return (conta.saldo + conta.limite) >= valor_saque

# conta_cliente = ContaBancaria("Carlos", 1000.0)
# print(f"Pode sacar R$1200? {pode_sacar(conta_cliente, 1200.0)}") # True
# print(f"Pode sacar R$1600? {pode_sacar(conta_cliente, 1600.0)}") # False

# 15. Gerenciando um Time
@dataclass
class Jogador:
    nome: str
    posicao: str
    habilidade: int # 0-100

@dataclass
class Time:
    nome_time: str
    jogadores: List[Jogador]

def habilidade_media_time(time: Time) -> float:
    if not time.jogadores:
        return 0.0
    total_habilidade = sum(jogador.habilidade for jogador in time.jogadores)
    return total_habilidade / len(time.jogadores)

# time_exemplo = Time("Os Invencíveis", [
#     Jogador("Ronaldo", "Atacante", 95),
#     Jogador("Zidane", "Meio-campo", 92),
#     Jogador("Maldini", "Defensor", 88)
# ])
# print(f"Habilidade média do time '{time_exemplo.nome_time}': {habilidade_media_time(time_exemplo):.2f}")

# 16. Carrinho de Compras
@dataclass
class ItemCarrinho:
    produto: Produto
    quantidade: int

def calcular_total_carrinho(carrinho: List[ItemCarrinho]) -> float:
    total = 0.0
    for item in carrinho:
        total += item.produto.preco * item.quantidade
    return total

# p1 = Produto("Fone de Ouvido", 150.0, 10)
# p2 = Produto("Teclado Mecânico", 350.0, 5)
# carrinho = [ItemCarrinho(p1, 2), ItemCarrinho(p2, 1)]
# print(f"Valor total do carrinho: R${calcular_total_carrinho(carrinho):.2f}")

# 17. Ordenando Alunos por Média
def ordenar_alunos_por_media(alunos: List[Aluno]) -> List[Aluno]:
    return sorted(alunos, key=calcular_media, reverse=True)

# aluno_a = Aluno("João", [7, 8, 9])       # Média 8.0
# aluno_b = Aluno("Maria", [10, 9.5, 9]) # Média 9.5
# aluno_c = Aluno("Pedro", [6, 7, 6.5])    # Média 6.5
# alunos_ordenados = ordenar_alunos_por_media([aluno_a, aluno_b, aluno_c])
# for aluno in alunos_ordenados:
#     print(f"{aluno.nome}: Média {calcular_media(aluno):.1f}")

# 18. Funcionários e Departamentos
@dataclass
class Funcionario:
    id: int
    nome: str
    salario: float

@dataclass
class Departamento:
    nome_depto: str
    funcionarios: List[Funcionario]

def salario_medio_departamento(depto: Departamento) -> float:
    if not depto.funcionarios:
        return 0.0
    soma_salarios = sum(f.salario for f in depto.funcionarios)
    return soma_salarios / len(depto.funcionarios)

# depto_ti = Departamento("Tecnologia", [
#     Funcionario(101, "Alice", 7000),
#     Funcionario(102, "Bob", 8500),
#     Funcionario(103, "Charlie", 6500)
# ])
# print(f"Salário médio do depto '{depto_ti.nome_depto}': R${salario_medio_departamento(depto_ti):.2f}")

# 19. Transferência Bancária
def transferir(origem: ContaBancaria, destino: ContaBancaria, valor: float) -> bool:
    if valor > 0 and origem.saldo >= valor:
        origem.saldo -= valor
        destino.saldo += valor
        return True
    return False

# conta1 = ContaBancaria("Júlia", 2000.0)
# conta2 = ContaBancaria("Lucas", 500.0)
# print(f"Antes: Conta1={conta1.saldo}, Conta2={conta2.saldo}")
# sucesso = transferir(conta1, conta2, 300.0)
# print(f"Transferência bem-sucedida? {sucesso}")
# print(f"Depois: Conta1={conta1.saldo}, Conta2={conta2.saldo}")


# 20. Validação de Dados com __post_init__
@dataclass
class Evento:
    nome: str
    dia: int
    mes: int

    def __post_init__(self):
        if not (1 <= self.dia <= 31):
            raise ValueError("Dia deve estar entre 1 e 31")
        if not (1 <= self.mes <= 12):
            raise ValueError("Mês deve estar entre 1 e 12")

def formatar_data_evento(evento: Evento) -> str:
    return f'"{evento.nome}" acontecerá em {evento.dia:02d}/{evento.mes:02d}.'

# try:
#     evento_valido = Evento("Festa Junina", 24, 6)
#     print(formatar_data_evento(evento_valido))
#     evento_invalido = Evento("Festa Fim de Ano", 32, 12)
# except ValueError as e:
#     print(f"Erro ao criar evento: {e}")