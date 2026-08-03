import os
from dotenv import load_dotenv
from groq import Groq

from planner.prompts import SYSTEM_PROMPT, build_prompt
from planner.parser import parse_response, ParserError

load_dotenv()

MODEL = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class LLMClient:

    def __init__(self):
        self.client = client
        self.model = MODEL

    def generate_tasks(self, goal: str, timeframe: str, granularity: str, expected_tasks: int, retries: int = 2,):

        prompt = build_prompt(goal, timeframe, granularity, expected_tasks,)
        last_error = None

        for attempt in range(retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model = self.model,
                    temperature = 0.3,
                    messages = [
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT,},
                        {
                            "role": "user",
                            "content": prompt,},],
                )

                content = response.choices[0].message.content

                return parse_response(content)

            except ParserError as e:

                last_error = e

                prompt += f"Your previous response could not be parsed. Error: {e} Return ONLY valid JSON."

        raise Exception(f"Failed after {retries + 1} attempts.\n{last_error}")