"""
career_analyzer.py

Analyzes a candidate's career history and extracts
career-quality features for ranking.
"""

import re

AI_KEYWORDS = {

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "ml",
    "neural network",
    "transformer",
    "bert",
    "gpt",
    "llm",
    "nlp"

}

RETRIEVAL_KEYWORDS = {

    "retrieval",
    "information retrieval",
    "semantic search",
    "hybrid search",
    "dense retrieval",
    "sparse retrieval",
    "search engine",
    "document retrieval"

}

RANKING_KEYWORDS = {

    "ranking",
    "recommendation",
    "recommendation engine",
    "candidate matching",
    "matching",
    "learning to rank",
    "ltr",
    "ndcg",
    "mrr",
    "map"

}

VECTOR_DB_KEYWORDS = {

    "faiss",
    "milvus",
    "pinecone",
    "qdrant",
    "weaviate",
    "elasticsearch",
    "opensearch"

}

EMBEDDING_KEYWORDS = {

    "embedding",
    "embeddings",
    "sentence transformer",
    "sentence-transformers",
    "bge",
    "e5"

}

PYTHON_KEYWORDS = {

    "python",
    "pandas",
    "numpy",
    "scikit",
    "sklearn",
    "tensorflow",
    "keras",
    "pytorch"

}

EVALUATION_KEYWORDS = {

    "evaluation",
    "offline evaluation",
    "ab testing",
    "a/b testing",
    "ndcg",
    "map",
    "mrr",
    "precision",
    "recall"

}

def count_keywords(text, keywords):

    text = text.lower()

    score = 0

    for word in keywords:

        if word in text:

            score += 1

    return score

def build_career_text(candidate):

    parts = []

    profile = candidate["profile"]

    parts.append(profile["headline"])

    parts.append(profile["summary"])

    for job in candidate["career_history"]:

        parts.append(job["title"])

        parts.append(job["description"])

    return " ".join(parts).lower()


def analyze_career(candidate):

    text = build_career_text(candidate)

    features = {}

    features["ai_mentions"] = count_keywords(
        text,
        AI_KEYWORDS
    )

    features["retrieval_mentions"] = count_keywords(
        text,
        RETRIEVAL_KEYWORDS
    )

    features["ranking_mentions"] = count_keywords(
        text,
        RANKING_KEYWORDS
    )

    features["embedding_mentions"] = count_keywords(
        text,
        EMBEDDING_KEYWORDS
    )

    features["vectordb_mentions"] = count_keywords(
        text,
        VECTOR_DB_KEYWORDS
    )

    features["python_mentions"] = count_keywords(
        text,
        PYTHON_KEYWORDS
    )

    features["evaluation_mentions"] = count_keywords(
        text,
        EVALUATION_KEYWORDS
    )

    return features


def career_score(features):

    score = 0

    score += features["ai_mentions"] * 4

    score += features["retrieval_mentions"] * 10

    score += features["ranking_mentions"] * 12

    score += features["embedding_mentions"] * 8

    score += features["vectordb_mentions"] * 10

    score += features["python_mentions"] * 3

    score += features["evaluation_mentions"] * 8

    return min(score,100)


def extract_career_features(candidate):

    features = analyze_career(candidate)

    features["career_score"] = career_score(features)

    return features