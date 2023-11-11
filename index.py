import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data from CSV file
csv_file_path = 'dataset.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Output
target_column = 'Target'

# Categorical features
categorical_columns = ["Marital status", "Daytime/evening attendance", "Previous qualification", "Displaced", "Educational special needs", "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "International"]

X_categorical = df[categorical_columns]

# Numerical feature columns
feature_columns = ['Age at enrollment', "Curricular units 1st sem (grade)"]

X_numerical = df[feature_columns]

# Combine one-hot encoded categorical features with numerical features
X_combined = np.concatenate([X_numerical.values, X_categorical.values], axis=1)

y = [1 if v == "Dropout" else 0 for v in df[target_column]] # Convert text values to one-hot encoded integers

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train[:, :len(feature_columns)] = scaler.fit_transform(X_train[:, :len(feature_columns)])
X_test[:, :len(feature_columns)] = scaler.transform(X_test[:, :len(feature_columns)])

y_train = np.array(y_train)
y_test = np.array(y_test)

# Create the model
model = Sequential()

# Add layers
model.add(Dense(32, activation='relu', input_dim=X_combined.shape[1]))
model.add(Dense(32, activation='relu', input_dim=32))
model.add(Dense(1, activation='sigmoid'))  # Output layer with sigmoid activation for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

model.save("model.keras")