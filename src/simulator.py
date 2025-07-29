import random
import csv
from datetime import datetime, timedelta

class Student:
    def __init__(self, student_id, aptitude, learning_style):
        self.student_id = student_id
        self.aptitude = aptitude
        self.learning_style = learning_style
        self.engagement = random.uniform(0.6, 1.0)

class CourseTopic:
    def __init__(self, topic_id, name, difficulty):
        self.topic_id = topic_id
        self.name = name
        self.difficulty = difficulty

class Question:
    def __init__(self, question_id, topic, difficulty):
        self.question_id = question_id
        self.topic = topic
        self.difficulty = difficulty

class LearningSimulator:
    def __init__(self, num_students=50, days=30):
        self.students = []

        # ✅ Force 30% students to be safe performers
        safe_students = int(num_students * 0.3)
        risky_students = num_students - safe_students

        # High aptitude students (Safe group)
        for i in range(1, safe_students + 1):
            self.students.append(Student(i, random.uniform(0.8, 1.0), random.choice(["visual", "auditory"])))

        # Lower aptitude students (At-risk group)
        for i in range(safe_students + 1, num_students + 1):
            self.students.append(Student(i, random.uniform(0.3, 0.6), random.choice(["visual", "auditory"])))

        self.topics = [
            CourseTopic(i, f"Topic_{i}", random.uniform(0.3, 0.9))
            for i in range(1, 6)
        ]
        self.questions = [
            Question(i, random.choice(self.topics), random.uniform(0.3, 0.9))
            for i in range(1, 101)
        ]
        self.days = days
        self.data = []

    def simulate(self):
        timestamp = datetime.now()
        for day in range(self.days):
            for student in self.students:
                attempts = random.randint(5, 12)
                for _ in range(attempts):
                    q = random.choice(self.questions)

                    # ✅ SAFE students: Always correct
                    if student.aptitude > 0.7:
                        is_correct = 1  # Safe students always succeed
                    else:
                        # Risky students answer 20-50% correctly
                        is_correct = 1 if random.random() < random.uniform(0.2, 0.5) else 0

                    time_spent = random.randint(20, 300)
                    self.data.append([
                        student.student_id, q.topic.topic_id, q.question_id,
                        timestamp.strftime("%Y-%m-%d"), time_spent, is_correct
                    ])
            timestamp += timedelta(days=1)

    def save_to_csv(self, filename="../data/simulated_data.csv"):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["student_id", "topic_id", "question_id", "date", "time_spent", "is_correct"])
            writer.writerows(self.data)
