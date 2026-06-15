import streamlit as st
import sqlite3

st.markdown("""
<div style="
    background: linear-gradient(90deg, #198754, #146C43);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
">
    <h1>📋 Cadastro de Demandas</h1>
    <p style="font-size:18px;">
        Conecte sua instituição ao IFMG e transforme necessidades reais
        em projetos de impacto para a comunidade.
    </p>
</div>
""", unsafe_allow_html=True)


st.write("""
Possui uma necessidade para sua instituição, empresa,
associação, escola ou comunidade?

Descreva sua demanda e ela poderá ser analisada para desenvolvimento
de futuros projetos extensionistas do IFMG Campus Piumhi.
""")

st.markdown("""
<div style="
    background-color:#f8f9fa;
    padding:20px;
    border-left:6px solid #198754;
    border-radius:10px;
    margin-bottom:20px;
">
    <h4>💡 Como funciona?</h4>
    <p>
    As demandas cadastradas são analisadas por professores e estudantes
    do IFMG Campus Piumhi e podem ser transformadas em projetos de extensão,
    cursos, pesquisas ou ações voltadas ao desenvolvimento local.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="
    background-color:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
">
""", unsafe_allow_html=True)

with st.form("demanda"):

    nome = st.text_input("👤 Nome do Responsável")

    instituicao = st.text_input("🏢 Instituição")

    telefone = st.text_input("📱 Telefone / WhatsApp")

    email = st.text_input("📧 E-mail")

    demanda = st.text_area(
        "📝 Descreva sua demanda",
        height=150,
        placeholder="Exemplo: Necessitamos de um estudo para revitalização de uma praça pública..."
    )

    enviar = st.form_submit_button(
        "📨 Enviar Demanda",
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

if enviar:

    if not nome or not instituicao or not telefone or not email or not demanda:

        st.error("⚠️ Preencha todos os campos obrigatórios.")

    else:

        conn = sqlite3.connect("database/banco.db")

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO demandas
            (nome,email,instituicao,demanda)
            VALUES (?,?,?,?)
        """,
        (nome,email,instituicao,demanda))

        conn.commit()
        conn.close()

        st.success(
            "✅ Demanda cadastrada com sucesso! Obrigado por contribuir com o desenvolvimento da comunidade."
        )

st.markdown("---")


st.markdown("""
<div style="
    background: linear-gradient(90deg,#198754,#146C43);
    color:white;
    padding:25px;
    border-radius:15px;
    margin-top:30px;
">

<h3>❓ Dúvidas? Entre em contato</h3>

<p>
<b>Profª Stella Gomes</b>
</p>

<p>
📧 assuntosinstitucionais.piumhi@ifmg.edu.br
</p>

<p>
💬 WhatsApp: (37) 3412-0791
</p>

</div>
""", unsafe_allow_html=True)