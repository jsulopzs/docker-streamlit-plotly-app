# Part 1
import pandas as pd

df = pd.read_excel('../data/gampinder.xlsx')

mask_year = df.year == 2007
df_year = df[mask_year]

import plotly.express as px

fig = px.scatter(
    data_frame=df_year, x='gdpPercap', y='lifeExp', hover_name='country',
    color='continent', facet_col='continent', facet_col_wrap=3, size='pop')

import streamlit as st

st.plotly_chart(fig)