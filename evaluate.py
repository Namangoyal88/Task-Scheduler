import json
import os

from planner.planner import GoalPlanner

planner = GoalPlanner()

with open("tests/sample_inputs.json", "r") as f:
    TEST_CASES = json.load(f)


def score_output(result):
    """
    Simple rubric scoring.
    """

    if result["status"] != "success":
        return {
            "score": 0,
            "remarks": result["message"]
        }

    tasks = result["tasks"]

    score = 0
    remarks = []

    score += 1

    if len(tasks) > 0:
        score += 1
    else:
        remarks.append("No tasks generated")

    titles = [task["title"].lower() for task in tasks]

    if len(titles) == len(set(titles)):
        score += 1
    else:
        remarks.append("Duplicate tasks")

    if all("dueDate" in task for task in tasks):
        score += 1
    else:
        remarks.append("Missing due dates")

    if all(len(task["title"]) >= 5 for task in tasks):
        score += 1
    else:
        remarks.append("Very short titles")

    return {
        "score": score,
        "remarks": remarks
    }


def evaluate():

    results = []

    for case in TEST_CASES:

        output = planner.generate_plan(**case)

        results.append(
            {
                "input": case,
                "output": output,
                "evaluation": score_output(output)
            }
        )

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/evaluation.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Evaluation completed.")
    print("Saved to outputs/evaluation.json")


if __name__ == "__main__":
    evaluate()