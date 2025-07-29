import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime

class StudentFeatureExtractor:
    def __init__(self, df):
        """
        df: LearningLogDataFrame object
        Expected to have a pandas DataFrame accessible as df.df or similar
        """
        # Try to access the actual DataFrame
        self.data = getattr(df, "data", None) or getattr(df, "df", None)

    def extract_features(self):
        """
        Extracts student-level features and generates a synthetic 'score' column
        for regression prediction.
        """
        features = defaultdict(dict)

        # Ensure data exists
        if self.data is None or len(self.data) == 0:
            print("⚠️ No data available for feature extraction.")
            return pd.DataFrame()

        # Group data by student
        grouped = self.data.groupby("student_id")

        for student_id, group in grouped:
            total_questions = len(group)
            correct_answers = group["is_correct"].sum()

            # Accuracy rate
            accuracy_rate = correct_answers / total_questions if total_questions > 0 else 0

            # Average time spent
            avg_time_spent = group["time_spent"].mean() if total_questions > 0 else 0

            # Active days
            active_days = group["date"].nunique()

            # Time since last activity (days)
            try:
                last_date = pd.to_datetime(group["date"]).max()
                time_since_last_activity = (datetime.now() - last_date).days
            except Exception:
                time_since_last_activity = 0

            # Practice test score (simulated)
            practice_test_score = np.random.uniform(0.3, 1.0)

            # Synthetic score for regression
            score = (accuracy_rate * 0.6 + practice_test_score * 0.4) * 100

            features[student_id] = {
                "accuracy_rate": float(accuracy_rate),
                "avg_time_spent": float(avg_time_spent),
                "active_days": int(active_days),
                "time_since_last_activity": int(time_since_last_activity) * -1,
                "practice_test_score": float(practice_test_score),
                "score": float(score)
            }

        # Convert to DataFrame
        features_df = pd.DataFrame.from_dict(features, orient="index")
        print("✅ Features extracted successfully with 'score' column.")
        return features_df
