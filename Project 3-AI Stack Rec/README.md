# AI Tech Stack Recommender

## Project 3 - DecodeLabs Internship

This project is a simple AI-based recommendation system that recommends suitable career paths based on the user's skills.

## Objective

The objective of this project is to take user skills as input, compare them with job-role skills, and recommend the most relevant career paths.

## How It Works

1. The user enters three skills.
2. The system reads job-role data from a CSV file.
3. TF-IDF converts skill text into numerical vectors.
4. Cosine Similarity compares the user's skills with each job role.
5. The results are sorted according to similarity scores.
6. The system displays up to three relevant career recommendations.
7. Jobs with a 0% similarity score are not displayed.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

## Project Structure

```text
DecodeLabs_Project3/
│
├── data/
│   └── raw_skills.csv
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation

Install the required libraries using:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

Run:

```bash
python main.py
```

## Example Input

```text
Python
Machine Learning
SQL
```

## Example Output

```text
Top Recommended Career Paths:

Data Scientist - 78.42 %
Machine Learning Engineer - 65.30 %
AI Engineer - 59.81 %
```

The exact similarity scores may change depending on the skills stored in the dataset.

## No Match Case

If the entered skills do not match any job-role skills, the program displays:

```text
No matching career found.
```
