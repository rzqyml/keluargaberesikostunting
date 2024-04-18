import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('cleaned_dataset.csv').fillna(0)

# Convert all non-numeric values to numeric
for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Encode categorical variables
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])

# Split features and target variable
X = df.drop('beresiko stunting', axis=1)
y = df['beresiko stunting']

# Train the Naive Bayes classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X, y)

# Streamlit interface
st.title('Stunting Risk Prediction')

# Add input form for user input
with st.form('input_form'):
    st.write('## Input Criteria')
    
    col1, col2, col3 = st.columns(3)
    
    criteria = {}
    
    with col1:
        criteria["sumber air minum buruk"] = st.selectbox("Apakah Sumber Air Minum Buruk? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])
        criteria["sanitasi buruk"] = st.selectbox("Apakah Sanitasi Buruk? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])
    
    with col2:
        criteria["terlalu muda istri"] = st.selectbox("Apakah Umur Istri Terlalu Muda? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])
        criteria["terlalu tua istri"] = st.selectbox("Apakah Istri Terlalu Tua? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])
    
    with col3:
        criteria["terlalu dekat umur"] = st.selectbox("Apakah Umur Suami & Istri Terlalu Dekat? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])
        criteria["terlalu banyak anak"] = st.selectbox("Apakah Memiliki Banyak Anak? (1=Ya, 0=Tidak)", ['Ya', 'Tidak'])

    submit_button = st.form_submit_button(label='Predict')

    # Make prediction if the form is submitted
    if submit_button:
        # Convert "Ya" to 1 and "Tidak" to 0
        for key, value in criteria.items():
            if value == 'Ya':
                criteria[key] = 1
            elif value == 'Tidak':
                criteria[key] = 0

        # Create a DataFrame from user input
        input_data = pd.DataFrame([criteria])

        # Encode categorical variables in input data
        for column in input_data.columns:
            if input_data[column].dtype == 'object':
                input_data[column] = label_encoders[column].transform(input_data[column])

        # Make prediction
        prediction = nb_classifier.predict(input_data)

        # Determine prediction result
        prediction_result = 'Beresiko Stunting' if all(criteria.values()) else 'Tidak Beresiko Stunting'

        # Display prediction result
        st.write('## Prediction Result')
        st.success(prediction_result)
