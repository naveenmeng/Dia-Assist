import pandas as pd


def predict(ppbs, hbaic, bmi, age):
    # Initialize the list to hold the report data
    report_data = []

    # HBA1C value-based report
    if hbaic < 5.7:
        hbaic_report = "Normal (Less than 5.7%)"
    elif 5.7 <= hbaic <= 6.4:
        hbaic_report = "Prediabetes (Between 5.7% and 6.4%)"
    else:
        hbaic_report = "Diabetes (Above 6.5%)"

    report_data.append({"Parameter": "HBA1C", "Value": f"{hbaic}%", "Report": hbaic_report})

    # PPBS value-based report
    if ppbs < 140:
        ppbs_report = "Normal (Less than 140)"
    elif 140 <= ppbs <= 199:
        ppbs_report = "Borderline High (Between 140 and 199)"
    else:
        ppbs_report = "High (200 or greater)"

    report_data.append({"Parameter": "PPBS", "Value": f"{ppbs}", "Report": ppbs_report})

    # BMI report
    if bmi < 18.5:
        bmi_report = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_report = "Normal weight"
    elif 25 <= bmi < 29.9:
        bmi_report = "Overweight"
    else:
        bmi_report = "Obesity"

    report_data.append({"Parameter": "BMI", "Value": f"{bmi}", "Report": bmi_report})

    # General health report based on all input parameters
    if hbaic >= 6.5 or ppbs >= 200:
        health_report = "At risk for Type 1 Diabetes. Please consult a healthcare professional."
    elif hbaic >= 5.7 or ppbs >= 140:
        health_report = "At risk of developing diabetes. Consider lifestyle changes and regular monitoring."
    else:
        health_report = "Your health indicators seem normal, but continue monitoring and maintain a healthy lifestyle."

    report_data.append({"Parameter": "General Health Report", "Value": "", "Report": health_report})

    # Convert the report data into a DataFrame
    report_df = pd.DataFrame(report_data)

    # Return the DataFrame to be displayed in the Streamlit app
    return report_df
