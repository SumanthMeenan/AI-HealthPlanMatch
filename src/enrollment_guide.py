import pandas as pd
import numpy as np
# from sklearn.neighbors import NearestNeighbors

# Function to recommend health plans
def recommend_plan(member_profile, plans_data):
    plans_data = plans_data.copy()
    
    # Preprocess the plans data (encode categorical variables)
    plans_data['Network Type'] = plans_data['Network Type'].map({'PPO': 0, 'HMO': 1, 'EPO': 2, 'POS': 3})
    plans_data['Chronic Condition Coverage'] = plans_data['Chronic Condition Coverage'].apply(lambda x: 1 if member_profile["Condition"] in x else 0)
    
    # Preparing feature vectors for recommendation
    features = ['Monthly Premium', 'Deductible', 'Coverage (%)', 'Network Type', 'Chronic Condition Coverage']
    X = plans_data[features]
    
    # Use Nearest Neighbors to recommend the best matching plan
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(X)
    
    member_vector = np.array([member_profile['Budget'], 2000, 80, {'PPO': 0, 'HMO': 1, 'EPO': 2, 'POS': 3}[member_profile['Network']], member_profile['Condition'] in plans_data['Chronic Condition Coverage'].values]).reshape(1, -1)
    
    # Find the nearest neighbor
    _, indices = knn.kneighbors(member_vector)
    
    # Return the recommended plan
    return plans_data.iloc[indices[0][0]].to_dict()

# src/enrollment_guide.py
def generate_enrollment_guide(health_plan):
    guide = f"Enrollment Guide for {health_plan['Plan Name']}:\n\n"
    guide += f"Monthly Premium: ${health_plan['Monthly Premium']}\n"
    guide += f"Deductible: ${health_plan['Deductible']}\n"
    guide += f"Coverage: {health_plan['Coverage (%)']}%\n"
    guide += f"Network Type: {health_plan['Network Type']}\n"
    guide += "To enroll, visit your provider's website and complete the enrollment process."
    return guide
