"""
risk_analyzer.py

Detects suspicious profiles,
keyword stuffing,
career inconsistencies,
and honeypot-like candidates.
"""

SERVICE_COMPANIES = {

"TCS",
"Infosys",
"Wipro",
"HCL",
"Cognizant",
"Capgemini",
"Accenture",
"Tech Mahindra",
"LTI",
"Mindtree"

}

def service_company_penalty(candidate):

    history = candidate["career_history"]

    total = len(history)

    service = 0

    for job in history:

        if job["company"] in SERVICE_COMPANIES:

            service += 1

    if total == 0:

        return 0

    ratio = service / total

    if ratio >= 0.8:

        return 30

    elif ratio >= 0.5:

        return 15

    return 0


def keyword_stuffing_penalty(candidate):

    skills = candidate["skills"]

    penalty = 0

    advanced = 0

    zero_duration = 0

    for skill in skills:

        if skill["proficiency"].lower() in [

            "advanced",

            "expert"

        ]:

            advanced += 1

        if skill.get("duration_months",0)==0:

            zero_duration += 1

    if advanced>12:

        penalty += 20

    if zero_duration>5:

        penalty += 20

    return penalty

def title_consistency_penalty(candidate):

    title = candidate["profile"]["current_title"].lower()

    summary = candidate["profile"]["summary"].lower()

    penalty = 0

    if "marketing" in title and "retrieval" in summary:

        penalty += 15

    if "hr" in title and "llm" in summary:

        penalty += 15

    if "accountant" in title and "ranking" in summary:

        penalty += 15

    return penalty


def experience_penalty(candidate):

    years = candidate["profile"]["years_of_experience"]

    penalty = 0

    if years<2:

        penalty += 30

    elif years>20:

        penalty += 15

    return penalty


def extract_risk_features(candidate):

    features = {}

    features["service_penalty"] = service_company_penalty(candidate)

    features["keyword_penalty"] = keyword_stuffing_penalty(candidate)

    features["consistency_penalty"] = title_consistency_penalty(candidate)

    features["experience_penalty"] = experience_penalty(candidate)

    features["risk_penalty"] = (

        features["service_penalty"]

        +

        features["keyword_penalty"]

        +

        features["consistency_penalty"]

        +

        features["experience_penalty"]

    )

    return features

    