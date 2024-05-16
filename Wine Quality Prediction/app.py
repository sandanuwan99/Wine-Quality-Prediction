import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('Wine_Quality_Prediction.pkl','rb'))

st.header('Wine Quality Prediction')

fixed_acidity = st.slider('Enter fixed_acidit',0,15)
volatile_acidity = st.slider('Enter volatile acidity',0,20)
citric_acid = st.slider('Enter citric Acid', 0,20)
residual_sugar = st.slider('Enter Residual Sugar',0,20)
chlorides = st.slider('Enter chlorides',0,20)
free_sulfur_dioxide = st.slider('Enter Free Sulfur Dioxide',0,20)
total_sulfur_dioxide = st.slider('Enter Total Sulfur Dioxide',0,20)
density = st.slider('Enter Density',0,20)
pH = st.slider('Enter ph',0,20)
sulphates = st.slider('Enter Suphates',0,20)
alcohol = st.slider('Enter Alcohol',0,20)

input_data = (fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)

if st.button('Predict'):
    predict_quality = model.predict(input_data)
    if predict_quality[0]==1:
        st.markdown('Good Quality Wine')
    else:
        st.markdown('Bad Quality Wine')

