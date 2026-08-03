from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def expected_task_count(timeframe: str, granularity: str) -> int:
    """
    Returns the expected number of tasks.
    """

    mapping = {
        ("MONTHLY", "DAILY"): 30,
        ("MONTHLY", "WEEKLY"): 4,
        ("MONTHLY", "MONTHLY"): 1,

        ("YEARLY", "DAILY"): 365,
        ("YEARLY", "WEEKLY"): 52,
        ("YEARLY", "MONTHLY"): 12,
    }

    return mapping.get((timeframe.upper(), granularity.upper()), 0)


def generate_due_dates(
    timeframe: str,
    granularity: str,
    start_date: str | None = None,
):
    """
    Returns a list of ISO formatted due dates.
    """

    if start_date:
        current = datetime.fromisoformat(start_date)
    else:
        current = datetime.today()

    dates = []

    count = expected_task_count(timeframe, granularity)

    if granularity.upper() == "DAILY":

        for _ in range(count):
            dates.append(current.date().isoformat())
            current += timedelta(days=1)

    elif granularity.upper() == "WEEKLY":

        for _ in range(count):
            dates.append(current.date().isoformat())
            current += timedelta(weeks=1)

    elif granularity.upper() == "MONTHLY":

        for _ in range(count):
            dates.append(current.date().isoformat())
            current += relativedelta(months=1)

    return dates