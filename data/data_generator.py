import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake names and details
fake = Faker()

# List of possible chronic conditions and network types
chronic_conditions = ['Diabetes', 'Hypertension', 'Asthma', 'Heart Disease', 'None']
network_types = ['PPO', 'HMO', 'EPO', 'POS']
coverage_percentages = [80, 85, 90, 95]

# Function to generate random member data
def generate_member_data(num_members):
    members = []
    for _ in range(num_members):
        name = fake.name()
        age = random.randint(18, 70)
        budget = random.randint(150, 1200)  # Monthly budget
        network = random.choice(network_types)
        condition = random.choice(chronic_conditions)
        
        members.append({
            'ID': fake.uuid4(),
            'Name': name,
            'Age': age,
            'Budget': budget,
            'Network': network,
            'Condition': condition
        })
    
    return pd.DataFrame(members)

# Function to generate random health plan data
def generate_health_plans(num_plans):
    plans = []
    for _ in range(num_plans):
        plan_name = f"Plan {fake.company()}"
        premium = random.randint(200, 1500)  # Monthly premium
        deductible = random.randint(500, 5000)
        coverage = random.choice(coverage_percentages)
        network = random.choice(network_types)
        chronic_condition_coverage = random.choice([True, False])
        
        plans.append({
            'Plan ID': fake.uuid4(),
            'Plan Name': plan_name,
            'Monthly Premium': premium,
            'Deductible': deductible,
            'Coverage (%)': coverage,
            'Network Type': network,
            'Chronic Condition Coverage': chronic_condition_coverage
        })
    
    return pd.DataFrame(plans)

# Generate 1000 members and 10 health plans
members_data = generate_member_data(1000)
health_plans_data = generate_health_plans(10)

# Save to CSV files
members_data.to_csv('data/members.csv', index=False)
health_plans_data.to_csv('data/health_plans.csv', index=False)

print("Sample data for members and health plans has been generated and saved to CSV.")
