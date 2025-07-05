#import all necessary libraries
import os 
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st
#load the model
model = joblib.load("pollution_model.pkl")
model_cols=joblib.load("model_columns.pkl")
#user interface 

@st.cache_data
def load_data():
    return pd.read_csv("datasetwaterquality.csv")

df = load_data()

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

st.title("Water Quality Prediction App")
st.write("This app predicts the water quality based on year and station ID.")
st.write("✅ App started")  # Debug line

# Check model exists
if os.path.exists("pollution_model.pkl") and os.path.exists("model_columns.pkl"):
    st.write("✅ Model found")
    model = joblib.load("pollution_model.pkl")
    model_cols = joblib.load("model_columns.pkl")
else:
    st.error("❌ Model file not found. Please check Git LFS or upload again.")
    st.stop()
#user inputs
year_input =st.number_input("enter the year",min_value=200,max_value=2100,value=2022)
station_mapping = {
    "1": "Ganga - Kanpur",
    "2": "Yamuna - Delhi",
    "3": "Mithi - Mumbai",
    "4": "Hooghly - Kolkata",
    "5": "Sabarmati - Ahmedabad"
    # Add all from your dataset
}

station_name = st.selectbox("Select a Station", list(station_mapping.values()))
station_id = [k for k, v in station_mapping.items() if v == station_name][0]

#button to predict
if st.button('predict'):
    if not station_id:
        st.warning("Please enter a station ID")
    else:
        input_df=pd.DataFrame({'year':[year_input],'id':[station_id]})
        input_encoded=pd.get_dummies(input_df, columns=['id'])
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col]=0
        input_encoded=input_encoded[model_cols]
        #predict
        predicted_pollutants =model.predict(input_encoded)
        pollutants=["O2","NO3","NO2","SO4","PO4","CL"]
        st.subheader(f"Predicted Pollutants '{station_id}' in {year_input}:")
        predicted_values={}
        for p, val in zip(pollutants, predicted_pollutants[0]):
            st.write(f'{p}: {val:.2f}')
            # Pollution Trend Chart
df_filtered = df[df['id'].astype(str) == station_id]

pollutants = ["O2", "NO3", "NO2", "SO4", "PO4", "CL"]
trend_data = df_filtered.groupby("year")[pollutants].mean().reset_index()

st.subheader(f"📈 Pollution Trends Over Years at {station_name}")
st.line_chart(trend_data.set_index("year"))
