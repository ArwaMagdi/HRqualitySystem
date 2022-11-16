import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

header = st.container()
feature = st.container()
model = st.container()

with header:
    st.write(" Promotion prediction system")

with feature:
    df=pd.read_csv("D:\AI402\Graduation project\employee_promotion.csv")
    st.header('See if this employee deserves a promotion!' )
   
    sel_col , disp_col = st.columns(2)

    department = sel_col.selectbox('Department', (df['department'].unique()))
    encoded_dep=[7, 4, 8, 0, 6, 5, 1, 2, 3]
    x=['Sales & Marketing', 'Operations', 'Technology', 'Analytics','R&D', 'Procurement', 'Finance', 'HR', 'Legal']
    for i in range(len(x)):
        if department==x[i]:
            department=encoded_dep[i]

    region = sel_col.selectbox('region', (df['region'].unique()))
    encoded_reg=[31, 14, 10, 15, 18, 11, 12, 27,  0, 28, 21, 24,  6,  5,  2, 29, 20,
        8,  4,  7, 17,  1, 19, 23,  3, 13, 32, 25, 30, 26, 16, 22, 33,  9]
    x=['region_7', 'region_22', 'region_19', 'region_23', 'region_26',
    'region_2', 'region_20', 'region_34', 'region_1', 'region_4',
    'region_29', 'region_31', 'region_15', 'region_14', 'region_11',
    'region_5', 'region_28', 'region_17', 'region_13', 'region_16',
    'region_25', 'region_10', 'region_27', 'region_30', 'region_12',
    'region_21', 'region_8', 'region_32', 'region_6', 'region_33',
    'region_24', 'region_3', 'region_9', 'region_18']
    for i in range(len(x)):
        if region==x[i]:
            region=encoded_reg[i]

    education = sel_col.selectbox('education', (df['education'].unique()))
    encoded_edu=[2, 0,  1]
    x=["Master's & above", "Bachelor's",  'Below Secondary']
    for i in range(len(x)) :
        if education==x[i]:
            education=encoded_edu[i]

    gender = sel_col.selectbox('gender', (df['gender'].unique()))
    encoded_gender=[0,1]
    x=['f', 'm']
    for i in range(len(x)):
        if gender==x[i]:
            gender=encoded_gender[i]

    recruitment_channel = sel_col.selectbox('recruitment_channel', (df['recruitment_channel'].unique()))
    encoded_rec=[2, 0, 1]
    x=['sourcing', 'other', 'referred']
    for i in range(len(x)):
        if recruitment_channel==x[i]:
            recruitment_channel=encoded_rec[i]

    no_of_trainings = sel_col.number_input('no_of_trainings',min_value=0, step=1)
    age = sel_col.number_input('age',min_value=18, step=1)
    previous_year_rating = sel_col.number_input('previous_year_rating',min_value=0, step=1)
    length_of_service=sel_col.number_input('length_of_service',min_value=0,max_value=5, step=1)
    awards_won=sel_col.number_input('awards_won',min_value=0, step=1)
    avg_training_score=sel_col.number_input('avg_training_score',min_value=0)
 
with model:
    
    loaded_model = pickle.load(open(r'C:\Users\HP\trained_model1.pkl','rb'))

    input_data= ([department],[region],[education],[gender],[recruitment_channel],[no_of_trainings],[age],[previous_year_rating],[length_of_service],[awards_won],[avg_training_score])
    
    input_data_as_numpy_acray = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_acray.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0]== 0):
        st.write('Not Promoted')
    elif (prediction[0]== 1):
        st.write("promoted")
