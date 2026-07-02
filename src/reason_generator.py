"""
reason_generator.py

Generates recruiter-friendly explanations
for every ranked candidate.
"""

def generate_reason(features):

    reasons = []

    if features["career_score"] >= 70:

        reasons.append(
            "Strong production AI experience"
        )

    elif features["career_score"] >= 50:

        reasons.append(
            "Relevant AI engineering background"
        )

    if features["skill_score"] >= 70:

        reasons.append(
            "Excellent AI/ML skill set"
        )

    elif features["skill_score"] >= 50:

        reasons.append(
            "Relevant technical skills"
        )

    if features["availability_score"] >= 70:

        reasons.append(
            "Actively available for opportunities"
        )

    if features["interest_score"] >= 60:

        reasons.append(
            "High recruiter engagement"
        )

    if features["trust_score"] >= 70:

        reasons.append(
            "Well-verified candidate profile"
        )

    if features["location_score"] >= 80:

        reasons.append(
            "Location matches hiring preference"
        )

    if features["risk_penalty"] > 20:

        reasons.append(
            "Minor profile consistency concerns"
        )

    return ". ".join(reasons[:3])