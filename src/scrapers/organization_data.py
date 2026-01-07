from typing import Dict


def load_organization() -> Dict[str, str]:
    """
    Curated real-world organization reference.
    Source: Public company information (Veeva Systems).
    """
    return {
        "name": "Veeva Systems",
        "domain": "veeva.com",
        "industry": "Enterprise SaaS",
        "employee_range": "5000-10000",
        "headquarters": "Pleasanton, California",
        "business_model": "B2B SaaS"
    }
