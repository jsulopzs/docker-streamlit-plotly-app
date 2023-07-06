import streamlit as st
import pickle
import pandas as pd

with open('../pickles/model_lr.pkl', 'rb') as f:
    model_lr = pickle.load(f)

with st.form('user_input'):
    
    total_bill = st.number_input('How much will the table pay?')
    size = st.number_input('How many people are in the table?')
    
    st.write('Total bill', total_bill)
    st.write('Size', size)
    
    button = st.form_submit_button()
    
    if button:
    
        dic = {
            'total_bill': total_bill,
            'size': size
        }

        df_user = pd.DataFrame(dic, index=['user'])
        
        prediction = model_lr.predict(X=df_user)[0]
        prediction = prediction.round(2)
        st.write(f'The table will tip you with ${prediction}.')
    