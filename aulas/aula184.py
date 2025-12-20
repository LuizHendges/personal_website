"""
Aula: Variáveis de ambiente com Python
Documentação: https://pypi.org/project/python-dotenv/

Nesta aula vemos como:
- Criar e usar variáveis de ambiente no Windows, Linux e Mac
- Ler variáveis com os.environ e os.getenv
- Utilizar o pacote python-dotenv para carregar dados do arquivo .env

IMPORTANTE:
Sempre crie um arquivo .env-example para servir como modelo no repositório.
"""

from dotenv import load_dotenv
import os

# ----------------------------------------------------------------------
# Carrega automaticamente as variáveis do arquivo .env
# ----------------------------------------------------------------------
load_dotenv()

# ----------------------------------------------------------------------
# Acessando variáveis de ambiente
# ----------------------------------------------------------------------
# os.environ["VAR"] -> lança erro se a variável não existir
# os.getenv("VAR")  -> retorna None se a variável não existir
#
# Exemplo:
#   BD_PASSWORD=123456  (no arquivo .env)
# ----------------------------------------------------------------------

senha = os.getenv("BD_PASSWORD")
print(senha)
