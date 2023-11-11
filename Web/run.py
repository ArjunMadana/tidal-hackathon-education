import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run(marital_status, daytime_attendance, previous_qualification, displaced, educational_special_needs, debtor, tuition_up_to_date, gender, scholarship_holder, international, age, gpa):
    feature_columns = ['Age at enrollment', "Curricular units 1st sem (grade)"]  # Replace with your desired feature column names

    new_model = tf.keras.models.load_model('model.keras')

    new_data_categorical = pd.DataFrame({
        "Marital status": [1 if marital_status else 0],  # Replace with actual values
        "Daytime/evening attendance": [1 if daytime_attendance else 0],
        "Previous qualification": [1 if previous_qualification else 0],
        "Displaced": [1 if displaced else 0],
        "Educational special needs": [1 if educational_special_needs else 0],
        "Debtor": [1 if debtor else 0],
        "Tuition fees up to date": [1 if tuition_up_to_date else 0],
        "Gender": [1 if gender else 0],
        "Scholarship holder": [1 if scholarship_holder else 0],
        "International": [1 if international else 0]
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




