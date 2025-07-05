import os
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Display available files (for debugging)
st.write("📁 Files in directory:", os.listdir())

# Load the model and model columns
if os.path.exists("pollution_model.pkl") and os.path.exists("model_columns.pkl"):
    model = joblib.load("pollution_model.pkl")
    model_cols = joblib.load("model_columns.pkl")
    st.success("✅ Model and columns loaded")
else:
    st.error("❌ Model files not found. Please check pollution_model.pkl and model_columns.pkl.")
    st.stop()

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("PB_All_2000_2021.csv")

df = load_data()
st.write("🧾 Columns in dataset:", df.columns.tolist())

# Convert 'date' to datetime and extract year
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

# App Title
st.title("💧 Water Quality Prediction App")
st.write("Predicts pollutant levels based on year and station ID.")

# User inputs
year_input = st.number_input("📅 Enter the Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("🏷️ Enter the Station ID (numeric)", value="1")

# Predict button
if st.button("🔮 Predict"):
    if not station_id.strip().isdigit():
        st.warning("⚠️ Please enter a valid numeric Station ID.")
    else:
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0

        input_encoded = input_encoded[model_cols]

        # Make prediction
        predicted_pollutants = model.predict(input_encoded)
        pollutants = ["O2", "NO3", "NO2", "SO4", "PO4", "CL"]
        st.subheader(f"🧪 Predicted Pollutants at Station ID {station_id} in {year_input}")
        for p, val in zip(pollutants, predicted_pollutants[0]):
            st.write(f"{p}: {val:.2f}")

        # Pollution Trend Chart
        try:
            df_filtered = df[df['id'].astype(str) == station_id]
            trend_data = df_filtered.groupby("year")[pollutants].mean().reset_index()
            st.subheader(f"📈 Pollution Trends Over Years at Station ID {station_id}")
            st.line_chart(trend_data.set_index("year"))
        except KeyError:
            st.warning("⚠️ Couldn't generate trend chart. Ensure 'id' and pollutant columns exist.")