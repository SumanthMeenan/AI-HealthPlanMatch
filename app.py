import streamlit as st
import pandas as pd
from src.model import recommend_plan
from src.enrollment_guide import generate_enrollment_guide

# Load data
@st.cache_data
def load_data():
    try:
        members_data = pd.read_csv('data/members.csv')
        plans_data = pd.read_csv('data/health_plans.csv')
        return members_data, plans_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

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
    if members_data is None or plans_data is None:
        return  # Exit if there's an error in loading the data
    
    member_profile = {"Age": age, "Condition": condition, "Network": network_type, "Budget": budget}
    
    # Button to trigger plan recommendation and guide generation
    if st.button("Generate Plan Recommendation"):
        # Fetching recommended plan based on member's profile
        recommended_plan = recommend_plan(member_profile, plans_data)
        
        if recommended_plan is not None:
            st.subheader("Recommended Plan")
            st.write(f"**Plan Name:** {recommended_plan['Plan Name']}")
            st.write(f"**Monthly Premium:** ${recommended_plan['Monthly Premium']}")
            st.write(f"**Deductible:** ${recommended_plan['Deductible']}")
            st.write(f"**Coverage:** {recommended_plan['Coverage (%)']}%")
            
            # Generate and display enrollment guide
            guide = generate_enrollment_guide(recommended_plan)
            st.subheader("Enrollment Guide")
            st.write(guide)
        else:
            st.error("Unable to fetch plan recommendations. Please check your input data.")

if __name__ == "__main__":
    app()
