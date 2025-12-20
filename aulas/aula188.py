"""
Aula: argparse.ArgumentParser
Documentação: https://docs.python.org/pt-br/3/howto/argparse.html

Nesta aula vemos como criar argumentos de linha de comando mais estruturados
e profissionais usando argparse.

Principais recursos mostrados:
- ArgumentParser(): cria o parser de argumentos
- add_argument(): define opções e parâmetros
- flags curtas (-b) e longas (--basic)
- help: mensagem exibida com --help
- metavar: nome exibido no uso
- action='append': permite passar o argumento várias vezes
  Ex.: python arquivo.py -b valor1 -b valor2
- parse_args(): interpreta os argumentos informados no terminal

Diferente de sys.argv, argparse:
- valida automaticamente
- cria mensagens de erro amigáveis
- gera automaticamente o --help
"""

# argparse.ArgumentParser para argumentos mais complexos

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,  # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo',  # Valor padrão
    required=False,
    action='append'  # Permite usar o argumento mais de uma vez
    # nargs='+'  # Permite passar vários valores de uma vez
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de -b/--basic.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)
