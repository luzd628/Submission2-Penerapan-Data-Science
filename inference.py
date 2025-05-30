# -*- coding: utf-8 -*-
"""Inference_submission2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hMqihCepXin5Ny0pdEKxgSQc_aoR2MF0

## Inferensi Model Klasifikasi Siswa yang kemungkinan Dropout/Lulus

### Import Library
"""

import pandas as pd
import pickle

"""### Load Model & Inference"""

# Load Model
with open('model.pkl','rb') as file:
  model = pickle.load(file)

# Inference
new_data = pd.DataFrame({
    'Marital_status': [1],
    'Application_mode': [2],
    'Application_order': [1],
    'Course': [5],
    'Daytime_evening_attendance': [1],
    'Previous_qualification': [3],
    'Previous_qualification_grade': [155.5],
    'Mothers_occupation': [4],
    'Fathers_occupation': [5],
    'Admission_grade': [130.0],
    'Displaced': [1],
    'Debtor': [0],
    'Tuition_fees_up_to_date': [1],
    'Gender': [0],
    'Scholarship_holder': [1],
    'Age_at_enrollment': [20],
    'Curricular_units_1st_sem_grade': [12.0],
    'Curricular_units_2nd_sem_grade': [15.5],
    'Unemployment_rate': [6.0],
    'Inflation_rate': [2.5],
    'GDP': [1200.0],
    'Total_Curricular_Credited': [12],
    'Total_Curricular_Enrolled': [18],
    'Total_Curricular_Approved': [10],
    'Total_Curricular_Evaluations': [25],
    'Total_Curricular_Without_Evaluation': [2],
})

#Predict
predict = model.predict(new_data)

# Output
if (predict[0] == 1):
  print("Siswa berkemungkinan Lulus")
else:
  print("Siswa berkemungkinan Dropout")