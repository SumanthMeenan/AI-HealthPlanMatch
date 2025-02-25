# 🚀 AI-HealthPlanMatch  
### 🩺 AI-Powered Health Insurance Advisor  

**AI-HealthPlanMatch** is an intelligent health insurance recommendation system that analyzes member profiles and suggests the best health plans using **LLMs** (GPT-4 Turbo). It helps members make informed decisions by providing:  
✅ **Personalized Plan Matching**  
✅ **AI-Generated Enrollment Guides**  
✅ **LLM-Powered Insights on Coverage & Costs**  

---

## 📌 Features  
✔️ Upload member profiles and get **AI-driven insights**  
✔️ Find the **best matching health plan** from available options  
✔️ Generate a **step-by-step enrollment guide**  
✔️ Simple & interactive **Streamlit UI**  

---

## 📂 Data Structure  

### 👤 members.csv (Sample)  
| Member ID | Age | Pre-existing Conditions | Preferred Network | Budget | Employment Status | Family Size |
|-----------|-----|-------------------------|-------------------|--------|-------------------|-------------|
| 101       | 34  | Diabetes                | PPO               | 400    | Employed          | 3           |

### 🏥 health_plans.csv (Sample)  
| Plan ID | Plan Name   | Monthly Premium | Deductible | Coverage (%) | Network Type | Chronic Condition Coverage |
|---------|------------|----------------|------------|--------------|--------------|---------------------------|
| P001    | Silver Plus | 350            | 2000       | 80%          | PPO          | Diabetes, Hypertension   |

---

## 🛠 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/YOUR_USERNAME/AI-HealthPlanMatch.git
cd AI-HealthPlanMatch

### 2️⃣ Install Dependencies
pip install streamlit pandas openai

### 3️⃣ Run the App
streamlit run app.py

⚙️ How It Works
1️⃣ Upload a member profile 🏥
2️⃣ AI analyzes health needs & budget 💡
3️⃣ Finds the best plan based on LLM reasoning 🤖
4️⃣ Generates an enrollment guide for easy signup 📜

🖥️ Demo Screenshot
📸 (Add a screenshot of your Streamlit UI here!)

🚀 Future Enhancements
🔹 Integrate with real-time insurance APIs
🔹 Support for different LLMs (Gemini, Claude, etc.)
🔹 Mobile-friendly UI

🤝 Contributing
Fork the repo 🍴
Create a new branch feature-xyz 🌿
Commit changes & push 🚀
Open a pull request!

📜 License
MIT License

