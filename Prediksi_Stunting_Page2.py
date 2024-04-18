import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Load the trained model
kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

# Title of the web app
st.title('Stunting Risk Prediction')

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

# DataFrame for the uploaded Excel data
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Display the DataFrame
    st.write('DataFrame from Excel File:')
    st.write(df)

    # Button for prediction
    if st.button('Make Prediction'):
        # Remove non-numeric columns
        numeric_df = df.select_dtypes(include=['number'])

        # Make predictions
        predictions = kbst_model.predict(numeric_df)

        # Add predictions to the DataFrame
        df['Beresiko Stunting'] = predictions

        # Display the DataFrame with predictions
        st.write('DataFrame with Predictions:')
        st.write(df)
        
        # Generate pie chart
        prediction_counts = df['Beresiko Stunting'].value_counts()
        prediction_counts.index = ['Tidak Beresiko Stunting' if idx == 0 else 'Beresiko Stunting' for idx in prediction_counts.index]
        fig = px.pie(prediction_counts, values=prediction_counts.values, names=prediction_counts.index,
                     title='Prediction Distribution')
        st.plotly_chart(fig)
