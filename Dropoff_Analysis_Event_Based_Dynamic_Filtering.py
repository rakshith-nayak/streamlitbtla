import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

st.title("User Drop off Funnel")

# ---- User Authentication ------

names = ['BTLA_Product_Team']
usernames = ['BTLA_Product_Team']

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
    authenticator.logout("Logout", "sidebar")
    
    st.header('Funnel metrics Selected:')
    
    Rerun = st.button('Clear All Events')
    
    import streamlit as st
    
    if Rerun:
        from streamlit.legacy_caching import clear_cache
        import streamlit as st
        
        for key in st.session_state.keys():
            del st.session_state[key]    
    
    
        
        #st.cache.clear()
        #st.experimental_rerun()
    
    from PIL import Image

    with st.sidebar.container():
        image = Image.open(r'C:\Users\Tnluser\Desktop\Dropoff Analysis Tool\Images\BTLA_Logo.png')
        st.sidebar.image(image)
        
    #st.write('Hi')
    #importing snowflake and setting the credentials
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
    
    
    
    st.sidebar.subheader('Enter the Event for the Funnel:')
    
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
        
    st.sidebar.subheader('Enter the Details for the Event selected:')
    
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
    
    
    
    
    st.sidebar.caption('Event details are filtered based on the Event submitted')
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
    
    st.subheader('Enter the Filters for the Funnel:')
    st.caption('Note: Timeframe is rolling of 3 months ')
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
    
    
    
    Run_Query = st.button('Create the Funnel')
    
    import re
    #line = re.sub('[]', '', line)
    
    
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
        
        
    #st.session_state['text_list_str'] = text_list_str
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
        
        st.session_state['text_list_str'] = text_list_str
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
            g.grade,a.counter,c.USER_TYPE
            
            from tnlk12.counter_last3 a
            left join tnlk12temp.tnl_cohorts g on a.value3 = g.id
            left join ETL_Install_Source_Mapper b
            on a.device_id = b.device_id and a.server_date_ist>=first_day and a.server_date_ist<=last_day 
            left join "TNLK12TEMP"."BTLA_SESSION_TIME_WITH_ENGAGEMENT" c 
            on a.USER_ID = c.USER_ID AND a.SERVER_DATE_IST = c.SERVER_DATE_IST
            where (""" 
        
        QUERY_PART_2 = text_list_str + ')'
        
        QUERY_PART_3 = SERVER_DATE_TEXT + '\n' +GRADE_TEXT + '\n' +USER_TYPE_TEXT +""" ) 
            
        
        
        
        SELECT  U_EVENT_ID, SERVER_DATE_IST, COUNT(DISTINCT USER_ID) AS USER_COUNT
        -- USER_ID,A.DATE, GRADE, COUNTER  
        FROM homepage a
        GROUP BY U_EVENT_ID, SERVER_DATE_IST
        ORDER BY USER_COUNT DESC
        
        """
        
        PM_Query_1 = SERVER_DATE_TEXT + '\n' +GRADE_TEXT + '\n' +USER_TYPE_TEXT +""" ) 

                        SELECT  *
                        FROM homepage a
        
        
        """
        query = QUERY_PART_1 + ' ' + QUERY_PART_2 + ' ' + QUERY_PART_3
        #st.write(query)
        
        PM_Query =  QUERY_PART_1 + ' ' + QUERY_PART_2 + ' ' + PM_Query_1
        
        
        data = pd.read_sql(query, conn)
        data = pd.DataFrame(data)
        
        
        #st.table(data)
        
        new_df = pd.merge(data, df, how = 'inner', left_on='U_EVENT_ID', right_on='EVENTS')
        #st.table(new_df)
        new_df = pd.DataFrame(new_df.groupby(['EVENTS','DESCRIPTION'])['USER_COUNT'].sum())
        new_df=new_df.reset_index()
        #st.write(new_df) 
        
        
        
        #st.table(new_df)
        if len(new_df)== 0:
            st.write('The dataframe is Null')
        else:
            Funnel_Top_Count = new_df['USER_COUNT'][0]
        
            import plotly.express as px
            
            new_df['percentage'] = new_df['USER_COUNT']/Funnel_Top_Count *100
            new_df = new_df[['EVENTS','DESCRIPTION','USER_COUNT','percentage']]
            
            
            st.subheader('Funnel chart:')
            fig = px.funnel(new_df, x='percentage', y='DESCRIPTION')
            
            # Plot!
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('Funnel chart details:')
            st.table(new_df)
            
            
            import seaborn as sns
            import matplotlib.pyplot as plt
            #fig = plt.figure(figsize=(10, 4))
            #st.write(data)  
            
            new_data = pd.merge(data, df, left_on = 'U_EVENT_ID', right_on = 'EVENTS', how = 'inner')
            
            #new_data['USER_COUNT'] = new_data['USER_COUNT'].astype(int) 
            line_chart_data = new_data[['DESCRIPTION','SERVER_DATE_IST','USER_COUNT']]
            line_chart_data['DESCRIPTION'] = line_chart_data['DESCRIPTION'].astype(str)
            import numpy as np
            
            st.subheader('Events Trend over a period of time:')
            line_chart_cross_tab = pd.crosstab(index=line_chart_data['SERVER_DATE_IST'],columns=line_chart_data['DESCRIPTION'],values=line_chart_data['USER_COUNT'],aggfunc=np.sum)
            
            #st.write(line_chart_cross_tab)
            
            
            #fig = sns.lineplot(new_data, x='SERVER_DATE_IST', y='USER_COUNT')
            fig = px.line(line_chart_cross_tab)
            st.plotly_chart(fig, use_container_width=True) 
            
            
            
            
            
            #st.table(PM_data.head(5))
            
     
    
    
    #PM_Button = st.button('Run the Process Mining')
    #
    #if PM_Button:
    #
    #    QUERY_PART_1 = """WITH homepage as 
    #    (
    #        select distinct a.user_id,a.server_date_ist,a.device_id,value3,a.U_EVENT_ID,
    #        case when b.device_id is null then 'Organic' else 'Inorganic' end as  install_source,
    #        g.grade,a.counter,c.USER_TYPE, a.DATE 
    #        
    #        from tnlk12.counter_last3 a
    #        left join tnlk12temp.tnl_cohorts g on a.value3 = g.id
    #        left join ETL_Install_Source_Mapper b
    #        on a.device_id = b.device_id and a.server_date_ist>=first_day and a.server_date_ist<=last_day 
    #        left join "TNLK12TEMP"."BTLA_SESSION_TIME_WITH_ENGAGEMENT" c 
    #        on a.USER_ID = c.USER_ID AND a.SERVER_DATE_IST = c.SERVER_DATE_IST
    #        where (""" 
    #    
    #    QUERY_PART_2 = text_list_str + ')'
    #    
    #    QUERY_PART_3 = SERVER_DATE_TEXT + '\n' +GRADE_TEXT + '\n' +USER_TYPE_TEXT +""" ) 
    #        
    #    
    #    
    #    
    #    SELECT  U_EVENT_ID, SERVER_DATE_IST, COUNT(DISTINCT USER_ID) AS USER_COUNT
    #    -- USER_ID,A.DATE, GRADE, COUNTER  
    #    FROM homepage a
    #    GROUP BY U_EVENT_ID, SERVER_DATE_IST
    #    ORDER BY USER_COUNT DESC
    #    
    #    """
    #    
    #    PM_Query_1 = SERVER_DATE_TEXT + '\n' +GRADE_TEXT + '\n' +USER_TYPE_TEXT +""" ) 
    #
    #                    SELECT  *
    #                    FROM homepage a
    #    
    #    
    #    """
    #    query = QUERY_PART_1 + ' ' + QUERY_PART_2 + ' ' + QUERY_PART_3
    #    #st.write(query)
    #    
    #    PM_Query =  QUERY_PART_1 + ' ' + QUERY_PART_2 + ' ' + PM_Query_1
    #    
    #    data_1 = pd.read_sql(PM_Query, conn)
    #    data_1 = pd.DataFrame(data_1)   
    #    
    #    #st.write(data_1)
    #
    #    PM_data = pd.merge(data_1, df, left_on = 'U_EVENT_ID', right_on = 'EVENTS', how = 'inner')
    #    PM_data['DATE'] = pd.to_datetime(PM_data['DATE'], utc=True,  errors = 'coerce')
    #        
    #    import pm4py
    #    df = pm4py.format_dataframe(PM_data[['USER_ID','DATE','DESCRIPTION']], case_id='USER_ID',activity_key='DESCRIPTION',
    #                                timestamp_key='DATE')
    #    #bpmn_model = pm4py.discover_bpmn_inductive(df)
    #    #bpmn = pm4py.view_bpmn(bpmn_model)
    #    #st.write(bpmn)
    #    #st.graphviz_chart(bpmn, use_container_width=False)
    #    
    #    dfg, start_activities, end_activities = pm4py.discover_dfg(df)
    #    format = "png"
    #    #
    #    from pm4py.visualization.dfg import visualizer as dfg_visualizer
    #    parameters = dfg_visualizer.Variants.FREQUENCY.value.Parameters
    #    gviz_aplha_miner = dfg_visualizer.apply(dfg, log=None, variant=dfg_visualizer.Variants.FREQUENCY,
    #                        parameters={parameters.FORMAT: format,
    #                                    parameters.START_ACTIVITIES: start_activities,
    #                                    parameters.END_ACTIVITIES: end_activities})
    #                                    
    #    
    #    
    #    st.graphviz_chart(gviz_aplha_miner, use_container_width=True)
    #    
    #    #Download = st.button('Download')
    #    
    #    #if Download:
    #    #    gviz_aplha_miner.savefig('abc.png')
    #    
    #    #st.download_button('Download the Process Mining graph', data = gviz_aplha_miner, file_name = 'PM.png')
    #        
    #     #df = data.groupby('COUNTER')['USER_ID'].nunique() 
    #     #df = pd.DataFrame(df)
    #     ## df['COUNTER'] = df.index
    #     #df.reset_index(inplace=True)
    #     #df['USER_ID'] = df['USER_ID'].astype(int)
    #     #df = df.sort_values(by='USER_ID',ascending = False)
    #     #
    #     #homescreen_arr = df.loc[df['COUNTER']=='homescreen',['USER_ID']].values
    #     #homescreen_list = homescreen_arr[0].tolist()
    #     #homescreen_value = homescreen_list[0]
    #     #
    #     #df['Dropoff_%'] = df['USER_ID']/homescreen_value*100
    #     #
    #     #import plotly.express as px
    #     #fig = px.funnel(df, x='Dropoff_%', y='COUNTER')
    #     #
    #     ## Plot!
    #     #st.plotly_chart(fig, use_container_width=True)
    #     
    #     #import pandas as pd
    #     #import pm4py
    #     #df = pm4py.format_dataframe(data[['USER_ID','DATE','COUNTER']], case_id='USER_ID',activity_key='COUNTER',
    #     #                            timestamp_key='DATE')
    #     #bpmn_model = pm4py.discover_bpmn_inductive(df)
    #     #bpmn = pm4py.view_bpmn(bpmn_model)
    #     #st.graphviz_chart(bpmn, use_container_width=False)
    #     #
    #     #dfg, start_activities, end_activities = pm4py.discover_dfg(df)
    #     #process_flow = pm4py.view_dfg(dfg, start_activities, end_activities)
    #     #st.graphviz_chart(process_flow, use_container_width=False)
    
    
    


