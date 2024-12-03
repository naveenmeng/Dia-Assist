import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import random
import requests

# Load the dataset
file_path = 'D:\projects\last\Dataset\diabetes_prediction_dataset.csv'  # Replace with the path to your dataset
data = pd.read_csv(file_path)

# Handle missing values
data.fillna({
    'age': data['age'].median(),
    'hypertension': data['hypertension'].mode()[0],
    'heart_disease': data['heart_disease'].mode()[0],
    'smoking_history': data['smoking_history'].mode()[0],
    'bmi': data['bmi'].median(),
    'HbA1c_level': data['HbA1c_level'].median(),
    'blood_glucose_level': data['blood_glucose_level'].median(),
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


# Function to calculate insulin dosage
def calculate_insulin_dosage(weight, diabetes_type):
    # Type 1 Diabetes: 0.5 - 1.0 units per kg of body weight
    print(diabetes_type)
    if diabetes_type == 1:
        insulin_dosage = weight * 0.8  # Example average of 0.5-1 unit/kg
        insulin_type = "Type 1 Diabetes"
    # Type 2 Diabetes: 0.2 - 0.5 units per kg of body weight
    elif diabetes_type == 2:
        insulin_dosage = weight * 0.3  # Example average of 0.2-0.5 unit/kg
        insulin_type = "Type 2 Diabetes"
    else:
        insulin_dosage = 0
        insulin_type = "Unknown Diabetes Type"

    # Calculate basal and bolus dosages
    basal_dosage = insulin_dosage * 0.6  # 60% for basal insulin
    bolus_dosage = insulin_dosage * 0.4  # 40% for bolus insulin

    return insulin_dosage, basal_dosage, bolus_dosage, insulin_type


# Function to fetch diabetes medications from OpenFDA API
def fetch_diabetes_medications():
    url = "https://api.fda.gov/drug/label.json"
    params = {
        "search": "indications_and_usage:diabetes",
        "limit": 1  # Limiting the results to top 1 medication
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if there is medication data
        if not data.get("results"):
            print("No medication data found.")
            return []

        medications = data["results"]

        # Shuffle the medication list to randomize the output
        random.shuffle(medications)

        medications_info = []

        for med in medications:
            # Extract medication details
            brand_name = med.get("openfda", {}).get("brand_name", ["Unknown"])[0]
            generic_name = med.get("openfda", {}).get("generic_name", ["Unknown"])[0]

            if brand_name == "Unknown" and generic_name == "Unknown":
                continue  # Skip medications with unknown brand and generic name

            usage = med.get("indications_and_usage", ["No details available"])[0]

            usage_points = usage.split(". ")
            if usage_points[0] == "No details available":
                usage_points = ["Usage information not available."]

            usage_points = list(dict.fromkeys(usage_points))  # Removing duplicates

            dosage = "500 mg once daily"  # Example dosage

            medications_info.append({
                "Brand Name": brand_name,
                "Generic Name": generic_name,
                "Suggested Dosage": dosage,
                "Usage": usage_points
            })

        return medications_info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching medications: {e}")
        return []


# Function to predict diabetes and suggest insulin dosage and medications
def predict_and_suggest(user_input, weight):
    # Ensure the user_input is in DataFrame format (if it's not already)
    if not isinstance(user_input, pd.DataFrame):
        user_input = pd.DataFrame([user_input])

    # Extract hba1c_level and age from the user_input
    hba1c_level = user_input['HbA1c_level'].iloc[0]
    age = user_input['age'].iloc[0]

    # Determine the diabetes type based on HbA1c level and age
    if hba1c_level > 9 and age < 18:  # Matching both HbA1c and age for Type 1
        diabetes_type = 1  # Type 1 Diabetes
    elif hba1c_level <= 9 and age >= 18:  # Matching both HbA1c and age for Type 2
        diabetes_type = 2  # Type 2 Diabetes
    else:
        # If age and HbA1c don't match both, use HbA1c as the determining factor
        if hba1c_level > 9:
            diabetes_type = 1  # Type 1 Diabetes
        else:
            diabetes_type = 2  # Type 2 Diabetes

    # Calculate insulin dosage based on diabetes type
    insulin_dosage, basal_dosage, bolus_dosage, insulin_type = calculate_insulin_dosage(weight, diabetes_type)

    # If Type 2 Diabetes, fetch medications
    medications_info = []
    if diabetes_type == 2:  # Type 2 Diabetes
        medications_info = fetch_diabetes_medications()

    return diabetes_type, insulin_dosage, basal_dosage, bolus_dosage, insulin_type, medications_info

