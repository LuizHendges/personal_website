"""
Aula: Módulo secrets

Geração de números aleatórios seguros em Python.

Este arquivo faz parte das minhas aulas pessoais.
"""

import secrets

# Criando uma instância segura de gerador aleatório
random = secrets.SystemRandom()

# -----------------------------------------------------------------------------
# randrange(inicio, fim, passo)
# -> Gera um inteiro aleatório dentro de um intervalo específico,
#    seguindo o passo definido.
# -----------------------------------------------------------------------------
r_range = random.randrange(10, 20, 2)
print("randrange:", r_range)

# -----------------------------------------------------------------------------
# randint(inicio, fim)
# -> Gera um inteiro aleatório dentro de um intervalo,
#    incluindo início e fim.
# -----------------------------------------------------------------------------
r_int = random.randint(10, 20)
print("randint:", r_int)

# -----------------------------------------------------------------------------
# uniform(inicio, fim)
# -> Gera um número flutuante aleatório dentro do intervalo.
# -----------------------------------------------------------------------------
r_uniform = random.uniform(10, 20)
print("uniform:", r_uniform)

# -----------------------------------------------------------------------------
# shuffle(lista_mutável)
# -> Embaralha a lista original (modifica in-place)
# -----------------------------------------------------------------------------
nomes = ["Luiz", "Maria", "Helena", "Joana"]
# random.shuffle(nomes)
print("lista original:", nomes)

# -----------------------------------------------------------------------------
# sample(iterável, k=N)
# -> Retorna NOVA lista com N itens selecionados aleatoriamente,
#    SEM repetição.
# -----------------------------------------------------------------------------
novos_nomes = random.sample(nomes, k=3)
print("sample - original:", nomes)
print("sample - novo:", novos_nomes)

# -----------------------------------------------------------------------------
# choices(iterável, k=N)
# -> Retorna nova lista com N itens escolhidos,
#    podendo repetir elementos.
# -----------------------------------------------------------------------------
novos_nomes = random.choices(nomes, k=3)
print("choices - original:", nomes)
print("choices - novo:", novos_nomes)

# -----------------------------------------------------------------------------
# choice(iterável)
# -> Retorna UM elemento aleatório.
# -----------------------------------------------------------------------------
print("choice:", random.choice(nomes))
