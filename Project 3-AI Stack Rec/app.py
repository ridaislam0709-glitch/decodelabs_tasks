from flask import Flask, render_template, request
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

data = pd.read_csv("data/raw_skills.csv")

vectorizer = TfidfVectorizer()
job_vectors = vectorizer.fit_transform(data["skills"])


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        skill1 = request.form["skill1"]
        skill2 = request.form["skill2"]
        skill3 = request.form["skill3"]

        user_skills = skill1 + " " + skill2 + " " + skill3

        user_vector = vectorizer.transform([user_skills])

        similarity_scores = cosine_similarity(
            user_vector,
            job_vectors
        )[0]

        top_indices = similarity_scores.argsort()[::-1]

        count = 0

        for index in top_indices:

            score = similarity_scores[index] * 100

            if score > 0:

                job_name = data.iloc[index]["job_role"]

                recommendations.append({
                    "job": job_name,
                    "score": round(score, 2)
                })

                count = count + 1

            if count == 3:
                break

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)