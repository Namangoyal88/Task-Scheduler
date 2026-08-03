import json
import re


class ParserError(Exception):
    """Raised when the LLM response cannot be parsed."""
    pass


def extract_json(text: str):
    """Extract the first JSON array or object from the model response."""

    text = text.strip()
    text = re.sub(r"```", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)
    text = re.sub(r"```", "", text, flags=re.IGNORECASE)
    match = re.search(r"\[[\s\S]*\]", text)

    if match:
        return match.group()

    match = re.search(r"\{[\s\S]*\}", text)

    if match:
        return match.group()

    raise ParserError("No JSON found in model response.")


def parse_response(response: str):
    """Parse the LLM response into Python objects."""
    try:
        json_text = extract_json(response)
        return json.loads(json_text)

    except json.JSONDecodeError as e:
        raise ParserError(f"Invalid JSON: {e}") from e