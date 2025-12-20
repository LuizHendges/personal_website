import streamlit as st
from datetime import date
import os

st.set_page_config(
    page_title='Personal Website',
    page_icon='🖥️',
    layout='wide'
)

st.markdown('''
<style>
body, .stApp {
    background-color: #0F141A;
    color: #E3E3E3;
}

h1, h2, h3, h4 {
    color: #E8F1F2;
    font-weight: 700;
    letter-spacing: 0.5px;
}

strong, b {
    color: #3ACC6C;
}

a {
    color: #3ACC6C !important;
}
a:hover { text-decoration: underline; }

.stButton>button {
    background-color: #1A1F26;
    color: #E3E3E3;
    border-radius: 8px;
    border: 1px solid #2B333B;
}
.stButton>button:hover {
    border-color: #3ACC6C;
    color: #3ACC6C;
    transition: 0.2s ease-in-out;
}

.streamlit-expanderHeader {
    color: #E3E3E3;
    background-color: #141A21 !important;
    border-radius: 8px;
    border: 1px solid #2B333B;
}
.streamlit-expanderHeader:hover { border-color: #3ACC6C; }

.streamlit-expanderContent {
    background-color: #11161D !important;
    border-radius: 8px;
    border: 1px solid #2B333B;
    padding: 10px;
}

.stImage img {
    max-width: 200px !important;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.6);
}

div[data-testid="column"]:has(.stImage) {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
''', unsafe_allow_html=True)

col_title, col_image = st.columns([2, 1], vertical_alignment='top')

with col_title:
    st.title("Site Pessoal de Luiz Alberto")
    st.subheader("Bem-vindo!")
    st.write('Olá, eu sou **Luiz Alberto**👋')
    st.write(''' 
    Este site é o meu espaço para **aprender, praticar e compartilhar projetos em Python**.  
             
    Aqui você vai encontrar experimentos simples enquanto estudo programação. 
              
    A ideia é crescer aos poucos, e aprender criando.
    ''')

with col_image:
    st.image(
        'https://i.pinimg.com/736x/52/2a/d2/522ad20d57d874f903c39f511579d432.jpg'
    )


st.markdown('---')
st.caption('Feito com Streamlit • Atualizo toda vez que termino uma aula nova!')
