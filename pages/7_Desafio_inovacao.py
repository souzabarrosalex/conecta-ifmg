import streamlit as st

st.set_page_config(
    page_title="I Desafio de Inovação",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 I Desafio de Inovação – Campus Piumhi")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O I Desafio de Inovação do Campus Piumhi foi uma iniciativa extensionista voltada
ao incentivo da criatividade, do empreendedorismo e da inovação tecnológica entre
os estudantes e a comunidade acadêmica.

O evento promoveu o desenvolvimento e a apresentação de ideias, produtos,
protótipos e soluções inovadoras para desafios relacionados à construção civil
e ao desenvolvimento tecnológico, estimulando a aplicação prática dos conhecimentos
adquiridos em sala de aula.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Estimular a inovação, o empreendedorismo e a criatividade dos participantes,
promovendo a busca por soluções inovadoras para desafios reais da sociedade
e do setor da construção civil.
""")

st.markdown("---")

st.header("💡 Temas Trabalhados")

st.write("""
- Inovação Tecnológica;
- Empreendedorismo;
- Desenvolvimento de Produtos;
- Soluções para Construção Civil;
- Sustentabilidade;
- Criatividade e Design;
- Desenvolvimento de Protótipos;
- Trabalho em Equipe.
""")

st.markdown("---")

st.header("🏗️ Desenvolvimento das Propostas")

st.write("""
Os participantes foram incentivados a identificar problemas e oportunidades
existentes no mercado, desenvolvendo propostas inovadoras capazes de gerar
impacto positivo para a sociedade.

As equipes elaboraram projetos, produtos e protótipos que posteriormente
foram apresentados e avaliados durante o evento.
""")

st.markdown("---")

st.header("🚀 Inovação e Empreendedorismo")

st.write("""
O projeto buscou despertar nos participantes uma visão empreendedora,
incentivando a criação de soluções que possam ser transformadas em produtos,
serviços ou oportunidades de negócio.

Além do conhecimento técnico, foram trabalhadas competências relacionadas
à liderança, criatividade, comunicação e resolução de problemas.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
A iniciativa fortaleceu a cultura da inovação no ambiente acadêmico,
aproximando estudantes dos desafios enfrentados pela sociedade e pelo mercado.

Ao estimular o desenvolvimento de soluções práticas, o projeto contribuiu
para a formação de profissionais mais preparados para atuar em cenários
cada vez mais dinâmicos e competitivos.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
O Desafio de Inovação proporcionou aos estudantes a oportunidade de aplicar
conhecimentos técnicos em situações reais, integrando teoria e prática.

A experiência fortaleceu habilidades fundamentais para a formação profissional,
como trabalho em equipe, pensamento crítico, criatividade e gestão de projetos.
""")

st.markdown("---")

st.header("🏆 Resultados Alcançados")

st.write("""
- Desenvolvimento de ideias inovadoras;
- Criação de protótipos e soluções tecnológicas;
- Estímulo ao empreendedorismo;
- Fortalecimento da cultura de inovação;
- Integração entre estudantes e comunidade;
- Aplicação prática dos conhecimentos acadêmicos.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Comunidade Acadêmica
- Estudantes Participantes
- Empresas e Profissionais Convidados
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos das apresentações, protótipos, equipes participantes e premiações do evento."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")