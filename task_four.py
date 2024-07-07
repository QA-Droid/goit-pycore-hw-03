from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Calculation of colleagues' birthdays

    Returns:
        upcoming colleagues' birthdays
    """
    today = datetime.today().date()
    delta_week = today + timedelta(days=7)

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # if birthday_this_year.weekday() == 5:
        #    birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day+2)
        # elif birthday_this_year.weekday() == 6:
        #    birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day+1)

        if birthday_this_year.weekday() in [5, 6]:
            birthday_this_year = birthday_this_year.replace(
                day=birthday_this_year.day + (7 - birthday_this_year.weekday())
            )

        if birthday_this_year <= delta_week:
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.1"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice", "birthday": "1990.07.07"},
    {"name": "Ronny", "birthday": "1990.07.10"},
    {"name": "Vadik", "birthday": "1990.07.12"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
