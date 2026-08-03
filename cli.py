import argparse
import json

from planner.planner import GoalPlanner


def main():

    parser = argparse.ArgumentParser(
        description="Planner AI CLI"
    )

    parser.add_argument(
        "--goal",
        required=True,
        help="Goal to achieve"
    )

    parser.add_argument(
        "--timeframe",
        choices=["MONTHLY", "YEARLY"],
        required=True
    )

    parser.add_argument(
        "--granularity",
        choices=["DAILY", "WEEKLY", "MONTHLY"],
        required=True
    )

    parser.add_argument(
        "--start-date",
        default=None,
        help="Start date (YYYY-MM-DD)"
    )

    args = parser.parse_args()

    planner = GoalPlanner()

    result = planner.generate_plan(
        goal=args.goal,
        timeframe=args.timeframe,
        granularity=args.granularity,
        start_date=args.start_date,
    )

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()