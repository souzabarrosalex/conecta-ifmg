import streamlit as st

st.markdown("""
<style>

.stButton > button {
    background-color: #198754;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #146C43;
    color: white;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Conecta IFMG",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Conecta IFMG")

st.subheader(
    "Conectando conhecimento, inovação e desenvolvimento para transformar comunidades."
)

st.image("assets/banner.jpg", use_container_width=True)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Projetos", "9")

with col2:
    st.metric("Alunos", "150+")

with col3:
    st.metric("Parceiros", "12")

with col4:
    st.metric("Impactados", "1000+")

st.markdown("---")

st.header("Nossos Projetos")

st.markdown("---")

st.subheader("🏙️ Plano Diretor de Piumhi")

st.write("""
Revisão e atualização do Plano Diretor Municipal,
promovendo desenvolvimento urbano sustentável.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="plano_diretor",
    use_container_width=True
):
    st.switch_page("pages/7_plano_diretor.py")

st.markdown("---")

st.subheader("♻️ Plano de Gerenciamento de Resíduos Sólidos")

st.write("""
Desenvolvimento de estratégias para gestão sustentável
dos resíduos sólidos do município.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Residuos_solidos",
    use_container_width=True
):
    st.switch_page("pages/7_Residuos_solidos.py")


st.markdown("---")

st.subheader("🌳 Revitalização do Parque da Mina")

st.write("""
Projeto de revitalização urbana com áreas de lazer,
academia ao ar livre e espaços de convivência.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Parque_mina",
    use_container_width=True
):
    st.switch_page("pages/7_Parque_mina.py")

st.markdown("---")

st.subheader("🏗️ Patologia das Construções")

st.write("""
Capacitação da comunidade para identificação,
prevenção e correção de patologias construtivas.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Patologias",
    use_container_width=True
):
    st.switch_page("pages/7_Patologias.py")


st.markdown("---")

st.subheader("⚡ Leitura de Projetos Elétricos")

st.write("""
Formação profissional voltada para interpretação
e leitura de projetos elétricos.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Eletricos",
    use_container_width=True
):
    st.switch_page("pages/7_Eletricos.py")

st.markdown("---")

st.subheader("🦺 Noções Básicas de Segurança do Trabalho")

st.write("""
Capacitação em normas regulamentadoras,
prevenção de acidentes e segurança ocupacional.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Seguranca",
    use_container_width=True
):
    st.switch_page("pages/7_Seguranca.py")

st.markdown("---")

st.subheader("🥽 Óculos de Realidade Virtual")

st.write("""
Aplicação de tecnologias imersivas na Engenharia Civil,
permitindo visualização virtual de projetos.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Realidade_virtual",
    use_container_width=True
):
    st.switch_page("pages/7_Realidade_virtual.py")

st.markdown("---")

st.subheader("🤖 Equipe de Robótica")

st.write("""
Criação e fortalecimento da equipe de robótica,
promovendo inovação e educação tecnológica.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Robotica",
    use_container_width=True
):
    st.switch_page("pages/7_Robotica.py")

st.markdown("---")

st.subheader("🚀 I Desafio de Inovação")

st.write("""
Evento extensionista voltado ao empreendedorismo,
criatividade e soluções inovadoras para a sociedade.
""")

if st.button(
    "📖 Ver Projeto Completo",
    key="Desafio_inovacao",
    use_container_width=True
):
    st.switch_page("pages/7_Desafio_inovacao.py")



col1, col2, col3 = st.columns(3)

st.markdown("---")

st.success(
    "Utilize o menu lateral para navegar pelas áreas do portal."
)