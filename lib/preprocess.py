def preprocess(data):
    data = data[data['caa'] < 4]
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
    errors="raise")
    return data