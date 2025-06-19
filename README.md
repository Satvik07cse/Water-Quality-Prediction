# Water-Quality-Prediction
💧 Water Quality Prediction - RMS
This project focuses on predicting multiple water quality parameters using machine learning techniques. It was developed during a one-month AICTE Virtual Internship conducted by Edunet Foundation and sponsored by Shell in June 2025.

🌍 Overview

Access to clean water is a global challenge. Timely prediction of water quality metrics is essential for detecting pollution early and enabling appropriate intervention. This project leverages multi-output regression techniques to predict critical water parameters from real-world data.

🧠 Key Objectives

Collect and preprocess real-world water quality datasets

Apply supervised machine learning for multi-target regression

Develop a pipeline using MultiOutputRegressor wrapped around RandomForestRegressor

Evaluate performance using regression metrics

🔬 Predicted Water Quality Parameters
The model predicts the following parameters:

NH4 (Ammonium)

BSK5 (Biochemical Oxygen Demand in 5 days)

Colloids (Suspended Solids)

O2 (Dissolved Oxygen)

NO3, NO2 (Nitrates and Nitrites)

SO4 (Sulfates)

PO4 (Phosphates)

CL (Chloride)

⚙️ Technologies Used
Python 3.12

Pandas, NumPy – Data handling

Scikit-learn – Model training and evaluation

Matplotlib, Seaborn – Data visualization

Jupyter Notebook – Interactive development environment

📈 Model Architecture
Base Model: RandomForestRegressor

Wrapper: MultiOutputRegressor

Pipeline: Preprocessing → Model Training → Multi-target Prediction
📊 Evaluation Metrics
R² Score

Mean Squared Error (MSE)

✅ The model demonstrated consistent performance across all predicted parameters, indicating good generalization on unseen data.
🎓 Internship Details
Type: AICTE Virtual Internship

Platform: Edunet Foundation

Sponsor: Shell

Duration: June 2025 (1 Month)

Domain: Environmental Monitoring using Machine Learning

