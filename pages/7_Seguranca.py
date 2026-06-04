import streamlit as st

st.set_page_config(
    page_title="Segurança do Trabalho",
    page_icon="🦺",
    layout="wide"
)

st.title("🦺 Curso FIC – Noções Básicas de Segurança do Trabalho")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto "Noções Básicas de Segurança do Trabalho" foi desenvolvido com o objetivo
de disseminar conhecimentos fundamentais sobre prevenção de acidentes,
identificação de riscos ocupacionais e promoção da cultura de segurança nos ambientes de trabalho.

A iniciativa proporcionou aos participantes uma formação introdutória sobre normas,
legislação e boas práticas relacionadas à saúde e segurança ocupacional,
contribuindo para a formação de profissionais mais conscientes e preparados.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Capacitar os participantes para compreender, identificar e aplicar conceitos
básicos de segurança do trabalho, promovendo a prevenção de acidentes
e a valorização da saúde nos ambientes profissionais.
""")

st.markdown("---")

st.header("📚 Conteúdos Abordados")

st.write("""
- Introdução à Segurança do Trabalho;
- Normas Regulamentadoras (NRs);
- Identificação de riscos ocupacionais;
- Equipamentos de Proteção Individual (EPIs);
- Equipamentos de Proteção Coletiva (EPCs);
- Prevenção de acidentes;
- Primeiros socorros;
- Saúde e bem-estar no ambiente de trabalho.
""")

st.markdown("---")

st.header("⚠️ Importância da Segurança do Trabalho")

st.write("""
A segurança do trabalho desempenha papel fundamental na proteção da vida,
na redução de acidentes e na promoção de ambientes laborais mais saudáveis.

O conhecimento das normas e procedimentos de segurança contribui para a prevenção
de riscos, redução de afastamentos e melhoria da qualidade de vida dos trabalhadores.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto proporcionou acesso gratuito a conhecimentos que podem ser aplicados
em diversas áreas profissionais, especialmente na construção civil,
indústria, comércio e prestação de serviços.

Os participantes passaram a compreender melhor a importância da prevenção,
da utilização correta dos equipamentos de proteção e do cumprimento das normas de segurança.
""")

st.markdown("---")

st.header("🏗️ Aplicação Prática")

st.write("""
Os conteúdos apresentados durante o curso foram relacionados a situações reais
encontradas nos ambientes de trabalho, permitindo que os participantes compreendessem
como aplicar os conceitos de segurança no dia a dia profissional.

Essa abordagem prática tornou o aprendizado mais eficiente e próximo da realidade do mercado.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
O projeto possibilitou aos estudantes envolvidos em sua execução aplicar conhecimentos
relacionados à Engenharia Civil, Segurança do Trabalho e Extensão Universitária.

A experiência fortaleceu competências como liderança, comunicação,
planejamento e responsabilidade social.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Capacitação de participantes em segurança do trabalho;
- Disseminação da cultura de prevenção;
- Ampliação da conscientização sobre riscos ocupacionais;
- Fortalecimento da relação entre IFMG e comunidade;
- Formação complementar para estudantes e trabalhadores;
- Promoção de ambientes de trabalho mais seguros.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Comunidade Local
- Participantes do Curso FIC
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos das aulas, atividades práticas, palestras, visitas técnicas e entrega de certificados."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")