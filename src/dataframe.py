import pandas as pd

class LearningLogDataFrame:
    def __init__(self, columns=None):
        """
        Initialize the learning log dataframe.
        """
        if columns is None:
            columns = ["student_id", "topic_id", "question_id", "date", "time_spent", "is_correct"]
        self.df = pd.DataFrame(columns=columns)

    def load_from_csv(self, filename):
        """
        Load student learning data from a CSV file.
        """
        try:
            self.df = pd.read_csv(filename)
            print(f"✅ Loaded data from {filename} with {len(self.df)} records.")
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
        except Exception as e:
            print(f"⚠️ Error loading CSV: {e}")

    def save_to_csv(self, filename):
        """
        Save the dataframe to a CSV file.
        """
        try:
            self.df.to_csv(filename, index=False)
            print(f"✅ Data saved to {filename}")
        except Exception as e:
            print(f"⚠️ Error saving CSV: {e}")

    def add_log(self, student_id, topic_id, question_id, date, time_spent, is_correct):
        """
        Add a new learning log entry to the dataframe.
        """
        new_row = {
            "student_id": student_id,
            "topic_id": topic_id,
            "question_id": question_id,
            "date": date,
            "time_spent": time_spent,
            "is_correct": is_correct
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_unique_students(self):
        """
        Get a list of all unique student IDs.
        """
        if "student_id" not in self.df.columns:
            raise ValueError("❌ Column 'student_id' not found in dataframe.")
        return self.df["student_id"].unique().tolist()

    def get_student_logs(self, student_id):
        """
        Get all learning log records for a specific student.
        """
        if "student_id" not in self.df.columns:
            raise ValueError("❌ Column 'student_id' not found in dataframe.")
        return self.df[self.df["student_id"] == student_id]

    def get_data(self):
        """
        Return the entire dataframe.
        """
        return self.df

    def print_summary(self):
        """
        Print a summary of the dataset.
        """
        print("\n📊 DATA SUMMARY")
        print(self.df.describe(include='all'))
