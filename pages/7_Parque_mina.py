import streamlit as st

st.set_page_config(
    page_title="Revitalização do Parque da Mina",
    page_icon="🌳",
    layout="wide"
)

st.title("🌳 Revitalização do Parque da Mina – Piumhi/MG")

st.success("Status: Projeto Finalizado")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto Revitalização do Parque da Mina tem como objetivo promover melhorias
em um dos mais importantes espaços públicos de lazer e convivência do município
de Piumhi. A iniciativa busca transformar o parque em um ambiente mais seguro,
acessível e atrativo para a população, por meio da implantação de novas áreas
de lazer, equipamentos esportivos, espaços de convivência e melhorias na infraestrutura.

O projeto integra conhecimentos da Engenharia Civil com demandas sociais,
ambientais e urbanísticas, fortalecendo a relação entre o IFMG e a comunidade.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Promover a revitalização do Parque da Mina através da implantação de estruturas
que incentivem o lazer, a prática esportiva, a convivência social e a valorização
dos espaços públicos do município.
""")

st.markdown("---")

st.header("🏗️ Principais Ações")

st.write("""
- Implantação de áreas de convivência;
- Construção de quiosques;
- Instalação de academias ao ar livre;
- Instalação de bebedouros;
- Implantação de brinquedos infantis;
- Utilização de brinquedos produzidos com materiais recicláveis;
- Melhoria da infraestrutura do parque;
- Incentivo à educação ambiental.
""")

st.markdown("---")

st.header("🌱 Sustentabilidade")

st.write("""
Um dos diferenciais do projeto é a utilização de materiais recicláveis
na construção de brinquedos e equipamentos de lazer, promovendo a conscientização
ambiental e incentivando práticas sustentáveis junto à comunidade.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
A revitalização do Parque da Mina proporcionará benefícios diretos para crianças,
jovens, adultos e idosos, oferecendo um ambiente adequado para atividades físicas,
recreação, integração social e contato com a natureza.

Além disso, o projeto contribui para a valorização dos espaços públicos,
o fortalecimento do turismo local e a melhoria da qualidade de vida da população.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Aumento da utilização do parque pela população;
- Ampliação das opções de lazer do município;
- Incentivo à prática esportiva;
- Melhoria da qualidade de vida da comunidade;
- Fortalecimento da educação ambiental;
- Valorização do patrimônio público;
- Integração entre IFMG e sociedade.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Prefeitura Municipal de Piumhi
- Comunidade Local
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos do parque, levantamentos realizados e propostas de revitalização."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")