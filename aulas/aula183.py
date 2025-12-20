"""
Aula: string.Template
Documentação: https://docs.python.org/3/library/string.html#template-strings

Nesta aula vemos como usar string.Template para substituir variáveis em textos.
Principais métodos:
- substitute: substitui valores e lança erro se faltar alguma variável
- safe_substitute: substitui valores e NÃO lança erro se faltar algo

Também é possível criar subclasses personalizadas e trocar o delimitador.
"""

import json
import string
import locale
from datetime import datetime
from pathlib import Path

# Caminho do arquivo externo usado como template
CAMINHO_ARQUIVO = Path(__file__).parent / "aula183.txt"

# Ajusta locale do sistema para formatação de moeda BR
locale.setlocale(locale.LC_ALL, "")


# -------------------------------------------------------------------------
# Função para converter número para formato monetário brasileiro
# -------------------------------------------------------------------------
def converte_para_br(numero: float | int) -> str:
    """
    Converte valores numéricos para formato BRL.
    Ex.: 12345 -> "R$ 12.345,00"
    """
    brl = "R$ " + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


# -------------------------------------------------------------------------
# Dados usados pelo template
# -------------------------------------------------------------------------
data = datetime(2025, 11, 27)
dados = dict(
    nome="João",
    valor=converte_para_br(1_234_456),
    data=data.strftime("%d/%m/%Y"),
    empresa="O. M.",
    telefone="+55 (48) 12345-1234",
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))


# -------------------------------------------------------------------------
# Exemplo de subclassing de Template (para trocar delimitador, etc.)
# -------------------------------------------------------------------------
class MyTemplate(string.Template):
    delimiter = "%"   # Corrigido: attributo correto é 'delimiter'


# -------------------------------------------------------------------------
# Lê o arquivo .txt (que contém placeholders como $nome, $valor, etc.)
# e faz a substituição usando string.Template
# -------------------------------------------------------------------------
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
    texto = f.read()
    template = string.Template(texto)

    # substitute -> lança erro se faltar uma chave no dicionário
    print(template.substitute(dados))

    # Caso queira evitar erros se faltar algo:
    # print(template.safe_substitute(dados))
