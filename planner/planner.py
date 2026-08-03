from planner.classifier import classify_goal
from planner.scheduler import expected_task_count
from planner.llm import LLMClient
from planner.validator import validate_tasks, ValidationError


class GoalPlanner:

    def __init__(self):
        self.llm = LLMClient()

    def generate_plan(
        self,
        goal: str,
        timeframe: str,
        granularity: str,
        start_date: str | None = None,):
        

        goal_type = classify_goal(goal, timeframe)

        if goal_type == "HARMFUL":
            return {
                "status": "rejected",
                "message": ("I can't help create plans for harmful or illegal activities."),
            }

        if goal_type == "VAGUE":
            return {
                "status": "clarification",
                "message": ("Your goal is too broad. Please make it more specific."),
            }

        if goal_type == "UNREALISTIC":
            return {
                "status": "clarification",
                "message": ("This goal appears unrealistic for the selected timeframe. Try adjusting the goal or timeframe."),
            }


        task_count = expected_task_count(
            timeframe,
            granularity,
        )
        
        tasks = self.llm.generate_tasks(
            goal = goal,
            timeframe = timeframe,
            granularity = granularity,
            expected_tasks = task_count,
        )

        try:

            final_tasks = validate_tasks(
                tasks = tasks,
                expected_count = task_count,
                timeframe = timeframe,
                granularity = granularity,
                start_date = start_date,
            )

        except ValidationError as e:

            return {"status": "error",  "message": str(e),}


        return {
            "status": "success",
            "goal": goal,
            "timeframe": timeframe,
            "granularity": granularity,
            "tasks": final_tasks,
        }