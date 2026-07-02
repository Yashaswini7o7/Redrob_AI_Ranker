from career_analyzer import extract_career_features

from skill_analyzer import extract_skill_features

from behavior_analyzer import extract_behavior_features

from location_analyzer import extract_location_features

from risk_analyzer import extract_risk_features

from semantic_analyzer import extract_semantic_features

def extract_features(candidate):

    features = {}

    features.update(
        extract_career_features(candidate)
    )

    features.update(
        extract_skill_features(candidate)
    )

    features.update(
        extract_behavior_features(candidate)
    )

    features.update(
        extract_location_features(candidate)
    )

    features.update(
        extract_risk_features(candidate)
    )

    features.update(
        extract_semantic_features(candidate)
    )

    return features