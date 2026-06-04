import streamlit as st

st.set_page_config(
    page_title="Óculos de Realidade Virtual",
    page_icon="🥽",
    layout="wide"
)

st.title("🥽 Curso FIC – Óculos de Realidade Virtual")

st.success("✅ Projeto Concluído")

st.markdown("---")

st.header("📖 Resumo")

st.write("""
O projeto Curso FIC – Óculos de Realidade Virtual foi desenvolvido com o objetivo
de capacitar estudantes e membros da comunidade no uso de tecnologias imersivas
aplicadas à Engenharia Civil.

Por meio da utilização de óculos de realidade virtual, os participantes puderam
explorar ambientes digitais tridimensionais, visualizar projetos de construção
antes de sua execução e conhecer ferramentas inovadoras cada vez mais presentes
no mercado profissional.
""")

st.markdown("---")

st.header("🎯 Objetivo")

st.write("""
Promover a qualificação tecnológica dos participantes por meio da utilização
de óculos de realidade virtual como ferramenta de apoio à visualização,
análise e apresentação de projetos na área da Engenharia Civil.
""")

st.markdown("---")

st.header("🚀 Principais Atividades Desenvolvidas")

st.write("""
- Introdução aos conceitos de Realidade Virtual;
- Apresentação dos equipamentos utilizados;
- Demonstração de ambientes virtuais;
- Visualização de projetos arquitetônicos e estruturais;
- Aplicação da tecnologia na Engenharia Civil;
- Treinamento prático com os participantes;
- Discussão sobre tendências tecnológicas do mercado.
""")

st.markdown("---")

st.header("💡 Inovação Tecnológica")

st.write("""
A Realidade Virtual representa uma das tecnologias mais promissoras para o setor
da construção civil, permitindo que clientes, engenheiros e arquitetos visualizem
projetos de forma imersiva antes mesmo do início da obra.

Essa abordagem reduz erros de interpretação, melhora a comunicação entre as partes
envolvidas e auxilia na tomada de decisões durante o desenvolvimento dos projetos.
""")

st.markdown("---")

st.header("🏗️ Aplicações na Engenharia Civil")

st.write("""
- Visualização de projetos arquitetônicos;
- Apresentação de empreendimentos aos clientes;
- Compatibilização de projetos;
- Simulação de ambientes construídos;
- Planejamento e execução de obras;
- Treinamento técnico e educacional.
""")

st.markdown("---")

st.header("👥 Impacto para a Comunidade")

st.write("""
O projeto proporcionou acesso a uma tecnologia inovadora que normalmente não está
disponível para grande parte da população.

Além de ampliar o conhecimento tecnológico dos participantes, a iniciativa contribuiu
para aproximar a comunidade das transformações digitais que vêm ocorrendo no setor
da construção civil e em diversas áreas profissionais.
""")

st.markdown("---")

st.header("📚 Contribuição Acadêmica")

st.write("""
Os estudantes tiveram a oportunidade de aplicar conhecimentos relacionados
à modelagem digital, visualização de projetos e inovação tecnológica.

A experiência fortaleceu competências importantes para a formação profissional,
como criatividade, comunicação, resolução de problemas e adaptação às novas tecnologias.
""")

st.markdown("---")

st.header("✅ Resultados Alcançados")

st.write("""
- Capacitação dos participantes no uso da tecnologia;
- Disseminação de conhecimentos sobre Realidade Virtual;
- Aproximação da comunidade com tecnologias inovadoras;
- Ampliação das competências digitais dos estudantes;
- Fortalecimento da cultura de inovação no IFMG.
""")

st.markdown("---")

st.header("🤝 Parceiros")

st.write("""
- IFMG Campus Piumhi
- Ambiente de Inovação do IFMG
- Comunidade Acadêmica
- Participantes do Curso FIC
""")

st.markdown("---")

st.header("📸 Galeria do Projeto")

st.info(
    "Espaço reservado para fotos das atividades, equipamentos utilizados e participação dos alunos durante o curso."
)

st.markdown("---")

if st.button("⬅ Voltar para a Página Inicial"):
    st.switch_page("app.py")