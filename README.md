Student Learning Analytics - AI Risk Prediction
📌 Project Overview
This project uses AI-driven analytics to predict students at risk of underperforming based on their learning activity data. It extracts behavioral features from simulated or real datasets, applies machine learning models to predict risk levels, and provides personalized recommendations for intervention.
🚀 Features

- Data Simulation: Generates synthetic learning data if no dataset is provided.
- Feature Engineering: Extracts features such as accuracy rate, time spent, activity recency, and test scores.
- Machine Learning Models: Predicts performance and detects at-risk students using Decision Tree classifiers.
- Personalized Recommendations: Suggests actions for improving student learning outcomes.
- Visual Dashboard: Bar chart showing safe vs at-risk students.
- Report Generation: Saves results to CSV and generates a PDF report for detailed analysis.

📂 Project Structure

- src/
    - main.py (Main script to run the entire project)
    - simulator.py (Simulates learning activity data)
    - dataframe.py (Custom class for handling learning logs)
    - feature_engineering.py (Extracts features for ML models)
    - predictor.py (Trains regression and classification models)
    - advisor.py (Generates personalized recommendations)
- data/
    - simulated_data.csv (Generated dataset)
    - predictions_recommendations.csv (Prediction results)
    - student_report.pdf (Generated report)
- requirements.txt (Python dependencies)
- README.md (Project documentation)

⚙️ Installation

1. Clone this repository:
   git clone https://github.com/Ateeb-333/Student-Learning-Analytics---AI-Risk-Prediction.git
2. Navigate to project folder:
   cd Student-Learning-Analytics---AI-Risk-Prediction/src
3. Install required dependencies:
   pip install -r requirements.txt

▶️ Usage

1. Run the main script:
   python main.py
2. The program will:
   - Load or simulate data
   - Train models
   - Predict at-risk students
   - Save CSV, PDF report, and visualization chart in /data folder

📊 Output

- predictions_recommendations.csv: List of students, their risk status, and recommendations
- student_risk_chart.png: Visualization of safe vs at-risk students
- student_report.pdf: Detailed student-level recommendations

🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.
📜 License
This project is licensed under the MIT License - you are free to use and modify it.
