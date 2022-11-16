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
    st.write(" Attrition prediction system")

with feature:
    df=pd.read_csv("D:\AI402\Graduation project\employee_attrition_train.csv")
    st.header('See if this employee is about to departure!' )
    
   
    sel_col , disp_col = st.columns(2)

    age = sel_col.number_input('age',min_value=18, step=1)

    travel=sel_col.selectbox('BusinessTravel', (df['BusinessTravel'].unique()))
    encoded_travel=[2, 1, 0]
    x=['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']
    for i in range(len(x)):
        if travel==x[i]:
            travel=encoded_travel[i]

    rate = sel_col.number_input('DailyRate',min_value=0, step=1)

    department = sel_col.selectbox('Department', (df['Department'].unique()))
    encoded_dep=[1, 2, 0]
    x=['Research & Development', 'Sales', 'Human Resources']
    for i in range(len(x)):
        if department==x[i]:
            department=encoded_dep[i]
    
    distance= sel_col.number_input('DistanceFromHome',min_value=0, step=1)
    
    education = sel_col.selectbox("education##1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'", (df['Education'].unique()))
    
    field = sel_col.selectbox('EducationField', (df['EducationField'].unique()))
    encoded_dep=[1, 0, 2, 3, 4]
    x=['Medical', 'Marketing', 'Life Sciences', 'Technical Degree',
       'Human Resources', 'Other']
    for i in range(len(x)):
        if field==x[i]:
            field=encoded_dep[i]

    EnvironmentSatisfaction = sel_col.number_input('EnvironmentSatisfaction',min_value=1, max_value=4)

    gender = sel_col.selectbox('gender', (df['Gender'].unique()))
    encoded_gender=[0,1]
    x=['Female', 'Male']
    for i in range(len(x)):
        if gender==x[i]:
            gender=encoded_gender[i]

    hrate = sel_col.number_input('HourlyRate',min_value=0, step=1)

    JobInvolvement=sel_col.number_input('JobInvolvement',min_value=1, max_value=4)
    JobLevel=sel_col.number_input('JobLevel',min_value=1, max_value=5)

    JobRole=sel_col.selectbox('JobRole', (df['JobRole'].unique()))
    encoded_travel=[5, 4, 8, 3, 0, 6, 7, 2, 1]
    x=['Research Director', 'Manufacturing Director','Sales Representative', 'Manager', 'Healthcare Representative',
    'Research Scientist', 'Sales Executive', 'Laboratory Technician','Human Resources']
    for i in range(len(x)):
        if JobRole==x[i]:
            JobRole=encoded_travel[i]
    
    JobSatisfaction = sel_col.number_input('JobSatisfaction',min_value=1, max_value=4)

    marital=sel_col.selectbox('MaritalStatus', (df['MaritalStatus'].unique()))
    encoded_travel=[0, 2, 1]
    x=['Divorced', 'Single', 'Married']
    for i in range(len(x)):
        if marital==x[i]:
            marital=encoded_travel[i]

    income = sel_col.number_input('MonthlyIncome',min_value=0, step=1)

    mrate = sel_col.number_input('MonthlyRate',min_value=0, step=1)
    
    num_companies = sel_col.number_input('NumCompaniesWorked',min_value=0, step=1)

    OverTime=sel_col.selectbox('OverTime', (df['OverTime'].unique()))
    if OverTime=='No':
        OverTime=0
    elif OverTime=="Yes":
        OverTime==1
    
    PercentSalaryHike=sel_col.number_input('PercentSalaryHike',min_value=0, step=1)
    PerformanceRating=sel_col.number_input('PerformanceRating',min_value=1, max_value=4)
    RelationshipSatisfaction=sel_col.number_input('RelationshipSatisfaction',min_value=1, max_value=4)
    StockOptionLevel=sel_col.number_input('StockOptionLevel',min_value=1, max_value=3)
    TotalWorkingYears=sel_col.number_input('TotalWorkingYears',min_value=0, step=1)
    TrainingTimesLastYear=sel_col.number_input('TrainingTimesLastYear',min_value=0, step=1)
    WorkLifeBalance=sel_col.number_input('WorkLifeBalance',min_value=1, max_value=4)
    YearsAtCompany=sel_col.number_input('YearsAtCompany',min_value=0, step=1)
    YearsInCurrentRole=sel_col.number_input('YearsInCurrentRole',min_value=0, step=1)
    YearsSinceLastPromotion=sel_col.number_input('YearsSinceLastPromotion',min_value=0, step=1)
    YearsWithCurrManager=sel_col.number_input('YearsWithCurrManager',min_value=0, step=1)



 
with model:
    
    loaded_model = pickle.load(open(r'C:\Users\HP\trained_model2.pkl','rb'))

    input_data=( [age], [travel], [rate], [department],[distance], [education], [field],[EnvironmentSatisfaction], [gender],  [hrate],[JobInvolvement], [JobLevel], [JobRole], [JobSatisfaction],[marital], [income], [mrate], [num_companies],[OverTime], [PercentSalaryHike], [PerformanceRating],[RelationshipSatisfaction], [StockOptionLevel],[TotalWorkingYears], [TrainingTimesLastYear], [WorkLifeBalance],[YearsAtCompany], [YearsInCurrentRole], [YearsSinceLastPromotion],[YearsWithCurrManager])
    
    input_data_as_numpy_acray = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_acray.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0]== 0):
        st.write('Will not departure')
    elif (prediction[0]== 1):
        st.write("Will departure")