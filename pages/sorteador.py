import streamlit as st
import random

st.title('Sorteador Número')

col1, col2 = st.columns(2)
with col1:
    minimo = st.number_input('Número mínimo', value=1)
with col2:
    maximo = st.number_input('Número máximo', value=100)

quantos = st.slider('Quantos números sortear?', 1, 20, 1)

if st.button('Sortear agora!', type='primary'):
    numeros = [random.randint(minimo, maximo) for _ in range(quantos)]
    st.success('Números sorteados:')
    st.write(' → '.join(map(str, numeros)))

    if quantos == 1:
        st.balloons()

st.markdown('---')

st.title('Sorteador Nomes')

col_inserir_nome, col_nomes_inseridos = st.columns([2, 2])

with col_inserir_nome:
    st.subheader("Adicionar nome")

    # Esse form é a mágica: Enter ou clique no botão funciona igual e limpa automático
    with st.form(key="form_nome", clear_on_submit=True):
        novo_nome = st.text_input(
            "Digite um nome e aperte Enter",
            placeholder="Ex: Luiz, Ana, João..."
        )
        botao = st.form_submit_button(
            "Adicionar nome",
            type="primary",
            use_container_width=True
        )

        # Quando aperta Enter ou clica no botão
        if botao or novo_nome:
            nome = novo_nome.strip()
            if nome:
                if "lista_nomes" not in st.session_state:
                    st.session_state.lista_nomes = []
                if nome not in st.session_state.lista_nomes:
                    st.session_state.lista_nomes.append(nome)
                    st.success(f"Adicionado: **{nome}**")
                    st.rerun()  # atualiza a lista do lado
            else:
                st.error("Digite um nome válido!")

with col_nomes_inseridos:
    st.subheader("Nomes na lista")
    if "lista_nomes" in st.session_state and st.session_state.lista_nomes:
        for i, nome in enumerate(st.session_state.lista_nomes, 1):
            st.write(f"{i}. **{nome}**")
        st.success(f"Total: **{len(st.session_state.lista_nomes)} nomes**")
    else:
        st.info("Nenhum nome adicionado ainda...")

if "lista_nomes" not in st.session_state:
    st.session_state.lista_nomes = []

nomes = st.session_state.lista_nomes

if len(nomes) <= 1:
    st.info("Adicione pelo menos dois nomes para poder sortear!")
else:
    st.markdown("---")
    st.subheader("Sortear nomes")

    # Garante que o slider nunca tenha min > max
    max_possible = len(nomes)
    quantos = st.slider(
        "Quantos nomes sortear?",
        min_value=1,
        max_value=max_possible,
        value=1 if max_possible >= 1 else 1,
        key="slider_quantos"  # chave única pra evitar conflitos
    )

    if st.button("SORTEAR AGORA!", type="primary", use_container_width=True):
        ganhadores = random.sample(nomes, quantos)
        st.balloons()

        st.markdown("### Resultado do sorteio:")
        for i, vencedor in enumerate(ganhadores, 1):
            st.markdown(f"""
            <div style="
                text-align: center;
                font-size: 2.8rem;
                padding: 25px;
                margin: 15px 0;
                background: linear-gradient(90deg, #1A1F26, #2B333B);
                border-radius: 20px;
                border: 3px solid #3ACC6C;
                color: #3ACC6C;
                font-weight: bold;
                box-shadow: 0 0 20px rgba(58, 204, 108, 0.3);
            ">
                {i}º → {vencedor.upper()}
            </div>
            """, unsafe_allow_html=True)

        if quantos == 1:
            st.success(f"O ganhador é: **{ganhadores[0]}**")

# Botão pra limpar tudo (opcional, mas útil)
if "lista_nomes" in st.session_state and st.session_state.lista_nomes:
    if st.button("Limpar todos os nomes"):
        st.session_state.lista_nomes = []
        st.rerun()
