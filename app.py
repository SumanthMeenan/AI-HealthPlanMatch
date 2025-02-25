import streamlit as st
import pandas as pd
from src.model import recommend_plan
from src.enrollment_guide import generate_enrollment_guide

# Load data
def load_data():
    members_data = pd.read_csv('data/members.csv')
    plans_data = pd.read_csv('data/health_plans.csv')
    return members_data, plans_data

# Streamlit UI
def app():
    st.title("AI-HealthPlanMatch")
    st.write("Welcome to AI-HealthPlanMatch! Find the best health plan for you.")
    
    # Member profile input
    st.sidebar.header("Enter Member Profile")
    age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
    condition = st.sidebar.selectbox("Pre-existing Condition", ["None", "Diabetes", "Hypertension", "Heart Disease"])
    network_type = st.sidebar.selectbox("Preferred Network", ["PPO", "HMO", "EPO", "POS"])
    budget = st.sidebar.number_input("Budget (monthly)", min_value=0, value=500)
    
    # Get recommendations based on user input
    members_data, plans_data = load_data()
    member_profile = {"Age": age, "Condition": condition, "Network": network_type, "Budget": budget}
    recommended_plan = recommend_plan(member_profile, plans_data)
    
    st.subheader("Recommended Plan")
    st.write(f"**Plan Name:** {recommended_plan['Plan Name']}")
    st.write(f"**Monthly Premium:** ${recommended_plan['Monthly Premium']}")
    st.write(f"**Deductible:** ${recommended_plan['Deductible']}")
    st.write(f"**Coverage:** {recommended_plan['Coverage (%)']}%")
    
    # Generate Enrollment Guide
    guide = generate_enrollment_guide(recommended_plan)
    st.subheader("Enrollment Guide")
    st.write(guide)

if __name__ == "__main__":
    app()
