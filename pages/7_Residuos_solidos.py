import streamlit as st

st.set_page_config(
    page_title="Plano de Gerenciamento de Resíduos Sólidos",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ Plano de Gerenciamento de Resíduos Sólidos de Piumhi")

st.success("Status: Projeto Finalizado")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O Plano de Gerenciamento de Resíduos Sólidos foi desenvolvido com o objetivo
de contribuir para a melhoria das políticas públicas relacionadas ao manejo,
tratamento e destinação adequada dos resíduos gerados no município de Piumhi.

O projeto envolveu estudos técnicos, levantamento de informações e análise
das necessidades locais, buscando propor soluções sustentáveis que promovam
a preservação ambiental, a saúde pública e o desenvolvimento sustentável do município.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Auxiliar o município na elaboração de diretrizes e estratégias para a gestão
eficiente dos resíduos sólidos, promovendo sustentabilidade ambiental,
cumprimento da legislação vigente e melhoria da qualidade de vida da população.
""")

st.markdown("---")

st.header("🏗️ Principais Atividades Desenvolvidas")

st.write("""
- Levantamento de dados sobre resíduos sólidos;
- Diagnóstico da situação municipal;
- Estudo da legislação aplicável;
- Identificação de oportunidades de melhoria;
- Proposição de ações sustentáveis;
- Desenvolvimento de diretrizes para gestão ambiental;
- Apoio técnico ao planejamento municipal.
""")

st.markdown("---")

st.header("🌱 Sustentabilidade")

st.write("""
O projeto está diretamente alinhado aos princípios da sustentabilidade,
promovendo o uso responsável dos recursos naturais, a redução dos impactos
ambientais e a conscientização sobre a importância da gestão adequada dos resíduos.

As propostas desenvolvidas contribuem para a construção de um município mais
limpo, saudável e ambientalmente responsável.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
Os benefícios do projeto alcançam toda a população do município,
uma vez que a correta gestão dos resíduos sólidos está diretamente relacionada
à saúde pública, à preservação ambiental e à qualidade de vida.

Além disso, o projeto fortalece as condições necessárias para que o município
tenha acesso a programas e recursos voltados para o saneamento e a sustentabilidade.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Diagnóstico da situação dos resíduos sólidos do município;
- Identificação de necessidades e oportunidades de melhoria;
- Apoio técnico ao planejamento ambiental municipal;
- Fortalecimento das ações de sustentabilidade;
- Integração entre IFMG e poder público;
- Formação prática dos estudantes envolvidos.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
O projeto permitiu aos estudantes aplicar conhecimentos de Engenharia Civil,
Saneamento, Gestão Ambiental e Planejamento Urbano em uma situação real,
aproximando a formação acadêmica das demandas da sociedade.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Prefeitura Municipal de Piumhi
- Secretaria Municipal de Meio Ambiente
- Comunidade Local
""")

st.markdown("---")

st.header("📸 Registro do Projeto")

st.info(
    "Espaço reservado para fotos, relatórios, mapas e documentos produzidos durante o projeto."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")