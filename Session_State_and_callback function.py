import streamlit as st
import pandas as pd

st.title('Exploring the Session State and call back functions')

if 'counter' not in st.session_state:
    st.write('counter initiation)
    st.session_state['counter'] = 0


df = pd.read_csv('Session_State_Test.csv')

increment = st.button('Show more columns'):
if increment:
    st.session_state.counter +=1

decrement = st.button('Show fewer columns')
if decrement:
    st.session_state.counter -=1
    
st.table(df.head(st.session_state['counter']))
 