from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculates time delta between now and date

    Returns:
        Days difference between dates
    """
    date_now = datetime.now()
    try:
        date_given = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Incorrect date format passed, expected YYYY-MM-DD, received {date}")
    else:
        return (date_now.toordinal() - date_given.toordinal())