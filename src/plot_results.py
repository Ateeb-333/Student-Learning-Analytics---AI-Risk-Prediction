import pandas as pd
import matplotlib.pyplot as plt

# Load predictions
data = pd.read_csv("../data/predictions_recommendations.csv")

# Count predictions
counts = data["Prediction"].value_counts()

# Plot bar chart
plt.figure(figsize=(6, 4))
bars = plt.bar(counts.index, counts.values)
plt.title("Student Risk Distribution")
plt.xlabel("Prediction")
plt.ylabel("Number of Students")

# Add labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', fontsize=12)

plt.tight_layout()
plt.savefig("../data/student_risk_chart.png")
plt.show()

print("✅ Bar chart saved as '../data/student_risk_chart.png'")
