import pandas as pd
import streamlit as st
import plotly.express as px

st.title('International Development: GDP & Life Expectancy Relationship')

df = pd.read_excel('data/gampinder.xlsx')

with st.sidebar:
    list_country = st.multiselect('Select the countries', df.country.unique(), default=['Spain', 'United States', 'United Kingdom', 'Japan'])

mask_country = df.country.isin(list_country)
dff = df[mask_country].sort_values('year')

st.write('## Data Visualization')

fig = px.scatter(
    data_frame=dff, x='gdpPercap', y='lifeExp',
    hover_name='country', color='continent', size='pop', animation_frame='year',
    log_x=True, size_max=40, range_x=[100, 100000], range_y=[25, 90])

st.plotly_chart(fig)

st.write('## Data Table')

st.dataframe(dff)