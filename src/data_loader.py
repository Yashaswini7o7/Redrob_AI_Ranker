"""
Loads Redrob candidate dataset.

Author:
Team Redrob
"""

import json


def load_candidates(path):
    """
    Load candidates from jsonl file.

    Parameters
    ----------
    path : str

    Returns
    -------
    list
    """

    candidates = []

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line:

                candidates.append(json.loads(line))

    return candidates