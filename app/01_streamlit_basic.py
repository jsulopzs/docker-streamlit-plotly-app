import pandas as pd

df_countries = pd.read_excel('../data/gampinder.xlsx')

import plotly.express as px

mask_year = df_countries.year == 2007
df_year = df_countries[mask_year]

fig = px.scatter(
    data_frame=df_year, x='gdpPercap', y='lifeExp',
    color='continent', size='pop', hover_name='country')

import streamlit as st

st.plotly_chart(fig)