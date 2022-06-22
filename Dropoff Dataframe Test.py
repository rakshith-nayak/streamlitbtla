import streamlit as st
import pandas as pd

st.title('Test')

EVENTS_df = pd.DataFrame(columns=['EVENTS','FAMILY','TRIBE','GENUS'])

st.sidebar.header('Events Options')
options_form = st.sidebar.form('Options_form')

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

EVENTS_LIST = options_form.selectbox(label, ALL_EVENTS_LIST)
FAMILY_LIST = options_form.selectbox(label,FAMILY_LIST)
TRIBE_LIST = options_form.selectbox(label,TRIBE_LIST)
GENUS_LIST = options_form.selectbox(label,GENUS_LIST)

add_data = options_form.form_submit_button()

if add_data:
    st.write(EVENTS_LIST,FAMILY_LIST,TRIBE_LIST,GENUS_LIST)
    new_data = {'EVENTS':EVENTS_LIST,
                'FAMILY':FAMILY_LIST,
                'TRIBE':TRIBE_LIST,
                'GENUS':GENUS_LIST}
    st.write(new_data)
    EVENTS_df = EVENTS_df.append(new_data, ignore_index=true)   
    st.table(EVENTS_df)