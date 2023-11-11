import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run(marital_status, daytime_attendance, previous_qualification, displaced, educational_special_needs, debtor, tuition_up_to_date, gender, scholarship_holder, international, age, gpa):
    feature_columns = ['Age at enrollment', "Curricular units 1st sem (grade)"]  # Replace with your desired feature column names

    new_model = tf.keras.models.load_model('model.keras')

    new_data_categorical = pd.DataFrame({
        "Marital status": [marital_status],  # Replace with actual values
        "Daytime/evening attendance": [daytime_attendance],
        "Previous qualification": [previous_qualification],
        "Displaced": [displaced],
        "Educational special needs": [educational_special_needs],
        "Debtor": [debtor],
        "Tuition fees up to date": [tuition_up_to_date],
        "Gender": [gender],
        "Scholarship holder": [scholarship_holder],
        "International": [international]
    })

    new_data_numerical = pd.DataFrame({
        'Age at enrollment': [age],  # Replace with actual values
        "Curricular units 1st sem (grade)": [gpa * 5] # scale from 4-point scale to 40-point scale
    })

    # Combine one-hot encoded categorical features with numerical features
    new_data_combined = pd.concat([new_data_numerical, pd.get_dummies(new_data_categorical)], axis=1)

    # Standardize numerical features (use the same scaler as used during training)
    scaler = StandardScaler()
    new_data_combined[feature_columns] = scaler.fit_transform(new_data_combined[feature_columns])

    # Ensure the input data is a NumPy array
    new_data_array = new_data_combined.to_numpy()

    # Make predictions
    predictions = new_model.predict(new_data_array)

    return predictions[0][0]




