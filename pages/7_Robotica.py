import streamlit as st

st.set_page_config(
    page_title="Equipe de Robótica IFMG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Equipe de Robótica do IFMG Campus Piumhi")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto de criação, desenvolvimento e consolidação da Equipe de Robótica do
IFMG Campus Piumhi teve como objetivo incentivar a educação tecnológica,
a inovação e o desenvolvimento de competências digitais entre estudantes e comunidade.

A iniciativa promoveu atividades práticas envolvendo robótica educacional,
programação, eletrônica, impressão 3D e participação em competições,
fortalecendo a formação acadêmica e aproximando a instituição das demandas
tecnológicas da sociedade.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Criar e consolidar uma equipe de robótica capaz de desenvolver projetos,
participar de competições tecnológicas e promover ações de extensão voltadas
à educação digital e inovação tecnológica.
""")

st.markdown("---")

st.header("🚀 Principais Atividades Desenvolvidas")

st.write("""
- Formação da equipe de robótica;
- Desenvolvimento de robôs para competições;
- Estudos de programação e eletrônica;
- Utilização de impressoras 3D;
- Desenvolvimento de protótipos tecnológicos;
- Participação em eventos e desafios de robótica;
- Capacitação dos estudantes em tecnologias digitais.
""")

st.markdown("---")

st.header("🖨️ Inovação e Tecnologia")

st.write("""
O projeto utilizou recursos do Ambiente de Inovação do IFMG,
incluindo impressoras 3D, equipamentos eletrônicos e softwares de programação.

Os participantes tiveram contato com tecnologias modernas que fazem parte
da transformação digital presente na indústria, na educação e na engenharia.
""")

st.markdown("---")

st.header("🏆 Resultados Alcançados")

st.write("""
- Formação da equipe de robótica do campus;
- Desenvolvimento de competências tecnológicas;
- Criação de protótipos e soluções inovadoras;
- Participação em competições e eventos;
- Ampliação da cultura de inovação no IFMG;
- Maior integração entre instituição e comunidade.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto contribuiu para despertar o interesse de estudantes e jovens
pelas áreas de ciência, tecnologia, engenharia e matemática.

Além disso, fortaleceu a inclusão digital e ampliou o acesso da comunidade
a conhecimentos tecnológicos que são cada vez mais valorizados no mercado de trabalho.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
Os estudantes puderam aplicar na prática conceitos relacionados à
programação, automação, eletrônica, modelagem 3D e trabalho em equipe.

A experiência proporcionou aprendizado além da sala de aula,
estimulando criatividade, resolução de problemas e pensamento inovador.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Ambiente de Inovação do IFMG
- Escolas da região
- Comunidade Local
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos dos robôs, competições, protótipos e atividades desenvolvidas pela equipe."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")