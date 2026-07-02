"""
scoring_engine.py

Combines all extracted features
into one final ranking score.
"""

WEIGHTS = {

    "career_score":0.25,

    "skill_score":0.18,

    "semantic_score":0.12,

    "availability_score":0.10,

    "interest_score":0.10,

    "reliability_score":0.08,

    "trust_score":0.07,

    "location_score":0.05,

    "risk_penalty":0.05

}


def final_score(features):

    score = 0

    score += WEIGHTS["career_score"] * features["career_score"]

    score += WEIGHTS["skill_score"] * features["skill_score"]

    score += WEIGHTS["availability_score"] * features["availability_score"]

    score += WEIGHTS["interest_score"] * features["interest_score"]

    score += WEIGHTS["reliability_score"] * features["reliability_score"]

    score += WEIGHTS["trust_score"] * features["trust_score"]

    score += WEIGHTS["location_score"] * features["location_score"]

    score -= WEIGHTS["risk_penalty"] * features["risk_penalty"]

    score += WEIGHTS["semantic_score"] * features["semantic_score"]

    return round(score,2)


