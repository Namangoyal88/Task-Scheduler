import json
import re


class ParserError(Exception):
    """Raised when the LLM response cannot be parsed."""
    pass


def extract_json(text: str):
    text = re.sub(r"```json|```", "", text, flags=re.IGNORECASE).strip()

    decoder = json.JSONDecoder()

    for i, ch in enumerate(text):
        if ch in "[{":
            try:
                obj, end = decoder.raw_decode(text[i:])
                return text[i:i+end]
            except json.JSONDecodeError:
                pass

    raise ParserError("No valid JSON found.")


def parse_response(response: str):
    """Parse the LLM response into Python objects."""
    try:
        json_text = extract_json(response)
        return json.loads(json_text)

    except json.JSONDecodeError as e:
        raise ParserError(f"Invalid JSON: {e}") from e