import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
def normalize_conditions(x):
    if isinstance(x, bool) or x is None or pd.isna(x):  # Convert booleans and NaNs to empty lists
        return []
    elif isinstance(x, str):  # Convert comma-separated string to list
        return x.split(", ")
    elif isinstance(x, list):  # Keep lists as is
        return x
    else:
        return []  # Default to empty list

# Function to recommend health plans
def recommend_plan(member_profile, plans_data):
    plans_data = plans_data.copy()
    
    # Normalize 'Chronic Condition Coverage' before checking condition match
    plans_data['Chronic Condition Coverage'] = plans_data['Chronic Condition Coverage'].apply(normalize_conditions)

    # Encode categorical variables
    network_mapping = {'PPO': 0, 'HMO': 1, 'EPO': 2, 'POS': 3}
    plans_data['Network Type'] = plans_data['Network Type'].map(network_mapping)

    # Check if member's condition exists in any plan
    plans_data['Condition Match'] = plans_data['Chronic Condition Coverage'].apply(
        lambda cond_list: 1 if member_profile["Condition"] in cond_list else 0
    )
    
    # Prepare feature vectors for recommendation
    features = ['Monthly Premium', 'Deductible', 'Coverage (%)', 'Network Type', 'Condition Match']
    X = plans_data[features]
    
    # Use Nearest Neighbors for recommendation
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(X)
    
    # Convert member's data into a comparable format
    member_vector = np.array([
        member_profile['Budget'], 
        2000,  # Assuming deductible 
        80,    # Assuming coverage 
        network_mapping[member_profile['Network']], 
        1  # Assume condition match is relevant
    ]).reshape(1, -1)
    
    # Find nearest plan
    _, indices = knn.kneighbors(member_vector)
    
    # Return recommended plan
    return plans_data.iloc[indices[0][0]].to_dict()
