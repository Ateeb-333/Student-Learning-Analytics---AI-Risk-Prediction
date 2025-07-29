import random

class InterventionAdvisor:
    def __init__(self, predictor_model, classifier_model, features, raw_data):
        self.predictor_model = predictor_model
        self.classifier_model = classifier_model
        self.features = features
        self.raw_data = raw_data
        self.recommendations = {}

    def generate_recommendations(self):
        predictions = self.classifier_model.predict(self.features)

        for i, (student_id, vals) in enumerate(self.features.items()):
            risk = predictions[i]
            if risk == 1:
                # Identify weak topic from raw data
                student_rows = [row for row in self.raw_data.data if row[0] == student_id]
                topic_errors = {}
                for row in student_rows:
                    topic = row[1]
                    is_correct = int(row[5])
                    if topic not in topic_errors:
                        topic_errors[topic] = {"wrong": 0, "total": 0}
                    topic_errors[topic]["total"] += 1
                    if is_correct == 0:
                        topic_errors[topic]["wrong"] += 1

                weak_topic = max(topic_errors, key=lambda t: topic_errors[t]["wrong"], default="General")

                suggestion = random.choice([
                    "review extra materials",
                    "attempt more practice questions",
                    "watch tutorial videos",
                    "schedule a 1-on-1 session"
                ])

                self.recommendations[student_id] = f"Student {student_id} is at risk. Recommend focusing on Topic {weak_topic} and {suggestion}."

        return self.recommendations

    def display_dashboard(self):
        print("\n📌 STUDENT DASHBOARD")
        print("---------------------------------------------------")
        print(f"Total students: {len(self.features)}")
        print(f"Students at risk: {len(self.recommendations)}")
        print("---------------------------------------------------")
        for student_id, rec in self.recommendations.items():
            print(rec)
