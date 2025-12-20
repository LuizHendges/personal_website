"""
Aula: sys.argv
Documentação: https://docs.python.org/3/library/sys.html#sys.argv

Nesta aula vemos como acessar argumentos passados ao executar um script Python.
Principais pontos:
- sys.argv contém todos os argumentos no momento da execução
- O índice 0 é sempre o nome do arquivo
- Os demais índices são os argumentos fornecidos no terminal
- É importante tratar erros como IndexError ao acessar posições específicas

Exemplo de uso no terminal:
python arquivo.py valor1 valor2 valor3
"""

# sys.argv - Executando arquivos com argumentos no sistema

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos: {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
