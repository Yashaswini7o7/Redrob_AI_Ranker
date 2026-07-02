"""
Skill Analyzer

Converts candidate skills into meaningful numerical features.
"""

CORE_AI = {

"Python",

"Machine Learning",

"Deep Learning",

"NLP",

"Transformers",

"LLM",

"Embeddings",

"Retrieval",

"Ranking",

"Recommendation",

"Information Retrieval"

}

VECTOR_DB = {

"FAISS",

"Pinecone",

"Milvus",

"Qdrant",

"Weaviate",

"ElasticSearch",

"OpenSearch"

}

LLM = {

"LoRA",

"QLoRA",

"PEFT",

"Fine-tuning LLMs",

"BERT",

"GPT"

}

PROFICIENCY_SCORE = {

"beginner":1,

"intermediate":2,

"advanced":3,

"expert":4

}

def analyze_skills(candidate):

    skills = candidate["skills"]

    assessments = candidate["redrob_signals"]["skill_assessment_scores"]

    result = {

        "num_skills":0,

        "core_ai_skills":0,

        "vector_db_skills":0,

        "llm_skills":0,

        "skill_strength":0,

        "endorsement_strength":0,

        "duration_strength":0,

        "assessment_strength":0

    }

    result["num_skills"] = len(skills)

    for skill in skills:

        name = skill["name"]

        prof = skill["proficiency"].lower()

        endorse = skill["endorsements"]

        duration = skill.get("duration_months",0)

        result["skill_strength"] += PROFICIENCY_SCORE.get(prof,0)

        result["endorsement_strength"] += endorse

        result["duration_strength"] += duration

        if name in CORE_AI:

            result["core_ai_skills"] += 1

        if name in VECTOR_DB:

            result["vector_db_skills"] += 1

        if name in LLM:

            result["llm_skills"] += 1

        if name in assessments:

            result["assessment_strength"] += assessments[name]

    return result


def skill_score(features):

    score = 0

    score += features["core_ai_skills"]*8

    score += features["vector_db_skills"]*12

    score += features["llm_skills"]*8

    score += min(features["skill_strength"],40)

    score += min(features["assessment_strength"]/5,20)

    score += min(features["endorsement_strength"]/20,10)

    score += min(features["duration_strength"]/50,10)

    return min(score,100)

def extract_skill_features(candidate):

    features = analyze_skills(candidate)

    features["skill_score"] = skill_score(features)

    return features