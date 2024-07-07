import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizing phone number

    Returns:
        clear phone number without symbols
    """
    clean_number = re.sub(r"[^\d+]", "", phone_number)

    if not clean_number.startswith("+"):
        if clean_number.startswith("380"):
            clean_number = f"+{clean_number}"
        else:
            clean_number = f"+38{clean_number}"

    return clean_number


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "asdqwe345",
    "  as5d dflkg72 /123asd dfg3/ 3451/ 1",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
