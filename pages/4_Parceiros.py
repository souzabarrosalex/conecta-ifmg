parceiros = [
    ("IFMG Campus Piumhi", "assets/parceiros/ifmg.png"),
    ("Prefeitura de Piumhi", "assets/parceiros/prefeitura_piumhi.png"),
    ("Banco Sicoob", "assets/parceiros/sicoob.png"),
    ("Crea MG", "assets/parceiros/creaMG.png"),
    ("104 FM", "assets/parceiros/104fm.png"),

]

import streamlit as st

st.set_page_config(layout="wide")

st.title("🤝 Nossos Parceiros")

st.write("""
Instituições e empresas que caminham junto conosco na missão de
transformar conhecimento em soluções para o desenvolvimento de Piumhi e região.
""")

st.markdown("<br>", unsafe_allow_html=True)

parceiros = [
    {
        "nome": "IFMG Campus Piumhi",
        "logo": "assets/parceiros/ifmg.png"
    },
    {
        "nome": "Prefeitura de Piumhi",
        "logo": "assets/parceiros/prefeitura_piumhi.png"
    },
    {
        "nome": "Banco Sicoob",
        "logo": "assets/parceiros/sicoob.png"
    },
    {
        "nome": "CREA-MG",
        "logo": "assets/parceiros/creaMG.png"
    },
    {
        "nome": "104 FM",
        "logo": "assets/parceiros/104fm.png"
    }
]

# CSS
st.markdown("""
<style>

.card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    background-color: white;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.nome-parceiro{
    font-size:20px;
    font-weight:bold;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# Primeira linha
cols = st.columns(3)

for i in range(3):

    parceiro = parceiros[i]

    with cols[i]:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.image(parceiro["logo"], width=150)

        st.markdown(
            f'<div class="nome-parceiro">{parceiro["nome"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

# Segunda linha
cols = st.columns(3)

for i in range(3, len(parceiros)):

    parceiro = parceiros[i]

    with cols[(i-3)]:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.image(parceiro["logo"], width=150)

        st.markdown(
            f'<div class="nome-parceiro">{parceiro["nome"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.success("Sua instituição também pode fazer parte desta rede de transformação social.")

if st.button("Quero ser parceiro"):
    st.switch_page("pages/5_Participar.py")