import streamlit as st #transforma scripts de dados em app web
import pandas as pd #organizar dados 
import plotly.express as px #plotar graficos

st.set_page_config(layout="wide") #ocupar a tela toda

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

### Criando os primeiros componentes 

price_max =  df_top100_books["book price"].max() #maior valor de todos os valores e retorna um unico valor
price_min =  df_top100_books["book price"].min()

#adicionando um slide com streamlit
max_price = st.sidebar.slider("Intervalo de Preço", price_min, price_max, price_max)

#pegar o df quando o preço for menor que o max_price do filtro, atualizar no dataframe
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

### Construindo os gráficos

#Gráfico de barra
fig = px.bar(df_books["year of publication"].value_counts())
#Histograma
fig2 = px.histogram(df_books["book price"])

#separando a tela em duas colunas
col1, col2 = st.columns(2)
#exibindo o gráfico
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
