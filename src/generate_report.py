import pandas as pd
from fpdf import FPDF

# Load predictions
data = pd.read_csv("../data/predictions_recommendations.csv")

# Save Excel report
excel_path = "../data/student_report.xlsx"
data.to_excel(excel_path, index=False)
print(f"✅ Excel report saved: {excel_path}")

# Create PDF report
pdf_path = "../data/student_report.pdf"

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(200, 10, "Student Risk Prediction Report", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=10)

for idx, row in data.iterrows():
    pdf.multi_cell(0, 10, f"Student ID: {row['Student_ID']}\nStatus: {row['Prediction']}\nRecommendation: {row['Recommendation']}\n", border=1)
    pdf.ln(2)

pdf.output(pdf_path)
print(f"✅ PDF report saved: {pdf_path}")
