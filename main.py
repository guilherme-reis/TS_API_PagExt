import streamlit as st
import requests
import json

with st.form("my_form"):
    cnpjSh = st.text_input('CNPJ da Software House')
    tokenSh = st.text_input('Token da Software House')
    payercpfcnpj = st.text_input('CNPJ do Payer')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        url = "http://staging.pagamentobancario.com.br/api/v1/payer"
        # Cabeçalho requsição
        payload = ""
        headers = {
            "payercpfcnpj": payercpfcnpj,
            "tokenSh": tokenSh,
            "cnpjSh": cnpjSh,
            "Content-Type": "application/json",
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # Cabeçalho requsição
        teste_de_conexao = json.loads(response.text)

        if (teste_de_conexao.get("status")) == 1:
            st.success("Sucesso", "Autenticação realizada com sucesso")
            acesso= True
        else:
            st.error("Autenticação inválida! Confire as informações e tente novamente")


st.write("")
