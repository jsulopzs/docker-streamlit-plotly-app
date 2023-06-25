import pandas as pd

df_countries = pd.read_excel('../data/gampinder.xlsx')

import plotly.express as px

import streamlit as st

with st.sidebar:
    year = st.selectbox(label='Select year', options=df_countries.year.unique())

mask_year = df_countries.year == year
df_year = df_countries[mask_year]

fig = px.scatter(
    data_frame=df_year, x='gdpPercap', y='lifeExp',
    color='continent', size='pop', hover_name='country')

st.plotly_chart(fig)