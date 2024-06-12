#calculadora básica streamlit

import streamlit as st

st.title("Calculadora")

numero1 = st.number_input("Dígite um número")

numero2 = st.number_input("Dígite outro número")

operacao = st.selectbox("Escolha a operação (+, -, *, /, **, root): ", ("+", "-", "*", "/", "**", "root"))

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 == 0:
        resultado = "Não é possível dividir por 0"
        st.error(resultado)
    else: 
        resultado = numero1 / numero2

elif operacao == "**":
    resultado = numero1 ** numero2

elif operacao == "root":
    if numero2%2==0 and numero1 <0:
        resultado = "não é póssivel raiz par de nº negativo"
        st.error(resultado)
    else:    
        resultado = numero1 ** (1/numero2)

st.write(resultado)