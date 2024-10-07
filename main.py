import streamlit as st
import requests


# criando uma funçao
def busca_letra (banda, musica):
    #recebe um Endpoint, adicionar o f de função
    url = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response= requests.get(url)
    letra =response.json()['lyrics'] if response.status_code ==200 else ""
    return letra

# Adiciona um título (opcional)
#st.title('Minha Visão', ' escolha uma musica')

#st.title() para desenvolvimento

# Exibe a imagem
st.image('WhatsApp.jpeg')

#criando variaveis
banda=st.text_input("digite o nome de uma banda", key = "banda")
musica=st.text_input("digite o nome de uma musica", key = "musica")

pesquisar=st.button("Pesquisar") #criando um botão

if pesquisar:
    letra= busca_letra(banda,musica)
    if letra:
        st.success("Encontramos a letra da sua musica")
        st.text(letra)
    else:
        st.error("não foi possivel achar essa letra")