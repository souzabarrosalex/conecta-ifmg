import streamlit as st

st.set_page_config(
    page_title="Leitura de Projetos Elétricos",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Lendo o Futuro - Capacitação em Leitura de Projetos Elétricos")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto "Lendo o Futuro" foi desenvolvido com o objetivo de capacitar
jovens e adultos na leitura e interpretação de projetos elétricos,
oferecendo conhecimentos técnicos fundamentais para atuação no setor
da construção civil e instalações elétricas.

A iniciativa buscou ampliar oportunidades de qualificação profissional,
promovendo inclusão social e preparando os participantes para atender
às demandas do mercado de trabalho.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Capacitar os participantes na leitura e interpretação de projetos elétricos,
desenvolvendo competências técnicas que contribuam para sua inserção
e crescimento no mercado profissional.
""")

st.markdown("---")

st.header("📚 Conteúdos Abordados")

st.write("""
- Introdução aos projetos elétricos;
- Simbologia técnica;
- Interpretação de plantas elétricas;
- Circuitos elétricos residenciais;
- Normas técnicas aplicáveis;
- Segurança em instalações elétricas;
- Leitura de diagramas e esquemas elétricos.
""")

st.markdown("---")

st.header("⚡ Importância da Capacitação")

st.write("""
A correta interpretação de projetos elétricos é uma habilidade essencial
para profissionais da construção civil e da área elétrica.

O domínio dessas competências contribui para a execução segura das instalações,
redução de erros em obras e melhoria da qualidade dos serviços prestados.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto proporcionou acesso gratuito à qualificação técnica,
possibilitando que jovens e trabalhadores ampliassem seus conhecimentos
e aumentassem suas oportunidades de inserção no mercado de trabalho.

Além disso, fortaleceu a relação entre o IFMG e a comunidade local,
promovendo desenvolvimento social e profissional.
""")

st.markdown("---")

st.header("🏗️ Aplicação Prática")

st.write("""
Os participantes tiveram contato com situações reais encontradas
em obras e instalações elétricas, permitindo uma compreensão prática
dos conteúdos apresentados durante a capacitação.

O conhecimento adquirido pode ser aplicado em atividades profissionais,
empreendimentos próprios e projetos futuros.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
O projeto permitiu aos estudantes envolvidos na sua execução
aplicar conhecimentos da Engenharia Civil e áreas correlatas,
desenvolvendo habilidades de ensino, comunicação e extensão universitária.

A experiência fortaleceu a integração entre teoria e prática,
um dos pilares da formação profissional.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Capacitação técnica dos participantes;
- Ampliação das oportunidades de empregabilidade;
- Disseminação de conhecimentos sobre instalações elétricas;
- Aproximação entre IFMG e comunidade;
- Desenvolvimento de competências profissionais;
- Promoção da inclusão social através da educação.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Comunidade Local
- Participantes do Curso
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos das aulas, atividades práticas, materiais utilizados e certificados entregues aos participantes."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")