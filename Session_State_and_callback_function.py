import streamlit as st
import pandas as pd

st.title('Exploring the Session State and call back functions')

if 'counter' not in st.session_state:
    #st.write('counter initiation')
    st.session_state['counter'] = 0

if 'EVENTS_LIST_DF' not in st.session_state:
    #st.write('EVENTS_LIST initiation')
    st.session_state['EVENTS_LIST_DF'] = []
    
if 'FAMILY_LIST_DF' not in st.session_state:
    #st.write('FAMILY_LIST initiation')
    st.session_state['FAMILY_LIST_DF'] = []

if 'TRIBE_LIST_DF' not in st.session_state:
    #st.write('TRIBE_LIST initiation')
    st.session_state['TRIBE_LIST_DF'] = []
    
if 'GENUS_LIST_DF' not in st.session_state:
    #st.write('TRIBE_LIST initiation')
    st.session_state['GENUS_LIST_DF'] = []

ALL_EVENTS_LIST = [
'1101090'
,'1212903'
,'1212917'
,'1924000'
,'1924001'
,'1924010'
,'1924100'
,'1924110'
,'1924120'
,'1924130'
,'1924140'
]

FAMILY_LIST = ['1','2','3','4']
TRIBE_LIST = ['1','2','3','4','5','6']
GENUS_LIST = ['1','2','3','4','5','6','7','8']

label = 'Select family from the list'

Enter_options_form = st.sidebar.form('Options_form')

EVENTS_LIST = Enter_options_form.selectbox(label, ALL_EVENTS_LIST)
FAMILY_LIST = Enter_options_form.selectbox(label,FAMILY_LIST)
TRIBE_LIST = Enter_options_form.selectbox(label,TRIBE_LIST)
GENUS_LIST = Enter_options_form.selectbox(label,GENUS_LIST)

#add_data = options_form.form_submit_button()



#increment = st.button('Show more columns')
increment = Enter_options_form.form_submit_button()
if increment:
    #st.session_state.counter +=1
    st.session_state['EVENTS_LIST_DF'].append(EVENTS_LIST) 
    st.session_state['FAMILY_LIST_DF'].append(FAMILY_LIST) 
    st.session_state['TRIBE_LIST_DF'].append(TRIBE_LIST) 
    st.session_state['GENUS_LIST_DF'].append(GENUS_LIST) 

#decrement = st.button('Show fewer columns')
#if decrement:
#   st.session_state.counter -=1
    
#st.table(df.head(st.session_state['counter']))
df = pd.DataFrame([st.session_state['EVENTS_LIST_DF'],st.session_state['FAMILY_LIST_DF'],st.session_state['TRIBE_LIST_DF'],st.session_state['GENUS_LIST_DF']])
df = df.transpose()
df.columns = ['EVENTS','FAMILY','TRIBE','GENUS']

st.table(df)
#st.write(st.session_state)
 