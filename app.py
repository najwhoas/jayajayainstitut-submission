import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

#import model
model = joblib.load('./model/trained_model.pkl')
standard_scaler = joblib.load('./model/standard_scaler.pkl')

#class untuk data form
#class untuk data form
class form_handler:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.dataframe = None

    #konversi ke dataframe pandas
    def convert_to_pandas(self):
        self.dataframe = pd.DataFrame(self.data_dict, index=[0])  # Added index=[0]

    #membersihkan data sebelum diprediksi
    def cleaning_data(self):
        # Define numerical features for scaling
        numerical_features = ['Application_order','Previous_qualification_grade','Admission_grade',
                            'Curricular_units_1st_sem_enrolled','Curricular_units_2nd_sem_enrolled',
                            'Curricular_units_1st_sem_credited','Curricular_units_2nd_sem_credited',
                            'Curricular_units_1st_sem_approved','Curricular_units_2nd_sem_approved',
                            'Curricular_units_1st_sem_grade','Curricular_units_2nd_sem_grade']
        
        # Create preprocessing pipeline
        preprocessor = ColumnTransformer(
            transformers=[
                ('scaler', standard_scaler, numerical_features)
            ],
            remainder='passthrough'
        )

        # Add the preprocessor and model to the pipeline
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', model)
        ])

        # Fit preprocessor to the data
        pipeline.named_steps['preprocessor'].fit(self.dataframe)

        self.pipeline = pipeline
    
    #prediksi data 
#prediksi data 
    def predict(self):
        prediction_res = self.pipeline.predict_proba(self.dataframe)
        dropout_proba = prediction_res[0][1]  # Probabilitas kelas 1 (Dropout)
        threshold = 0.25

        if dropout_proba >= threshold:
            result = 'Dropout'
            proba = dropout_proba
            proba = 1 - dropout_proba
        else:
            result = 'Graduate'
            proba = 1 - dropout_proba

        return [result, round(proba * 100, 2)]


#isi main page   
def main():
    st.header("🎓 Jaya Jaya Institut Student Status Prediction")
    st.write('Predicting the probability of a student dropping out of school or otherwise')

    #form untuk mengisi data
    with st.form("User Prediction"):
        st.subheader('**👤 Student\'s Profile**')

        st.write('Enter the student\'s information here 👇')
        name = st.text_input("Name", placeholder="Insert the student name...")
        
        # Personal Information
        col1, col2 = st.columns(2)
        with col1:
            Application_order = st.number_input('Application Order (1-10)', 1, 10, 1)
            Daytime_evening_attendance = st.radio('Attendance Time', ['Daytime', 'Evening'])
            Previous_qualification_grade = st.number_input('Previous Qualification Grade (0-200)', 0.0, 200.0, 90.0)
            Admission_grade = st.number_input('Admission Grade (0-200)', 0.0, 200.0, 90.0)

        
        with col2:
            Displaced = st.radio('Displaced Status', ['Yes', 'No'])
            Debtor = st.radio('Debt Status', ['Yes', 'No'])
            Tuition_fees_up_to_date = st.radio('Tuition Fees Up to Date', ['Yes', 'No'])
            Gender = st.radio('Gender', ['Male', 'Female'])
            Scholarship_holder = st.radio('Scholarship Status', ['Yes', 'No'])
        
        with st.container():
            st.subheader("🚀 Academic Performance")
            st.write('Enter the student\'s academic performance here 👇')
            
            # 1st Semester
            with st.expander("1️⃣ 1st Semester"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    Curricular_units_1st_sem_credited = st.number_input('Credited Units', min_value=0, key='cu1_credited')
                with col2:
                    Curricular_units_1st_sem_enrolled = st.number_input('Enrolled Units', min_value=0, key='cu1_enrolled')
                with col3:
                    Curricular_units_1st_sem_approved = st.number_input('Approved Units', min_value=0, key='cu1_approved')
                with col4:
                    Curricular_units_1st_sem_grade = st.number_input('Grade (0-20)', 0.0, 20.0, 0.0, key='cu1_grade')

            # 2nd Semester
            with st.expander("2️⃣ 2nd Semester"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    Curricular_units_2nd_sem_credited = st.number_input('Credited Units', min_value=0, key='cu2_credited')
                with col2:
                    Curricular_units_2nd_sem_enrolled = st.number_input('Enrolled Units', min_value=0, key='cu2_enrolled')
                with col3:
                    Curricular_units_2nd_sem_approved = st.number_input('Approved Units', min_value=0, key='cu2_approved')
                with col4:
                    Curricular_units_2nd_sem_grade = st.number_input('Grade (0-20)', 0.0, 20.0, 0.0, key='cu2_grade')

        submitted = st.form_submit_button("✨ Predict")

        if submitted:
            data = {
                'Application_order': Application_order,
                'Daytime_evening_attendance': 1 if Daytime_evening_attendance == 'Daytime' else 0,
                'Previous_qualification_grade': Previous_qualification_grade,
                'Admission_grade': Admission_grade,
                'Displaced': 1 if Displaced == 'Yes' else 0,
                'Debtor': 1 if Debtor == 'Yes' else 0,
                'Tuition_fees_up_to_date': 1 if Tuition_fees_up_to_date == 'Yes' else 0,
                'Gender': 1 if Gender == 'Male' else 0,
                'Scholarship_holder': 1 if Scholarship_holder == 'Yes' else 0,
                'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
                'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
                'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
                'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
                'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
                'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
                'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
                'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
            }

            submitted_data = form_handler(data)
            submitted_data.convert_to_pandas()
            submitted_data.cleaning_data()
            result, percentage = submitted_data.predict()

            #hasil prediksi
            st.write('**👉 Result :**')
            color = 'red' if result == 'Dropout' else 'green'
            st.markdown(f'<p style="color:{color}">Prediction result of {name}: <strong>{result}</strong> ({percentage}%)</p>', unsafe_allow_html=True)
    

main()