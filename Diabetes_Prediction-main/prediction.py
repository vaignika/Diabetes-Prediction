import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "model.pkl")
    
    # Load the model
    try:
        model = pickle.load(open(model_path, "rb"))
    except FileNotFoundError:
        st.error(f"Could not find model file at {model_path}")
        return
        
    st.title('Diabetes Prediction Using Machine Learning')
    Pregnancies = st.number_input("Pregnancies",min_value=0,format="%d",help="Number of pregnancies")
    Glucose = st.number_input("Glucose",min_value=0,format="%d",help="Plasma Glucose Concentration")
    BloodPressure = st.number_input("Blood Pressure",min_value=0,format="%d",help="Diastolic Blood Pressure (mm Hg)")
    SkinThickness = st.number_input("Skin Thickness",min_value=0,format="%d",help="Triceps skin fold thickness (in mm)")
    Insulin = st.number_input("Insulin",min_value=0,format="%d",help="2-Hour Serum Insulin (mu U/ml)")
    BMI = st.number_input("BMI",min_value=0.0,help="Body Mass Index")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function",help="Likelihood of diabetes based on genetic/hereditary factors")
    Age = st.number_input("Age",min_value=0,max_value=100,format="%d",help="Age in years")

    if st.button("Predict"):
        input_array = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        y_pred = model.predict(input_array)
        y_prob = model.predict_proba(input_array)
        
        if y_pred[0] == 1:
            prediction = "Diabetic"
            confidence = y_prob[0][1] * 100
        else:
            prediction = "Non Diabetic"
            confidence = y_prob[0][0] * 100

        st.markdown(f"Based on your input: {prediction}")
        st.markdown(f"Confidence: {confidence:.2f}%")

if __name__ == '__main__':
    main()
