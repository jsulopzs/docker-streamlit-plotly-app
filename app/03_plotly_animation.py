import pandas as pd

df_countries = pd.read_excel('../data/gampinder.xlsx')

import plotly.express as px

import streamlit as st

with st.sidebar:
    list_countries = st.multiselect(
        label='Select countries', options=df_countries.country.unique(),
        default=['Spain', 'United Kingdom'])

mask_country = df_countries.country.isin(list_countries)
dff = df_countries[mask_country]

fig = px.scatter(
    data_frame=dff, x='gdpPercap', y='lifeExp',
    color='continent', size='pop', hover_name='country', size_max=40,
    animation_frame='year', range_y=[20, 90], range_x=[0, 100000])

st.plotly_chart(fig)