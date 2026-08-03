from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from planner.planner import GoalPlanner


app = FastAPI(title = "Planner AI API", version = "1.0.0")


planner = GoalPlanner()


class GoalRequest(BaseModel):
    goal: str
    timeframe: str
    granularity: str
    startDate: Optional[str] = None


@app.get("/")
def home():
    return {"message": "Planner AI API is running."}


@app.post("/generate")
def generate_plan(request: GoalRequest):

    result = planner.generate_plan(goal = request.goal, timeframe = request.timeframe, granularity = request.granularity, start_date = request.startDate)

    return result