import streamlit as st 
###COLOCA UM TITULO

st.title("Carros de aluguel")


st.write ("Bem vindo!🚗⭐")
###ESCREVE

st.sidebar.title("MENU")
###CRIA UMA BARRA LATERAL

###CRIANDO A LISTA DE NOMES 
nomes = ["BMW X6M", "Altezza", "Nissan Gtr R35", "Omega", "Monza", "civic g10", "M3 V10"]


###COLOCA FOTO / VIDEO NO SITE
st.sidebar.image("logo.png", width=150)


###CRIANDO A LISTA
opcao = st.sidebar.selectbox("Escolha um carro:",nomes)


###--------------------------------------pricipal
st.title("leonardo aluga, aluguel de carro!!")
st.image(f'{opcao}.png')
st.markdown(f'##Voce alugou o modelo: {opcao}')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')


### Copia daqui pra frente --- Define a diária
if opcao == 'BMW X6M':
    diaria = 1200

elif opcao == 'Altezza':
    diaria = 800


elif opcao == 'Nissan Gtr R35':
    diaria = 1400


elif opcao == 'Omega':
    diaria = 230


elif opcao == 'Monza':
    diaria = 200


elif opcao == 'civic g10':
    diaria = 450


elif opcao == 'M3 v10':
    diaria = 1370

### calcular

if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'voce alugou o {opcao} por {dias} e rodou {km}, O valor total a pagar é R${aluguel_total:.2f}')

