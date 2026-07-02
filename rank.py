"""
rank.py

Main pipeline for the Redrob Candidate Ranking Challenge.

Loads all candidates,
extracts features,
scores candidates,
generates reasoning,
creates submission.csv
"""

import os
import sys
import json
import pandas as pd
from tqdm import tqdm

sys.path.append(os.path.abspath("src"))

from data_loader import load_candidates
from feature_extractor import extract_features
from scoring_engine import final_score
from reason_generator import generate_reason

DATA_PATH = "data/candidates.jsonl"

OUTPUT_PATH = "output/submission.csv"

print("Loading candidates...")

candidates = load_candidates(DATA_PATH)

print(f"Loaded {len(candidates)} candidates.")

results = []

print("Scoring candidates...")

for candidate in tqdm(candidates):

    features = extract_features(candidate)

    score = final_score(features)

    reason = generate_reason(features)

    results.append({

        "candidate_id": candidate["candidate_id"],

        "score": score,

        "reasoning": reason

    })


df = pd.DataFrame(results)

df = df.sort_values(

    by=["score","candidate_id"],

    ascending=[False,True]

)

df = df.head(100).reset_index(drop=True)

df["rank"] = range(1,101)

df = df[[

    "candidate_id",

    "rank",

    "score",

    "reasoning"

]]

os.makedirs("output",exist_ok=True)

df.to_csv(

    OUTPUT_PATH,

    index=False

)

print("Submission saved.")

print(df.head())