import streamlit as st

st.set_page_config(
    page_title="Patologia das Construções",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Patologia das Construções: Conhecimento e Prevenção de Problemas em Edificações")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto "Patologia das Construções: Conhecimento e Prevenção de Problemas em Edificações"
foi desenvolvido com o objetivo de disseminar conhecimentos sobre as principais manifestações
patológicas encontradas em edificações, suas causas, formas de prevenção e possíveis soluções.

A iniciativa aproximou a comunidade de conceitos técnicos importantes para a conservação,
segurança e durabilidade das construções, contribuindo para a valorização do patrimônio
edificado e para a redução de problemas construtivos.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Capacitar os participantes para identificar, compreender e prevenir problemas
construtivos comuns em edificações, promovendo maior conscientização sobre
manutenção preventiva e qualidade das construções.
""")

st.markdown("---")

st.header("📚 Conteúdos Abordados")

st.write("""
- Conceitos básicos de Patologia das Construções;
- Fissuras e trincas;
- Infiltrações e umidade;
- Desplacamento de revestimentos;
- Corrosão de armaduras;
- Falhas de execução;
- Manutenção preventiva;
- Diagnóstico e prevenção de patologias.
""")

st.markdown("---")

st.header("🏠 Principais Problemas Estudados")

st.write("""
Durante o projeto foram apresentados exemplos reais de problemas frequentemente
encontrados em residências, edifícios e obras de infraestrutura, permitindo que
os participantes compreendessem suas causas e consequências.

Também foram discutidas práticas que auxiliam na prevenção desses problemas
ainda durante as etapas de projeto, execução e manutenção das edificações.
""")

st.markdown("---")

st.header("🔍 Importância do Conhecimento Técnico")

st.write("""
Grande parte das manifestações patológicas pode ser evitada por meio de
planejamento adequado, execução correta dos serviços e manutenção periódica.

O conhecimento sobre esses problemas contribui para aumentar a vida útil
das construções, reduzir custos com reparos e garantir maior segurança
para os usuários das edificações.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto proporcionou à comunidade acesso a informações técnicas que normalmente
estão restritas ao ambiente profissional da Engenharia Civil.

Os participantes passaram a compreender melhor os sinais de deterioração
das edificações e a importância da manutenção preventiva para preservação
de seus imóveis.
""")

st.markdown("---")

st.header("🏗️ Aplicação Prática")

st.write("""
Os conteúdos foram apresentados por meio de exemplos reais, estudos de caso
e análises de situações frequentemente observadas em construções da região.

Essa abordagem permitiu uma melhor compreensão dos conceitos e facilitou
a aplicação dos conhecimentos adquiridos no dia a dia.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
O projeto possibilitou aos estudantes aplicar conhecimentos adquiridos durante
o curso de Engenharia Civil, fortalecendo competências relacionadas à análise,
diagnóstico e prevenção de problemas construtivos.

Além disso, promoveu a integração entre ensino, pesquisa e extensão,
aproximando a formação acadêmica das necessidades da sociedade.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Disseminação de conhecimentos sobre Patologia das Construções;
- Conscientização sobre manutenção preventiva;
- Aproximação entre IFMG e comunidade;
- Formação complementar dos participantes;
- Fortalecimento das ações de extensão universitária;
- Aplicação prática dos conhecimentos de Engenharia Civil.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Comunidade Local
- Participantes do Projeto
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos de estudos de caso, exemplos de patologias construtivas, visitas técnicas e atividades desenvolvidas durante o projeto."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")