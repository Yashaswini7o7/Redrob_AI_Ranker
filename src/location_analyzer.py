"""
Location scoring
"""

PREFERRED = {

"Pune",

"Noida",

"Delhi",

"Delhi NCR",

"Hyderabad",

"Mumbai"

}

COUNTRY = {"India"}

def extract_location_features(candidate):

    profile = candidate["profile"]

    score = 0

    if profile["country"] in COUNTRY:

        score += 40

    if profile["location"] in PREFERRED:

        score += 40

    if candidate["redrob_signals"]["willing_to_relocate"]:

        score += 20

    return {

        "location_score":score

    }