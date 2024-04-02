import pandas as pd
import streamlit as st
import plotly.express as px

# Cabeçalho
st.header('CARS REPORT :car:', divider='rainbow')
#st.header("Stay :blue[UP TO DATE] with _Car Data_", text_size='small')
st.markdown("<p style='font-size: 1.3em;'>Gráficos interativos de um conjunto de dados sobre veículos nos EUA</p>", unsafe_allow_html=True)

# Dados
car_data = pd.read_csv('vehicles.csv')

st.header('Amostras do conjunto de dados', divider='rainbow')

# Separando colunas 'fabricante' e 'modelo'
split_model = car_data['model'].str.split(' ', n=1, expand=True)
if len(split_model.columns) == 2:  # Verificando
    car_data[['fabricante', 'modelo']] = split_model
else:
    print("A coluna 'model' não pode ser dividida em duas colunas separadas.")
car_data.head()

# Exibindo tabela com os dados
st.write(car_data)

# Gráfico de barras com plotly.express
st.header('Tipos de carro por fabricante', divider='rainbow')

# Construindo o gráfico de barras
fig_bar_type_fab = px.bar(car_data, x='fabricante', color='type', color_discrete_sequence=px.colors.qualitative.G10)
st.plotly_chart(fig_bar_type_fab)

# Histograma de comparação Condição x Ano
st.header('Histograma Condição x Ano', divider='rainbow')

build_histogram = st.button('Condição x Ano')
     
if build_histogram: # se o botão for clicado
    # escrever uma descição
    st.write('Comparação de Condição x Ano')
         
    # criar um histograma
    fig_hist2 = px.histogram(car_data, x="model_year", color='condition', color_discrete_sequence=px.colors.qualitative.G10)
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist2, use_container_width=True)

# Gráficos de dispersão Modelo x Preço
st.header('Gráficos de dispersão Modelo x Preço', divider='rainbow')

scatter_check= st.checkbox('Modelo x Preço')

if scatter_check: # se o botão for clicado
    # escrever uma descição
    st.write('Gráficos de dispersão Modelo x Preço')

    # criar um histograma
    fig_scatter1 = px.scatter(car_data, x="model", y="price")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter1, use_container_width=True)

# Diagrama de caixa Condição x Kilometragem
st.header('Diagrama de Caixa Condição x Kilometragem', divider='rainbow')

boxpplot_check= st.checkbox('Condição x Kilometragem')

if boxpplot_check: # se o botão for clicado
    # escrever uma descição
    st.write('Diagrama de Caixa Condição x Kilometragem')

    # Agrupando os dados
    avg_odometer_by_condition = car_data.groupby('condition')['odometer'].mean().reset_index()

    # Criando diagrama de caixa
    fig_cond_km = px.box(car_data, x='condition', y='odometer', color='condition', labels={'condition': 'Condição do Veículo', 'odometer': 'Quilometragem'})

    # Adicionar as médias da quilometragem ao gráfico
    for idx, row in avg_odometer_by_condition.iterrows():
        fig_cond_km.add_shape(type='line', xref='x', yref='y',
                      x0=row['condition'], y0=row['odometer'], 
                      x1=row['condition'], y1=row['odometer'],
                      line=dict(color='red', width=2))

    st.plotly_chart(fig_cond_km, use_container_width=True)

# Gráfico de barras Preços médios
st.header('Preços médios por tipo', divider='rainbow')

# Agrupando pelo fabricante, calculando a média do preço e redefinindo o índice
avg_price_km= car_data.groupby('type')['price'].mean().reset_index()

# Plotando o gráfico
fig_mean_km = px.bar(avg_price_km, x='type', y='price', labels={'fabricante': 'Fabricante', 'price': 'Preço Médio'}, color_discrete_sequence=px.colors.qualitative.Dark2)
st.plotly_chart(fig_mean_km)

#Gráfico de barrasPreços médios por fabricantes
st.header('Preços médios por fabricantes', divider='rainbow')

# Agrupando por fabricante e preço médio
avg_price_fab= car_data.groupby('fabricante')['price'].mean().reset_index()

fig_mean_fab = px.bar(avg_price_fab, x='fabricante', y='price', color='price', labels={'fabricante': 'Fabricante', 'price': 'Preço Médio'}, color_discrete_sequence=px.colors.qualitative.G10)
st.plotly_chart(fig_mean_fab)
