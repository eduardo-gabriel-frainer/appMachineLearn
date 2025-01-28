import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

# Carrega os dados da tabela
df = pd.read_csv("pizzas.csv")

# Treina o modelo (Machine Learn)
modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

# Interação com o usuário atravez da tela
st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(
        f"O valor da Pizza com diâmetro de {diametro:.2f} cm "
        f"é de R${preco_previsto:.2f}."
    )
    st.balloons()
