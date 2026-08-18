import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = pd.read_csv("data/raw_skills.csv")

#print(data)
print("\n--- Tech Stack Recommender ---")

skill1 = input("Enter your first skill: ")
skill2 = input("Enter your second skill: ")
skill3 = input("Enter your third skill: ")

user_skills = skill1 + " " + skill2 + " " + skill3

print("Your skills:", user_skills)
vectorizer = TfidfVectorizer()
job_vectors = vectorizer.fit_transform(data["skills"])
user_vector = vectorizer.transform([user_skills])
similarity_scores = cosine_similarity(user_vector, job_vectors)[0]

#print("Similarity Scores:", similarity_scores)
top_indices = similarity_scores.argsort()[::-1][:3]
similarity_scores.argsort()

top_indices = similarity_scores.argsort()[::-1]

print("\nTop Recommended Career Paths:")

count = 0

for index in top_indices:
    score = similarity_scores[index] * 100

    if score > 0:
        job_name = data.iloc[index]["job_role"]
        print(job_name, "-", round(score, 2), "%")

        count = count + 1

    if count == 3:
        break

if count == 0:
    print("No matching career found.")