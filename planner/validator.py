from planner.scheduler import generate_due_dates


class ValidationError(Exception):
    """Raised when the generated tasks fail validation."""
    pass


def validate_tasks(
    tasks: list,
    expected_count: int,
    timeframe: str,
    granularity: str,
    start_date: str | None = None,):
    
    """ Validate and format the generated tasks.
    Returns:
        [{ "title": "...",  "dueDate": "2026-08-01" }] """

    if not isinstance(tasks, list):
        raise ValidationError("Output must be a list.")

    if len(tasks) != expected_count:
        raise ValidationError(f"Expected {expected_count} tasks but received {len(tasks)}.")

    titles = set()

    due_dates = generate_due_dates(timeframe = timeframe, granularity = granularity, start_date = start_date)

    final_tasks = []

    for i, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise ValidationError("Each task must be an object.")

        title = task.get("title")

        if not title:
            raise ValidationError("Missing task title.")

        title = title.strip()

        if len(title) < 5:
            raise ValidationError(f"Task title too short: {title}")

        key = title.lower()

        if key in titles:
            raise ValidationError(f"Duplicate task: {title}")

        titles.add(key)

        final_tasks.append({"title": title,  "dueDate": due_dates[i],})

    return final_tasks