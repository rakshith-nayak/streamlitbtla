import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

st.title("Drop off Analysis")

# ---- User Authentication ------

names = ['BTLA_Product_Team']
usernames = ['BTLA_Product_Team']


# data
import pandas as pd
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.util import dataframe_utils

# process mining 
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

# viz
from pm4py.visualization.petrinet import visualizer as pn_visualizer
from pm4py.visualization.process_tree import visualizer as pt_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization

# misc 
from pm4py.objects.conversion.process_tree import converter as pt_converter

file_path = Path(__file__).parent / "hashed_pw.pkl" 

with file_path.open("rb") as file:
	hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "Dropoff Funnel Analysis Dashboard",
    "abcdef",
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error('Username/Password is incorrect')
    
if authentication_status == None:
    st.error('Please enter Username and Password')



if authentication_status:
    #st.write('Hi')
    #importing snowflake and setting the credentials
    
    #st.sidebar.image("C:\Users\Tnluser\Desktop\Dropoff Analysis Tool\Images\BTLA_Logo.png")
    import pandas as pd
    EVENTS_df = pd.DataFrame(columns=['EVENTS','FAMILY','TRIBE','GENUS'])
    
    import snowflake.connector
    #create connection
    conn=snowflake.connector.connect(
                    user='rakshith_nayak',
                    password='Rakshith@007',
                    account='yd42534.ap-southeast-1',
                    role = 'K12_ANALYST',
                    warehouse='K12_ANALYSTS_WH2'
                    ,database='TNL_K12',
                    schema='TNLK12TEMP'
    #                 ,authenticator='externalbrowser'
                    )
    #create cursor
    curs=conn.cursor()
    
    authenticator.logout("Logout", "sidebar")
    
    #if 'counter' not in st.session_state:
    #    #st.write('counter initiation')
    #    st.session_state['counter'] = 0
    
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
        
    if 'COUNTER_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['COUNTER_LIST_DF'] = []
        
    if 'VARIETY_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['VARIETY_LIST_DF'] = []
    
    if 'SPECIES_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['SPECIES_LIST_DF'] = []
        
    if 'RECORD_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['RECORD_LIST_DF'] = []
        
    if 'FORM_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['FORM_LIST_DF'] = []
        
    if 'VALUE1_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['VALUE1_LIST_DF'] = []
    
    if 'VALUE2_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['VALUE2_LIST_DF'] = []
    
    if 'DESCRIPTION' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['DESCRIPTION'] = []
    
    if 'Start_Date' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['START_DATE'] = ''
        
    if 'End_Date' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['END_DATE'] = ''
        
    if 'Family_test' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['Family_test'] = ''
        
    if 'GRADE_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['GRADE_LIST_DF'] = []
        
    if 'USER_TYPE_LIST_DF' not in st.session_state:
        #st.write('TRIBE_LIST initiation')
        st.session_state['USER_TYPE_LIST_DF'] = []
        
    import os
    ALL_EVENTS_LIST_QUERY = """SELECT * from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS""" 
    ALL_EVENTS_LIST = pd.read_sql(ALL_EVENTS_LIST_QUERY, conn)
    ALL_EVENTS_LIST = pd.DataFrame(ALL_EVENTS_LIST)
    
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    ALL_EVENTS_LIST = ALL_EVENTS_LIST[ALL_EVENTS_LIST['U_EVENT_ID'].notna()]
    ALL_EVENTS_LIST = ALL_EVENTS_LIST['U_EVENT_ID'].astype(int).tolist()
    #st.write(ALL_EVENTS_LIST) 
    
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #FAMILY_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_FAMILY_OPTIONS.csv')
    #st.table(FAMILY_LIST)
    
    
    #st.write(FAMILY_LIST)
    
    #FAMILY_LIST = ['1','2','3','4'] 
    
    
    
    
   
    
    Enter_Events_Form = st.sidebar.form('Events_form')
    
    EVENTS_LIST = Enter_Events_Form.selectbox('Select Events from the list', ALL_EVENTS_LIST)
    DESCRIPTION = Enter_Events_Form.text_input('Enter the Description')
    Enter_Events_Form_Increment = Enter_Events_Form.form_submit_button()
    if Enter_Events_Form_Increment:
        #st.session_state.counter +=1
        st.session_state['EVENTS_LIST_DF'].append(EVENTS_LIST)
        st.session_state['DESCRIPTION'].append(str(DESCRIPTION))
        
    
    if len(st.session_state['EVENTS_LIST_DF'])==0:
        EVENTS_SUB_TEXT = '1101090'
        #st.write(EVENTS_SUB_TEXT)
    else:
        EVENTS_SUB_TEXT = str(EVENTS_LIST)
        EVENTS_SUB_TEXT = EVENTS_SUB_TEXT.replace('[','')
        EVENTS_SUB_TEXT = EVENTS_SUB_TEXT.replace(']','')
        #st.write(EVENTS_SUB_TEXT)
        
    ALL_FAMILY_LIST_QUERY = """SELECT DISTINCT TOP 1000 FAMILY from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_FAMILY_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    FAMILY_LIST = pd.read_sql(ALL_FAMILY_LIST_QUERY, conn)
    FAMILY_LIST = pd.DataFrame(FAMILY_LIST)
    FAMILY_LIST = FAMILY_LIST[FAMILY_LIST['FAMILY'].notna()]
    FAMILY_LIST = FAMILY_LIST['FAMILY'].astype(str).tolist()
    FAMILY_LIST.insert(0,'All') 
    #st.write(FAMILY_LIST)
        
        
    ALL_TRIBE_LIST_QUERY = """SELECT DISTINCT TOP 1000 TRIBE from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_TRIBE_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    TRIBE_LIST = pd.read_sql(ALL_TRIBE_LIST_QUERY, conn)
    TRIBE_LIST = pd.DataFrame(TRIBE_LIST)
    TRIBE_LIST = TRIBE_LIST[TRIBE_LIST['TRIBE'].notna()] 
    TRIBE_LIST = TRIBE_LIST['TRIBE'].astype(str).tolist()
    TRIBE_LIST.insert(0,'All')
    #st.write(TRIBE_LIST)
    
    ALL_GENUS_LIST_QUERY = """SELECT DISTINCT TOP 1000 GENUS from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_GENUS_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    GENUS_LIST = pd.read_sql(ALL_GENUS_LIST_QUERY, conn)
    GENUS_LIST = pd.DataFrame(GENUS_LIST)
    GENUS_LIST = GENUS_LIST[GENUS_LIST['GENUS'].notna()]
    GENUS_LIST = GENUS_LIST['GENUS'].astype(str).tolist()
    GENUS_LIST.insert(0,'All')
    #st.write(GENUS_LIST)
    
    
    COUNTER_QUERY = """SELECT DISTINCT TOP 1000 COUNTER from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_COUNTER_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    COUNTER_LIST = pd.read_sql(COUNTER_QUERY, conn)
    COUNTER_LIST = pd.DataFrame(COUNTER_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    COUNTER_LIST = COUNTER_LIST[COUNTER_LIST['COUNTER'].notna()]
    COUNTER_LIST = COUNTER_LIST['COUNTER'].astype(str).tolist()
    COUNTER_LIST.insert(0,'All')
    #st.write(COUNTER_LIST) 
    
    VARIETY_QUERY = """SELECT DISTINCT TOP 1000 VARIETY from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_VARIETY_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    VARIETY_LIST = pd.read_sql(VARIETY_QUERY, conn)
    VARIETY_LIST = pd.DataFrame(VARIETY_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    VARIETY_LIST = VARIETY_LIST[VARIETY_LIST['VARIETY'].notna()]
    VARIETY_LIST = VARIETY_LIST['VARIETY'].astype(str).tolist()
    VARIETY_LIST.insert(0,'All')
    #st.write(VARIETY_LIST) 
    
    SPECIES_QUERY = """SELECT DISTINCT TOP 1000 SPECIES from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_SPECIES_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    SPECIES_LIST = pd.read_sql(SPECIES_QUERY, conn)
    SPECIES_LIST = pd.DataFrame(SPECIES_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    SPECIES_LIST = SPECIES_LIST[SPECIES_LIST['SPECIES'].notna()]
    SPECIES_LIST = SPECIES_LIST['SPECIES'].astype(str).tolist()
    SPECIES_LIST.insert(0,'All')
    #st.write(SPECIES_LIST) 
    
    RECORD_QUERY = """SELECT DISTINCT TOP 1000 RECORD from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_RECORD_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    RECORD_LIST = pd.read_sql(RECORD_QUERY, conn)
    RECORD_LIST = pd.DataFrame(RECORD_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    RECORD_LIST = RECORD_LIST[RECORD_LIST['RECORD'].notna()]
    RECORD_LIST = RECORD_LIST['RECORD'].astype(str).tolist()
    RECORD_LIST.insert(0,'All')
    #st.write(RECORD_LIST) 
    
    
    FORM_QUERY = """SELECT DISTINCT TOP 1000 FORM from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_FORM_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    FORM_LIST = pd.read_sql(FORM_QUERY, conn)
    FORM_LIST = pd.DataFrame(FORM_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    FORM_LIST = FORM_LIST[FORM_LIST['FORM'].notna()]
    FORM_LIST = FORM_LIST['FORM'].astype(str).tolist()
    FORM_LIST.insert(0,'All')
    #st.write(FORM_LIST) 
    
    
    VALUE1_QUERY = """SELECT DISTINCT TOP 1000 VALUE1 from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_VALUE1_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    VALUE1_LIST = pd.read_sql(VALUE1_QUERY, conn)
    VALUE1_LIST = pd.DataFrame(VALUE1_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    VALUE1_LIST = VALUE1_LIST[VALUE1_LIST['VALUE1'].notna()]
    VALUE1_LIST = VALUE1_LIST['VALUE1'].astype(str).tolist()
    VALUE1_LIST.insert(0,'All')
    #st.write(VALUE1_LIST) 
    
    
    VALUE2_QUERY = """SELECT DISTINCT TOP 1000 VALUE2 from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_VALUE2_OPTIONS""" + '\n' + """where U_EVENT_ID = """ + str(EVENTS_SUB_TEXT)
    VALUE2_LIST = pd.read_sql(VALUE2_QUERY, conn)
    VALUE2_LIST = pd.DataFrame(VALUE2_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    VALUE2_LIST = VALUE2_LIST[VALUE2_LIST['VALUE2'].notna()]
    VALUE2_LIST = VALUE2_LIST['VALUE2'].astype(str).tolist()
    VALUE2_LIST.insert(0,'All')
    #st.write(VALUE2_LIST) 
    
    
    
    
    
    Enter_options_form = st.sidebar.form('Options_form')
    FAMILY_LIST = Enter_options_form.multiselect('Select Family from the list',FAMILY_LIST,default='All')
    TRIBE_LIST = Enter_options_form.multiselect('Select Tribe from the list',TRIBE_LIST,default='All')
    GENUS_LIST = Enter_options_form.multiselect('Select Genus from the list',GENUS_LIST,default='All')
    COUNTER_LIST = Enter_options_form.multiselect('Select Counter from the list',COUNTER_LIST,default='All')
    VARIETY_LIST = Enter_options_form.multiselect('Select Variety from the list',VARIETY_LIST,default='All')
    SPECIES_LIST = Enter_options_form.multiselect('Select Species from the list',SPECIES_LIST,default='All')
    RECORD_LIST = Enter_options_form.multiselect('Select Record from the list',RECORD_LIST,default='All')
    FORM_LIST = Enter_options_form.multiselect('Select Form from the list',FORM_LIST,default='All')
    VALUE1_LIST = Enter_options_form.multiselect('Select Value1 from the list',VALUE1_LIST,default='All')
    VALUE2_LIST = Enter_options_form.multiselect('Select Value2 from the list',VALUE2_LIST,default='All')
    Enter_options_form_Increment = Enter_options_form.form_submit_button()
    
    #if FAMILY_LIST is None:
    #    FAMILY_LIST = [' ']
    
    if Enter_options_form_Increment:
        
        st.session_state['FAMILY_LIST_DF'].append(FAMILY_LIST)
        st.session_state['TRIBE_LIST_DF'].append(TRIBE_LIST)
        st.session_state['GENUS_LIST_DF'].append(GENUS_LIST)
        st.session_state['COUNTER_LIST_DF'].append(COUNTER_LIST)
        st.session_state['SPECIES_LIST_DF'].append(SPECIES_LIST)
        st.session_state['VARIETY_LIST_DF'].append(VARIETY_LIST)
        st.session_state['RECORD_LIST_DF'].append(RECORD_LIST)
        st.session_state['FORM_LIST_DF'].append(FORM_LIST)
        st.session_state['VALUE1_LIST_DF'].append(VALUE1_LIST)
        st.session_state['VALUE2_LIST_DF'].append(VALUE2_LIST)
        
        
    EVENTS_LIST_DF_SERIES = pd.Series(st.session_state['EVENTS_LIST_DF'])
    DESCRIPTION_SERIES = pd.Series(st.session_state['DESCRIPTION'])
    FAMILY_LIST_DF_SERIES = pd.Series(st.session_state['FAMILY_LIST_DF'])
    TRIBE_LIST_DF_SERIES = pd.Series(st.session_state['TRIBE_LIST_DF'])
    GENUS_LIST_DF_SERIES = pd.Series(st.session_state['GENUS_LIST_DF'])
    COUNTER_LIST_DF_SERIES = pd.Series(st.session_state['COUNTER_LIST_DF'])
    SPECIES_LIST_DF_SERIES = pd.Series(st.session_state['SPECIES_LIST_DF'])
    VARIETY_LIST_DF_SERIES = pd.Series(st.session_state['VARIETY_LIST_DF'])
    RECORD_LIST_DF_SERIES = pd.Series(st.session_state['RECORD_LIST_DF'])
    FORM_LIST_DF_SERIES = pd.Series(st.session_state['FORM_LIST_DF'])
    VALUE1_LIST_DF_SERIES = pd.Series(st.session_state['VALUE1_LIST_DF'])
    VALUE2_LIST_DF_SERIES = pd.Series(st.session_state['VALUE2_LIST_DF'])
    
    
    #st.write(FAMILY_LIST_DF_SERIES)
    
    df = pd.DataFrame(dict(EVENTS=EVENTS_LIST_DF_SERIES
                           ,DESCRIPTION= DESCRIPTION_SERIES
                           ,FAMILY=FAMILY_LIST_DF_SERIES
                           ,TRIBE=TRIBE_LIST_DF_SERIES
                           ,GENUS=GENUS_LIST_DF_SERIES
                           ,COUNTER=COUNTER_LIST_DF_SERIES
                           ,SPECIES=SPECIES_LIST_DF_SERIES
                           ,VARIETY=VARIETY_LIST_DF_SERIES
                           ,RECORD=RECORD_LIST_DF_SERIES
                           ,FORM=FORM_LIST_DF_SERIES
                           ,VALUE1= VALUE1_LIST_DF_SERIES
                           ,VALUE2=VALUE2_LIST_DF_SERIES
                           )).reset_index()
    st.table(df)
    #df.columns = ['EVENTS','FAMILY','TRIBE','GENUS','COUNTER','SPECIES','VARIETY','RECORD','FORM','VALUE1','VALUE2','DESCRIPTION']
    
        
    #df = pd.DataFrame([st.session_state['EVENTS_LIST_DF']
    #                ,[st.session_state['FAMILY_LIST_DF']]
    #                ,[st.session_state['TRIBE_LIST_DF']]
    #                ,[st.session_state['GENUS_LIST_DF']]
    #                ,[st.session_state['COUNTER_LIST_DF']]
    #                ,[st.session_state['SPECIES_LIST_DF']]
    #                ,[st.session_state['VARIETY_LIST_DF']]
    #                ,[st.session_state['RECORD_LIST_DF']]
    #                ,[st.session_state['FORM_LIST_DF']]
    #                ,[st.session_state['VALUE1_LIST_DF']]
    #                ,[st.session_state['VALUE2_LIST_DF']]
    #                ,st.session_state['DESCRIPTION']])
    #df = df.transpose() 
    #df.columns = ['EVENTS','FAMILY','TRIBE','GENUS','COUNTER','SPECIES','VARIETY','RECORD','FORM','VALUE1','VALUE2','DESCRIPTION']
    
    #st.subheader('The Events and the corresponding filters for the funnel')
    #df['index'] = df.index
    #st.table(df)    
        
    
    DATES_OPTIONS_LIST_QUERY = """SELECT * from tnlk12temp.DROPOFF_FUNNEL_ANALYSIS_DATE_OPTIONS""" 
    DATES_OPTIONS_LIST = pd.read_sql(DATES_OPTIONS_LIST_QUERY, conn)
    DATES_OPTIONS_LIST = pd.DataFrame(DATES_OPTIONS_LIST)
    DATES_OPTIONS_LIST = DATES_OPTIONS_LIST[DATES_OPTIONS_LIST['SERVER_DATE_IST'].notna()]
    DATES_OPTIONS_LIST = DATES_OPTIONS_LIST['SERVER_DATE_IST'].astype(str).tolist()
    
    
    GRADE_QUERY = """SELECT DISTINCT GRADE from tnlk12temp.tnl_cohorts""" 
    GRADE_LIST = pd.read_sql(GRADE_QUERY, conn)
    GRADE_LIST = pd.DataFrame(GRADE_LIST)
    #os.chdir('C:\\Users\\Tnluser\\Desktop\\Dropoff Analysis Tool\\Datasets')
    #ALL_EVENTS_LIST = pd.read_csv('DROPOFF_FUNNEL_ANALYSIS_EVENTS_OPTIONS.csv')
    GRADE_LIST = GRADE_LIST[GRADE_LIST['GRADE'].notna()]
    GRADE_LIST = GRADE_LIST['GRADE'].astype(str).tolist()
    GRADE_LIST.insert(0,'All') 
    #st.write(VALUE2_LIST) 
    
    USER_TYPE_LIST = ['Returning User','D0 User']
    
    
    Filters_form = st.form('Filters_form')
    st.session_state['START_DATE'] = Filters_form.selectbox('Select the Start date for the analysis',DATES_OPTIONS_LIST)
    st.session_state['END_DATE'] = Filters_form.selectbox('Select the END date for the analysis',DATES_OPTIONS_LIST)
    st.session_state['GRADE_LIST_DF'] = Filters_form.multiselect('Select the grades for the analysis',GRADE_LIST)
    st.session_state['USER_TYPE_LIST_DF'] = Filters_form.multiselect('Select the User Types for the analysis',USER_TYPE_LIST)
    Add_Filters = Filters_form.form_submit_button()
    
    
    #if Add_Filters:
    #   st.write('start date Selected:', st.session_state['START_DATE'])
    #   st.write('end_data Selected:',st.session_state['END_DATE'])
    #   st.write('Grades Selected:',st.session_state['GRADE_LIST_DF'])
    #   st.write('User_Type Selected:',st.session_state['USER_TYPE_LIST_DF'])
    
    
    
    Run_Query = st.button('Run the Query')
    
    import re
    #line = re.sub('[]', '', line)
    
    if Run_Query:
        text_list = []
        
        #st.write(st.session_state['START_DATE'])
        #st.write(st.session_state['END_DATE'])
        
        for index,row in df.iterrows():
            index = row['index']
            EVENT = row['EVENTS']
            
            FAMILY = str(row['FAMILY'])
            FAMILY = FAMILY.replace('[','')
            FAMILY = FAMILY.replace(']','')
            
            TRIBE = str(row['TRIBE'])
            TRIBE = TRIBE.replace('[','')
            TRIBE = TRIBE.replace(']','')
            
            GENUS = str(row['GENUS'])
            GENUS = GENUS.replace('[','')
            GENUS = GENUS.replace(']','')
            
            COUNTER = str(row['COUNTER'])
            COUNTER = COUNTER.replace('[','')
            COUNTER = COUNTER.replace(']','')
            
            SPECIES = str(row['SPECIES'])
            SPECIES = SPECIES.replace('[','')
            SPECIES = SPECIES.replace(']','')
            
            VARIETY = str(row['VARIETY'])
            VARIETY = VARIETY.replace('[','')
            VARIETY = VARIETY.replace(']','')
            
            RECORD = str(row['RECORD'])
            RECORD = RECORD.replace('[','')
            RECORD = RECORD.replace(']','')
            
            FORM = str(row['FORM'])
            FORM = FORM.replace('[','')
            FORM = FORM.replace(']','')
            
            VALUE1 = str(row['VALUE1'])
            VALUE1 = VALUE1.replace('[','')
            VALUE1 = VALUE1.replace(']','')
            
            VALUE2 = str(row['VALUE2'])
            VALUE2 = VALUE2.replace('[','')
            VALUE2 = VALUE2.replace(']','')
            
            
            
            
            # st.write(index, EVENT, FAMILY, TRIBE, GENUS)
            
            if index == 0:
                OR = ''
            else:
                OR = 'OR '
            
            EVENTS_TEXT = OR + '( a.U_EVENT_ID in ( ' +"'" + str(EVENT) +"'" + ' ) ' 
            #st.write(EVENTS_TEXT)
            
            #st.write(FAMILY)
            if FAMILY == '' or FAMILY == 'None' or FAMILY == "'All'": 
                FAMILY_TEXT = ''
                #st.write(1)
            else:
                FAMILY_TEXT = 'AND a.FAMILY in ( ' + str(FAMILY)  + ' ) '
                #st.write(2)
            #st.write(FAMILY_TEXT)
                
            if GENUS == '' or GENUS == 'None' or GENUS == "'All'":
                GENUS_TEXT = ''
            else:
                GENUS_TEXT = 'AND a.GENUS in ( '+ str(GENUS)  + ' ) '
            #st.write(GENUS_TEXT)
            
            if TRIBE == '' or TRIBE == 'None' or TRIBE == "'All'":
                TRIBE_TEXT = ''
            else:
                TRIBE_TEXT = 'AND a.TRIBE in ( ' + str(TRIBE) + ' ) '
            #st.write(TRIBE_TEXT)
            
            if COUNTER == '' or COUNTER == 'None' or COUNTER == "'All'":
                COUNTER_TEXT = ''
            else:
                COUNTER_TEXT = 'AND a.COUNTER in ( ' + str(COUNTER) + ' ) '
                
            if SPECIES == '' or SPECIES == 'None' or SPECIES == "'All'":
                SPECIES_TEXT = ''
            else:
                SPECIES_TEXT = 'AND a.SPECIES in ( ' + str(SPECIES) + ' ) '
                
            if RECORD == '' or RECORD == 'None' or RECORD == "'All'":
                RECORD_TEXT = ''
            else:
                RECORD_TEXT = 'AND a.RECORD in ( ' + str(RECORD) + ' ) '
                
            if FORM == '' or FORM == 'None' or FORM == "'All'":
                FORM_TEXT = ''
            else:
                FORM_TEXT = 'AND a.FORM in ( ' + str(FORM) + ' ) '
                
            if VALUE1 == '' or VALUE1 == 'None' or VALUE1 == "'All'":
                VALUE1_TEXT = ''
            else:
                VALUE1_TEXT = 'AND a.VALUE1 in ( ' + str(VALUE1) + ' ) '
                
            if VALUE2 == '' or VALUE2 == 'None' or VALUE2 == "'All'":
                VALUE2_TEXT = ''
            else:
                VALUE2_TEXT = 'AND a.VALUE2 in ( ' + str(VALUE2) + ' ) '
            
            
            text =  EVENTS_TEXT + FAMILY_TEXT + GENUS_TEXT + TRIBE_TEXT + COUNTER_TEXT +  SPECIES_TEXT + RECORD_TEXT + FORM_TEXT + VALUE1_TEXT + VALUE2_TEXT +')' + '\n'
            #st.write(text)
            
            text_list.append(text)
        
        #st.write(text_list)
        
        text_list_str = ' '.join(text_list)
        #st.write(text_list_str)
        
        #st.write(st.session_state['GRADE_LIST_DF'])
        GRADE = str(st.session_state['GRADE_LIST_DF'])
        GRADE = GRADE.replace('[','')
        GRADE = GRADE.replace(']','')
        #st.write(GRADE) 
        
        USER_TYPE = str(st.session_state['USER_TYPE_LIST_DF'])
        USER_TYPE = USER_TYPE.replace('[','')
        USER_TYPE = USER_TYPE.replace(']','')
        
        if st.session_state['START_DATE'] != st.session_state['END_DATE']:
            SERVER_DATE_TEXT = """ and a.server_date_ist >= """ + "'" +str(st.session_state['START_DATE']) + "'" + """ and a.server_date_ist <= """ + "'"+ str(st.session_state['END_DATE'])+ "'"
        else:
            SERVER_DATE_TEXT = """ and a.server_date_ist = """ + "'" +str(st.session_state['START_DATE']) + "'" 
    
        #st.write(SERVER_DATE_TEXT)
        
        
        if GRADE == '' or GRADE == 'None':
            GRADE_TEXT = ''
        else:
            GRADE_TEXT = """ and g.GRADE IN ( """ + GRADE + """ ) """
            
        
        if USER_TYPE == '' or USER_TYPE == 'None':
            USER_TYPE_TEXT = ''
        else:
            USER_TYPE_TEXT = """ and c.USER_TYPE IN ( """ + USER_TYPE + """ ) """
        
        
        
        QUERY_PART_1 = """WITH homepage as 
        (
            select distinct a.user_id,a.server_date_ist,a.device_id,value3,a.U_EVENT_ID,
            case when b.device_id is null then 'Organic' else 'Inorganic' end as  install_source,
            g.grade,a.counter,c.USER_TYPE,a.DATE
            
            from tnlk12.counter_last3 a
            left join tnlk12temp.tnl_cohorts g on a.value3 = g.id
            left join ETL_Install_Source_Mapper b
            on a.device_id = b.device_id and a.server_date_ist>=first_day and a.server_date_ist<=last_day 
            left join "TNLK12TEMP"."BTLA_SESSION_TIME_WITH_ENGAGEMENT" c 
            on a.USER_ID = c.USER_ID AND a.SERVER_DATE_IST = c.SERVER_DATE_IST
            where (""" 
        
        QUERY_PART_2 = text_list_str + ')'
        
        QUERY_PART_3 = SERVER_DATE_TEXT + '\n' +GRADE_TEXT + '\n' +USER_TYPE_TEXT +""" ) 
            
        
        
        
        SELECT  *
        FROM homepage a
        
        
        """
        query = QUERY_PART_1 + ' ' + QUERY_PART_2 + ' ' + QUERY_PART_3
        st.write(query)
        
        
        data = pd.read_sql(query, conn)
        data = pd.DataFrame(data)
        
        PM_data = pd.merge(data, df, left_on = 'U_EVENT_ID', right_on = 'EVENTS', how = 'inner')
        st.table(PM_data.head(5))
        
        #st.table(data.head(5))
        
        #new_df = pd.merge(data, df, how = 'inner', left_on='U_EVENT_ID', right_on='EVENTS')
        #
        #if len(new_df)== 0:
        #    st.write('The dataframe is Null')
        #else:
        #    Funnel_Top_Count = new_df['USER_COUNT'][0]
        #
        #    import plotly.express as px
        #    
        #    new_df['percentage'] = new_df['USER_COUNT']/Funnel_Top_Count *100
        #    new_df = new_df[['U_EVENT_ID','DESCRIPTION','USER_COUNT','percentage']]
        #    st.table(new_df)
        #    
        #    fig = px.funnel(new_df, x='percentage', y='DESCRIPTION')
        #    
        #    # Plot!
        #    st.plotly_chart(fig, use_container_width=True)
        
        
         #df = data.groupby('COUNTER')['USER_ID'].nunique() 
         #df = pd.DataFrame(df) 
         ## df['COUNTER'] = df.index
         #df.reset_index(inplace=True)
         #df['USER_ID'] = df['USER_ID'].astype(int)
         #df = df.sort_values(by='USER_ID',ascending = False)
         #
         #homescreen_arr = df.loc[df['COUNTER']=='homescreen',['USER_ID']].values
         #homescreen_list = homescreen_arr[0].tolist()
         #homescreen_value = homescreen_list[0]
         #
         #df['Dropoff_%'] = df['USER_ID']/homescreen_value*100 
         #
         #import plotly.express as px 
         #fig = px.funnel(df, x='Dropoff_%', y='COUNTER')
         #
         ## Plot!
         #st.plotly_chart(fig, use_container_width=True)
         
         #import pandas as pd
        import pm4py
        df = pm4py.format_dataframe(PM_data[['USER_ID','DATE','DESCRIPTION']], case_id='USER_ID',activity_key='DESCRIPTION',
                                    timestamp_key='DATE')
        #bpmn_model = pm4py.discover_bpmn_inductive(df)
        #bpmn = pm4py.view_bpmn(bpmn_model)
        #st.write(bpmn)
        #st.graphviz_chart(bpmn, use_container_width=False)
        
        dfg, start_activities, end_activities = pm4py.discover_dfg(df)
        format = "png"
        #
        from pm4py.visualization.dfg import visualizer as dfg_visualizer
        parameters = dfg_visualizer.Variants.FREQUENCY.value.Parameters
        gviz_aplha_miner = dfg_visualizer.apply(dfg, log=None, variant=dfg_visualizer.Variants.FREQUENCY,
                                parameters={parameters.FORMAT: format,
                                            parameters.START_ACTIVITIES: start_activities,
                                            parameters.END_ACTIVITIES: end_activities})
                                            
        
        
        st.graphviz_chart(gviz_aplha_miner, use_container_width=True)
        
        
        ## Import the alpha_miner algorithm
        #from pm4py.algo.discovery.alpha import algorithm as alpha_miner
        #net, initial_marking, final_marking = alpha_miner.apply(df)
        #
        #
        ### Import the petrinet visualizer object
        #from pm4py.visualization.petrinet import visualizer as pn_visualizer
        ## Visualise 
        #gviz_1 = pn_visualizer.apply(net, initial_marking, final_marking) 
        #st.graphviz_chart(gviz_1)
        ##pn_visualizer.view(gviz)
        #
        #gviz_2 = pn_visualizer.apply(net, initial_marking, final_marking,parameters=parameters,variant=pn_visualizer.Variants.FREQUENCY,log=df)
        #st.graphviz_chart(gviz_2)
        
        
        #pn_visualizer.view(gviz)
        #Fig_Size_1 = st.form('Fig_Size')
        #Fig_Size = Fig_Size_1.number_input(label="Fig size",format="%.2f", min_value = 1, value='float')        
        #Fig_Size_submit = Fig_Size_1.form_submit_button()
        
        #if Fig_Size_submit:
        #from PIL import Image
        #Alpha_miner_image = Image.open(dfg_visualizer.view(gviz_aplha_miner))
        #st.image(Alpha_miner_image, caption='Alpha_miner_image')
        
        
        
        # BPMN model
        bpmn_model = pm4py.discover_bpmn_inductive(df)
        
        from pm4py.visualization.bpmn import visualizer as bpmn_visualizer
        parameters = bpmn_visualizer.Variants.CLASSIC.value.Parameters
        gviz_bpmn = bpmn_visualizer.apply(bpmn_model, parameters={parameters.FORMAT: format})
        #BPMN_Image = Image.open(gviz.name)
        st.graphviz_chart(gviz_bpmn, use_container_width = True)
        
        
        #Inductive miner
        # convert the process tree to a petri net
        tree = inductive_miner.apply_tree(df)
        net, initial_marking, final_marking = pt_converter.apply(tree)
        
        # alternatively, use the inductive_miner to create a petri net from scratch
        # net, initial_marking, final_marking = inductive_miner.apply(log)
        
        # viz
        parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
        gviz_inductive_miner = pn_visualizer.apply(net, initial_marking, final_marking, 
                                    parameters=parameters, 
                                    variant=pn_visualizer.Variants.FREQUENCY, 
                                    log=df)
        st.graphviz_chart(gviz_inductive_miner)
        
        
        # heuristics miner
        #map = pm4py.discover_heuristics_net(df)
        #
        #format = "png"
        #from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
        #parameters = hn_visualizer.Variants.PYDOTPLUS.value.Parameters
        #gviz_hue_net = hn_visualizer.apply(map, parameters={parameters.FORMAT: format})
        #
        #from PIL import Image
        #hue_net_image = Image.open(gviz_hue_net)
        #
        #test = hue_net_image.name
        #st.image(test)
        #hn_visualizer.view(gviz)
        
        #pm4py.view_heuristics_net(map)

        # viz
        #gviz_hue_net = hn_visualizer.apply(heu_net)
        #st.graphviz_chart(gviz_hue_net, use_container_width = True)
        
        
        #try:
        #    filename = gviz.name
        #    figure = filename
        #except AttributeError:
        #    # continue without problems, a proper path has been provided
        #    pass
        #
        #from IPython.display import Image
        #img = Image(figure)
        ##img.save('img.png')
        #
        #with open(r"C:\Users\Tnluser\Desktop\Test\BPMN_Test.png", "wb") as png:
        #    png.write(img.png)
        
        #BPMN_Image = Image.open(gviz.name)
        #st.image(BPMN_Image)
        
        
        #BPMN_Image = Image.open(figure)
        #st.image(BPMN_Image)
        
        
        #gviz.savefig(r'C:\Users\Tnluser\Desktop\Test\img.png')
        
        #import shutil
        #shutil.copyfile(gviz, r'C:\Users\Tnluser\Desktop\Test\img.png')
        
        
        
        
        
        #import matplotlib.pyplot as plt
        #import matplotlib.image as mpimg
        #
        ##matplotlib test
        #img = mpimg.imread(gviz)
        ##img.savefig(r'C:\Users\Tnluser\Desktop\Test\img.png')
        #st.pyplot(img) 
        
        
        
        #Try saving the image
        #from IPython.display import Image
        #BPMN_Image = Image(gviz)
        #BPMN_Image.save(r'C:\Users\Tnluser\Desktop\Test')
        #from IPython.display import display
        #st.image(display(BPMN_Image))
        
        #from PIL import Image
        #Test = Image.open(BPMN_Image)
        #st.image(Test[0])
        
        #BPMN_Image = Image.open(pm4py.view_bpmn(bpmn_model))
        #st.image(BPMN_Image)
        
        
        #from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
        #parameters = hn_visualizer.Variants.PYDOTPLUS.value.Parameters
        #
        #dependency_threshold=0.5
        #and_threshold=0.65
        #loop_two_threshold=0.5
        #
        #from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
        #parameters = heuristics_miner.Variants.CLASSIC.value.Parameters
        #map = heuristics_miner.apply_heu(df, variant=heuristics_miner.Variants.CLASSIC, parameters={
        #                                    parameters.DEPENDENCY_THRESH: dependency_threshold, parameters.AND_MEASURE_THRESH: and_threshold,
        #                                    parameters.LOOP_LENGTH_TWO_THRESH: loop_two_threshold})
        #
        #from typing import Optional, Dict, Any, List
        #
        #from pm4py.objects.bpmn.obj import BPMN
        #from pm4py.objects.heuristics_net.obj import HeuristicsNet
        #from pm4py.objects.log.obj import EventLog
        #from pm4py.objects.petri_net.obj import PetriNet, Marking
        #from pm4py.objects.process_tree.obj import ProcessTree
        #import pandas as pd
        #from typing import Union, List
        #from pm4py.util.pandas_utils import check_is_pandas_dataframe, check_pandas_dataframe_columns
        #from pm4py.utils import get_properties
        #from copy import copy
        
        
        #def view_heuristics_net(heu_net: HeuristicsNet, format: str = "png"):
        #    """
        #    Views an heuristics net
        #
        #    Parameters
        #    --------------
        #    heu_net
        #        Heuristics net
        #    format
        #        Format of the visualization (default: png)
        #    """
        #    from PIL import Image
        #    from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
        #    parameters = hn_visualizer.Variants.PYDOTPLUS.value.Parameters
        #    gviz = hn_visualizer.apply(heu_net, parameters={parameters.FORMAT: format})
        #    
        #    #import matplotlib.pyplot as plt
        #    #import matplotlib.image as mpimg
        #    #
        #    #img = mpimg.imread(gviz)
        #    st.image(gviz) 
        #    
        #    #Hueristics_miner_image = Image.open(gviz)
        #    #st.image(Hueristics_miner_image)
        #    #Hueristics_miner_image = Image.open(hn_visualizer.view(gviz)) 
        #    #st.image(Hueristics_miner_image)
        #    
        #view_heuristics_net(map)
            
        #Hueristics_miner_image = Image.open(pm4py.view_heuristics_net(map))
        #st.image(Hueristics_miner_image)
        
        #from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
        #parameters = hn_visualizer.Variants.PYDOTPLUS.value.Parameters
        #gviz = hn_visualizer.apply(heu_net, parameters={parameters.FORMAT: format})
        #hn_visualizer.view(gviz)
        
        #format="png"
        #gviz_hueristic_net = hn_visualizer.apply(map, parameters={parameters.FORMAT: "png"})
        #Hueristics_miner_image = Image.open(hn_visualizer.view(gviz_hueristic_net))
        #st.image(Hueristics_miner_image, caption='Hueristics_miner_image')
        
        #from graphviz import *
        #map = pm4py.discover_heuristics_net(df)
        #st.image(pm4py.view_heuristics_net(map),caption = 'Hueristics_net_image')
        #Hueristics_net_image = Image.open(pm4py.view_heuristics_net(map))
        #st.image(Hueristics_net_image, caption = 'Hueristics_net_image')
        
            
            #st.graphviz_chart(pm4py.view_dfg(dfg, start_activities, end_activities))
            #st.write(process_flow)
            #st.graphviz_chart(process_flow, use_container_width=False) 
    
    
    



## Add line chart

