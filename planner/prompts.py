SYSTEM_PROMPT = """
You are an expert productivity coach.

Your task is to convert a user's goal into a structured list of actionable tasks.

Rules:

1. Return ONLY valid JSON.
2. No markdown.
3. No explanations.
4. Every task must be specific and actionable.
5. Never restate the goal.
6. Never generate duplicate tasks.
7. Titles should be concise (5-12 words).
8. Follow the requested task count exactly.
9. Dates must NOT be generated.
10. If the goal is harmful, return:

{
    "status":"rejected",
    "reason":"harmful"
}

11. If the goal is too vague, return:

{
    "status":"clarification",
    "reason":"vague"
}

12. If the goal is unrealistic, return:

{
    "status":"clarification",
    "reason":"unrealistic"
}
"""


def build_prompt(goal: str,
                 timeframe: str,
                 granularity: str,
                 expected_tasks: int):

    return f"""
Goal:
{goal}

Timeframe:
{timeframe}

Granularity:
{granularity}

Generate exactly {expected_tasks} tasks.

Return ONLY JSON.

Example:

[
    {{
        "title":"Learn greetings and introductions"
    }},
    {{
        "title":"Practice present tense verbs"
    }}
]
"""