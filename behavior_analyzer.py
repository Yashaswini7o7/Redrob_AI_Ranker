"""
behavior_analyzer.py

Behavioral scoring using
Redrob platform signals.
"""

from datetime import datetime

def availability_score(signals):

    score = 0

    if signals["open_to_work_flag"]:
        score += 40

    notice = signals["notice_period_days"]

    if notice <= 30:
        score += 30

    elif notice <= 60:
        score += 20

    elif notice <= 90:
        score += 10

    last_active = datetime.strptime(
        signals["last_active_date"],
        "%Y-%m-%d"
    )

    days = (datetime(2026,7,1)-last_active).days

    if days <= 30:

        score += 30

    elif days <= 90:

        score += 20

    elif days <= 180:

        score += 10

    return min(score,100)


def recruiter_interest(signals):

    score = 0

    score += min(
        signals["profile_views_received_30d"]/2,
        20
    )

    score += min(
        signals["saved_by_recruiters_30d"]*3,
        30
    )

    score += min(
        signals["search_appearance_30d"]/10,
        30
    )

    score += signals["recruiter_response_rate"]*20

    return min(score,100)


def reliability_score(signals):

    score = 0

    score += signals["interview_completion_rate"]*50

    offer = signals["offer_acceptance_rate"]

    if offer >= 0:

        score += offer*50

    return min(score,100)


def trust_score(signals):

    score = 0

    if signals["verified_email"]:
        score += 20

    if signals["verified_phone"]:
        score += 20

    if signals["linkedin_connected"]:
        score += 20

    if signals["github_activity_score"] > 0:

        score += min(
            signals["github_activity_score"]/2,
            20
        )

    score += signals["profile_completeness_score"]/5

    return min(score,100)


def extract_behavior_features(candidate):

    s = candidate["redrob_signals"]

    features = {}

    features["availability_score"] = availability_score(s)

    features["interest_score"] = recruiter_interest(s)

    features["reliability_score"] = reliability_score(s)

    features["trust_score"] = trust_score(s)

    return features