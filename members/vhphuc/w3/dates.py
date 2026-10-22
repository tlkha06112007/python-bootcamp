from datetime import date, datetime, timedelta

def parse_due(text: str, today: date) -> date:
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        pass

    if text == "tomorrow":
        return today + timedelta(days=1)

    if text.startswith("in ") and text.endswith(" days"):
        parts = text.split()
        if len(parts) == 3 and parts[1].isdigit():
            return today + timedelta(days=int(parts[1]))

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if text in weekdays:
        target_weekday = weekdays.index(text)
        current_weekday = today.weekday()
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")