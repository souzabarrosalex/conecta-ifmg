import streamlit as st
import sqlite3

st.title("Cadastro de Demandas")

with st.form("demanda"):

    nome = st.text_input("Nome")

    email = st.text_input("Email")

    instituicao = st.text_input("Instituição")

    demanda = st.text_area("Descreva sua demanda")

    enviar = st.form_submit_button("Enviar")

if enviar:

    conn = sqlite3.connect("database/banco.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO demandas
        (nome,email,instituicao,demanda)
        VALUES (?,?,?,?)
    """,
    (nome,email,instituicao,demanda))

    conn.commit()
    conn.close()

    st.success("Demanda cadastrada com sucesso!")