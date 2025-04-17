import re
from pathlib import Path


def preprocess(data):
    if 'caa' in data.columns:
        data = data[data['caa'] < 4]
    if 'thall' in data.columns:
        data = data[data['thall'] > 0]
    data = data.rename(
    columns = {'cp':'chest_pain_type', 
               'trtbps':'resting_blood_pressure', 
               'chol': 'cholesterol',
               'fbs': 'fasting_blood_sugar',
               'restecg' : 'resting_electrocardiogram', 
               'thalachh': 'max_heart_rate_achieved', 
               'exng': 'exercise_induced_angina',
               'oldpeak': 'st_depression', 
               'slp': 'st_slope', 
               'caa':'num_major_vessels', 
               'thall': 'thalassemia',
               'output':'target'
               }, 
    errors='ignore')
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'],inplace=True)
    return data

def export(data):
    data_dir = Path("Data")
    pattern = re.compile(r"heart_(\d+)\.csv")
    existing_files = [f for f in data_dir.iterdir() if f.is_file() and pattern.match(f.name)]

    existing_numbers = [int(pattern.match(f.name).group(1)) for f in existing_files]

    next_number = max(existing_numbers) + 1 if existing_numbers else 1

    filename = data_dir / f"heart_{next_number}.csv"

    data.to_csv(filename, index=False)