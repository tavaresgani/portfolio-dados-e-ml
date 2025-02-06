import streamlit as st
import pandas as pd

st.set_page_config(layout="wide") #ocupar a tela toda


df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books =  df_top100_books["book title"].unique() #uma lista com os nomes dos livros

#caixa de seleção dos livros
book = st.sidebar.selectbox("Books", books)

# Filtro selecionando o livro de acordo com a caixa de seleção
df_book = df_top100_books[df_top100_books["book title"] == book]
#mostrando o review de acordo com o livro selecionado
df_reviews_f = df_reviews[df_reviews["book name"] == book]


book_title = df_book["book title"].iloc[0] #trazendo apenas o titulo
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

#Adicionando titulo e subtitulo com streamlit
st.title(book_title)
st.subheader(book_genre)

#Dividindo a tela em 3 colunas com preço avaliação e ano
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

#Linha imaginária
st.divider()

#Exibindo as avaliações com as notas 
for row in df_reviews_f.values:
     message = st.chat_message(f"{row[4]}") #nota
     message.write(f"**{row[2]}**") #avaliação em negrito
     message.write(row[5])
