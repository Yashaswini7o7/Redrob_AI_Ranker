"""
semantic_analyzer.py

Computes semantic similarity between
the Job Description and candidate profile.
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

JD_TEXT = """
Senior AI Engineer

Python

Retrieval

Ranking

Embeddings

Vector Database

Recommendation Systems

Machine Learning

LLM

Evaluation

Production AI

Hybrid Search

Semantic Search

NDCG

MRR

MAP
"""

JD_EMBEDDING = model.encode(
    JD_TEXT
)

def candidate_text(candidate):

    profile = candidate["profile"]

    text = []

    text.append(profile.get("headline", ""))

    text.append(profile.get("summary", ""))

    for job in candidate["career_history"]:

        text.append(job.get("title", ""))

        text.append(job.get("description", ""))

    for skill in candidate["skills"]:

        text.append(skill.get("name", ""))

    return " ".join(text)


def semantic_score(candidate):

    text = candidate_text(candidate)

    embedding = model.encode(text)

    similarity = cosine_similarity(

        [JD_EMBEDDING],

        [embedding]

    )[0][0]

    return round(float(similarity*100),2)


def extract_semantic_features(candidate):

    return {

        "semantic_score":

        semantic_score(candidate)

    }