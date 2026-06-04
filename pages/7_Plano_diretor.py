import streamlit as st

st.set_page_config(
    page_title="Plano Diretor de Piumhi",
    page_icon="🏙️",
    layout="wide"
)

st.title("🏙️ Plano Diretor de Piumhi")

st.success("Status: Projeto Finalizado")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O Plano Diretor de Piumhi é o principal instrumento de planejamento urbano
e territorial do município. O projeto extensionista busca apoiar estudos,
levantamentos e propostas voltadas para o desenvolvimento sustentável,
a organização do crescimento urbano, a preservação ambiental e a melhoria
da qualidade de vida da população.

A iniciativa fortalece a parceria entre o IFMG Campus Piumhi e a Prefeitura
Municipal, aproximando a formação acadêmica das necessidades reais da cidade.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Contribuir para a revisão e atualização do Plano Diretor Municipal,
promovendo o desenvolvimento urbano sustentável e auxiliando o poder público
na tomada de decisões relacionadas ao crescimento da cidade.
""")

st.markdown("---")

st.header("🏗️ Áreas Envolvidas")

st.write("""
- Planejamento Urbano
- Mobilidade Urbana
- Habitação
- Saneamento Básico
- Desenvolvimento Econômico
- Meio Ambiente
- Gestão Pública
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto beneficia diretamente toda a população de Piumhi,
fornecendo informações técnicas que auxiliam na construção
de uma cidade mais organizada, acessível, sustentável e preparada
para o futuro.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Apoio técnico ao município;
- Levantamento de demandas urbanas;
- Propostas de desenvolvimento sustentável;
- Fortalecimento da participação popular;
- Integração entre IFMG e Prefeitura;
- Contribuição para políticas públicas municipais.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Prefeitura Municipal de Piumhi
- Comunidade Local
""")

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")