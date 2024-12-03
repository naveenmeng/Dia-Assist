import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = 'D:\\Hackathon\\Dia\\Dataset\\diabetes_prediction_dataset.csv'  # Replace with your actual dataset path
data = pd.read_csv(file_path)

# Handle missing values
data.fillna({
    'age': data['age'].median(),
    'hypertension': data['hypertension'].mode()[0],
    'heart_disease': data['heart_disease'].mode()[0],
    'smoking_history': data['smoking_history'].mode()[0],
    'bmi': data['bmi'].median(),
    'HbA1c_level': data['HbA1c_level'].median(),
    'blood_glucose_level': data['blood_glucose_level'].median()
}, inplace=True)

# Convert categorical variables to numerical values using Label Encoding
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['smoking_history'] = label_encoder.fit_transform(data['smoking_history'])

# Split data into features (X) and target (y)
X = data.drop(columns=['diabetes'])
y = data['diabetes']

# Split the data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
    """Predict diabetes risk based on user input."""

    # Encode smoking history
    try:
        smoking_history_encoded = label_encoder.transform([smoking_history])[0]
    except ValueError:
        return "Invalid smoking history input. Please choose from 'never', 'No Info', or 'current'."

    # Prepare input data
    user_input = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'smoking_history': [smoking_history_encoded],
        'bmi': [bmi],
        'HbA1c_level': [hba1c_level],
        'blood_glucose_level': [blood_glucose_level]
    })

    # Predict diabetes
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        return "You are at risk of diabetes."
    else:
        return "You are not at risk of diabetes."
