from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

CLASSIFIER_PROMPT = """
You are a goal classifier. Classify the user's goal into exactly ONE category.
VALID
- Specific and achievable.

VAGUE
- Too broad.
Examples:
"Be better"
"Improve myself"

UNREALISTIC
- Impossible or extremely unrealistic within the requested timeframe.
Examples:
"Become fluent in Japanese tomorrow"
"Lose 50 kg in one week"

HARMFUL
- Requests involving violence, crime, self-harm, illegal activity or dangerous acts.

Return ONLY one word: VALID, VAGUE, UNREALISTIC, HARMFUL"""


def classify_goal(goal: str, timeframe: str) -> str:
    """ Returns one of: VALID VAGUE UNREALISTIC HARMFUL """
    response = client.chat.completions.create(
        model = MODEL,
        temperature = 0,
        messages = [{
                "role": "system",
                "content": CLASSIFIER_PROMPT,},
            {
                "role": "user",
                "content": f"Goal:{goal} Timeframe:{timeframe}",},],)

    result = response.choices[0].message.content.strip().upper()

    if result not in {"VALID", "VAGUE", "UNREALISTIC", "HARMFUL",}:
        return "VALID"

    return result