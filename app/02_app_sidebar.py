import pandas as pd
import streamlit as st
import plotly.express as px

st.title('International Development: GDP & Life Expectancy Relationship')

df = pd.read_excel('../data/gampinder.xlsx')

with st.sidebar:
    year = st.selectbox('Seleccione un año', df.year.unique())

mask_year = df.year == year
df_year = df[mask_year]

fig = px.scatter(
    data_frame=df_year, x='gdpPercap', y='lifeExp', hover_name='country',
    color='continent', facet_col='continent', facet_col_wrap=3, size='pop')

st.plotly_chart(fig)
