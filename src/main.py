import os
import pandas as pd
from dataframe import LearningLogDataFrame
from simulator import LearningSimulator
from feature_engineering import StudentFeatureExtractor
from predictor import PerformancePredictor, RiskClassifier
from advisor import InterventionAdvisor
from fpdf import FPDF
import matplotlib.pyplot as plt

DATA_FILE = "../data/simulated_data.csv"
OUTPUT_FILE = "../data/predictions_recommendations.csv"

# 1️⃣ Load or Simulate Data
df = LearningLogDataFrame(["student_id", "topic_id", "question_id", "date", "time_spent", "is_correct"])

if not os.path.exists(DATA_FILE):
    print("✅ No dataset found. Simulating new data...")
    simulator = LearningSimulator()
    simulator.simulate()
    simulator.save_to_csv(DATA_FILE)
    print("✅ New data simulated and saved!")

df.load_from_csv(DATA_FILE)
record_count = getattr(df, "data", None)
if record_count is not None:
    print(f"✅ Loaded data from {DATA_FILE} with {len(df.data)} records.")
else:
    print(f"✅ Loaded data from {DATA_FILE}")

print("✅ Data loaded successfully!")

# 2️⃣ Feature Extraction
extractor = StudentFeatureExtractor(df)
features = extractor.extract_features()   # ✅ Already returns DataFrame

# 3️⃣ Train Models
print("\n🔹 Training regression model (score predictor)...")
reg_model = PerformancePredictor()
reg_model.train(features)
print("Evaluation:", reg_model.evaluate(features))

print("\n🔹 Training classification model (risk detector)...")
clf_model = RiskClassifier()
clf_model.train(features)
clf_eval = clf_model.evaluate(features)
print("Evaluation:", clf_eval)

predictions = clf_model.predict(features)
students = list(features.index)

# Count
safe_count = sum(1 for p in predictions if p == 0)
risk_count = sum(1 for p in predictions if p == 1)

# 4️⃣ Generate Recommendations
advisor = InterventionAdvisor(reg_model, clf_model, features, df)
recommendations = advisor.generate_recommendations()

# 5️⃣ Save Results
output_data = []
for student, pred in zip(students, predictions):
    rec = recommendations.get(student, "Student is safe and performing well.")
    output_data.append({"Student_ID": student, "Prediction": "At-risk" if pred == 1 else "Safe", "Recommendation": rec})

pd.DataFrame(output_data).to_csv(OUTPUT_FILE, index=False)
print(f"\n📂 Results saved to: {OUTPUT_FILE}")

# 6️⃣ Bar Chart
data = pd.DataFrame(output_data)
counts = data["Prediction"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(counts.index, counts.values, color=['green', 'red'])
plt.title("Student Risk Distribution")
plt.xlabel("Prediction")
plt.ylabel("Number of Students")
plt.savefig("../data/student_risk_chart.png")
print("📊 Bar chart saved to ../data/student_risk_chart.png")

# 7️⃣ PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Student Risk Prediction Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=10)
for row in output_data:
    pdf.multi_cell(0, 10, f"Student ID: {row['Student_ID']}\nStatus: {row['Prediction']}\nRecommendation: {row['Recommendation']}\n", border=1)
pdf.output("../data/student_report.pdf")
print("📜 PDF report saved to ../data/student_report.pdf")

# 8️⃣ Dashboard
print("\n📊 FINAL DASHBOARD")
print("---------------------------------------------------")
print(f"Total students: {len(students)}")
print(f"✅ Safe students: {safe_count}")
print(f"⚠️ At-risk students: {risk_count}")
print("---------------------------------------------------")
for row in output_data[:5]:
    print(f" - {row['Recommendation']}")
print("---------------------------------------------------")
print("✅ Process Completed Successfully!")
