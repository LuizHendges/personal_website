import streamlit as st
from pathlib import Path

st.title("Todas as minhas aulas")

# Caminho da pasta aulas (um nível acima do script)
CAMINHO_ARQUIVO = Path(__file__).parent.parent / "aulas"

# Cria a pasta se não existir
CAMINHO_ARQUIVO.mkdir(parents=True, exist_ok=True)

# Lista todos os arquivos com as extensões desejadas
arquivos = sorted(
    [arquivo for arquivo in CAMINHO_ARQUIVO.iterdir()
     if arquivo.is_file() and arquivo.suffix in {".py", ".txt", ".ipynb"}],
    key=lambda x: x.stat().st_mtime,  # ordena por data de modificação
    reverse=True
)

if not arquivos:
    st.warning("Ainda não tem nenhuma aula na pasta 'aulas'.")
else:
    for arquivo in arquivos:  # agora 'arquivo' é um Path de verdade!
        nome = arquivo.stem.replace("_", " ").replace("-", " ").title()

        with st.expander(nome, expanded=False):
            try:
                conteudo = arquivo.read_text(encoding="utf-8")

                if arquivo.suffix == ".py":
                    st.code(conteudo, language="python")
                elif arquivo.suffix == ".ipynb":
                    st.info("Jupyter Notebook detectado")
                    preview = conteudo[:3000]
                    st.code(
                        preview + "\n\n... (notebook cortado para preview)", language="json")
                else:
                    st.code(conteudo, language="text")

            except Exception as e:
                st.error(f"Erro ao ler {arquivo.name}")
                st.exception(e)  # mostra o erro completo (bom pra debug)
