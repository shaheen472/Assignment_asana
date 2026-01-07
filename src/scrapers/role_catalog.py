from typing import Dict


def load_role_distribution() -> Dict[str, float]:
    """
    Role distribution modeled after enterprise SaaS orgs.
    """
    return {
        "IC": 0.75,
        "Manager": 0.17,
        "Director": 0.05,
        "Executive": 0.03
    }


def role_to_titles() -> Dict[str, list]:
    """
    Job title templates conditioned on role.
    """
    return {
        "IC": [
            "Software Engineer",
            "Senior Software Engineer",
            "QA Engineer",
            "Product Designer",
            "Data Analyst"
        ],
        "Manager": [
            "Engineering Manager",
            "Product Manager",
            "Marketing Manager",
            "Operations Manager"
        ],
        "Director": [
            "Director of Engineering",
            "Director of Product",
            "Director of Marketing"
        ],
        "Executive": [
            "VP Engineering",
            "VP Product",
            "Chief Technology Officer"
        ]
    }
