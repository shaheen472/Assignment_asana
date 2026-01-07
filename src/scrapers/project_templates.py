from typing import Dict, List


def load_project_templates() -> Dict[str, List[str]]:
    """
    Project name patterns derived from:
    - Public Asana templates
    - GitHub project boards
    - SaaS quarterly planning norms
    """
    return {
        "Engineering": [
            "Q{quarter} Platform Stability Improvements",
            "API Performance Optimization – Phase {phase}",
            "Security Hardening Initiative",
            "Backend Refactor for Scalability",
            "Release {version} Engineering Execution"
        ],
        "Product": [
            "Product Roadmap Q{quarter}",
            "Feature Discovery & Validation",
            "UX Revamp – Phase {phase}",
            "Customer Feedback Integration"
        ],
        "Marketing": [
            "Product Launch Campaign – Q{quarter}",
            "Website Conversion Optimization",
            "Brand Messaging Refresh",
            "Demand Generation Sprint"
        ],
        "Operations": [
            "Compliance Audit Preparation",
            "Internal Tooling Automation",
            "Infrastructure Cost Optimization",
            "Security Policy Review"
        ]
    }
