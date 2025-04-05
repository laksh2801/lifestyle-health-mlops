# Lifestyle Health Dataset

A comprehensive dataset capturing lifestyle and health metrics to facilitate research on correlations between daily habits, biometrics, and health outcomes.

---

## 📁 Dataset Overview
**Filename**: `FINAL_LIFESTYLE_DATASET.csv`  
**Rows**: 1,000+ entries (sample data provided)  
**Columns**: 15  
**Use Cases**: Health analytics, BMI prediction, lifestyle impact studies, and machine learning models.

---

## 📋 Column Descriptions

| Column Name         | Description                                                                 | Data Type | Notes                                                                 |
|---------------------|-----------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------|
| Age                 | Age of the individual (years)                                               | Integer   | Range: 18–69                                                          |
| Gender              | Gender identifier                                                           | Integer   | Encoded as `0` (Female), `1` (Male), `2` (Other/Unspecified)          |
| Height              | Height in meters (m)                                                        | Float     | Range: 1.27–2.16 m                                                   |
| Weight              | Weight in kilograms (kg)                                                    | Float     | Range: 45–130 kg                                                     |
| Activity_Level      | Physical activity level (ordinal scale)                                     | Integer   | `0` (Sedentary) to `3` (Highly Active)                               |
| Daily_Steps         | Number of steps recorded daily                                              | Integer   | Contains outliers (e.g., negative values: -49, -1049)                |
| Exercise_Hours      | Hours spent exercising daily                                                | Float     | Range: 0.02–5.0 hours                                                |
| Sleep_Hours         | Hours of sleep per night                                                    | Float     | Range: 4.0–10.0 hours                                                |
| Stress_Level        | Self-reported stress level (scale: 0–10)                                    | Integer   | `0` (No Stress) to `10` (Extreme Stress)                             |
| Calorie_Intake      | Daily calorie intake (kcal)                                                 | Float     | Range: 958–2918 kcal                                                 |
| Protein_Intake      | Daily protein intake (grams)                                                | Float     | Range: 9.9–101.7 g                                                   |
| Water_Intake        | Daily water consumption (liters)                                            | Float     | Range: 0.55–4.68 L                                                   |
| Family_History      | Family history of chronic diseases (binary)                                 | Integer   | `0` (No), `1` (Yes)                                                  |
| BMI                 | Body Mass Index (kg/m²)                                                     | Float     | Range: 13.69–56.20                                                   |
| BMI_Category        | BMI classification (encoded)                                                | Integer   | Likely `0` (Underweight), `1` (Normal), `2` (Overweight), `3` (Obese) |

---

## 🔍 Key Observations & Notes
1. **Data Quality**:  
   - Negative values in `Daily_Steps` (e.g., -49, -1049) likely indicate missing data or entry errors.  
   - Incomplete rows (e.g., `53,1,`) suggest potential data collection gaps.  

2. **Categorical Encoding**:  
   - Confirm `BMI_Category` labels with domain experts for accurate interpretation.  

3. **Outliers**:  
   - Extreme values in `Weight` (e.g., 130 kg) and `Calorie_Intake` (e.g., 2918 kcal) may require normalization.  

---

## 💡 Potential Analyses
- **BMI Prediction**: Train models to predict BMI using lifestyle features.  
- **Stress-Sleep Correlation**: Explore how stress levels relate to sleep duration.  
- **Activity Impact**: Analyze how `Activity_Level` influences `Daily_Steps` and `Exercise_Hours`.  

---

## 🛠️ Usage Example (Python)

```python
import pandas as pd

# Load the dataset
df = pd.read_csv("FINAL_LIFESTYLE_DATASET.csv")

# Preview data
print(df.head())

# Clean negative steps (example)
df["Daily_Steps"] = df["Daily_Steps"].apply(lambda x: x if x > 0 else None)
