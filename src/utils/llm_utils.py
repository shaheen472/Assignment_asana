import os


def generate_text(prompt: str) -> str:
    """
    Wrapper for LLM text generation.
    Can be replaced with mock output if no API key.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        # fallback for offline execution
        return "Placeholder generated content based on template."

    # Real implementation would go here
    return "LLM generated content"
