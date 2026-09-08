import datetime
import random
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

UTC = datetime.timezone.utc
now = datetime.datetime.now(UTC)
random_future_datetime = now + datetime.timedelta(days=random.randint(1, 10000))


def generate_random_datetime(
    start: datetime.datetime, end: datetime.datetime
) -> datetime.datetime:
    """
    Generate a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = int(delta.total_seconds())
    if int_delta <= 0:
        raise ValueError("The end datetime must be after the start datetime")
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def test_datetime():
    print("Current UTC datetime: ", now)
    print("Random future datetime: ", random_future_datetime)


def date_and_time_examples() -> None:
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    print("Date: ", current_date)
    print("Time: ", current_time)


def cast_datetime_to_string(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def cast_string_to_datetime(dt_str: str) -> datetime.datetime:
    return datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")


def parse_iso_datetime(iso_string: str) -> datetime.datetime:
    """Parse ISO 8601, including a trailing Z for UTC."""
    normalized = iso_string[:-1] + "+00:00" if iso_string.endswith("Z") else iso_string
    return datetime.datetime.fromisoformat(normalized)


def format_iso_with_z(dt: datetime.datetime) -> str:
    """Format an aware UTC datetime using the explicit Z suffix."""
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("A timezone-aware datetime is required")
    utc_datetime = dt.astimezone(UTC)
    return utc_datetime.isoformat().replace("+00:00", "Z")


def format_datetime(dt: datetime.datetime) -> str:
    return dt.strftime("%A, %B %d, %Y %I:%M%p")


def datetime_difference(dt1: datetime.datetime, dt2: datetime.datetime) -> datetime.timedelta:
    return dt2 - dt1


def compare_datetimes(dt1: datetime.datetime, dt2: datetime.datetime) -> int:
    """Compare two compatible datetimes: -1, 0, or 1."""
    dt1_is_aware = dt1.tzinfo is not None and dt1.utcoffset() is not None
    dt2_is_aware = dt2.tzinfo is not None and dt2.utcoffset() is not None
    if dt1_is_aware != dt2_is_aware:
        raise ValueError("Cannot compare naive and timezone-aware datetimes")
    return (dt1 > dt2) - (dt1 < dt2)


def is_within_interval(
    value: datetime.datetime,
    start: datetime.datetime,
    end: datetime.datetime,
) -> bool:
    """Return whether value is inside the inclusive interval."""
    if start > end:
        raise ValueError("The interval start must be before its end")
    return start <= value <= end


def parse_date(date_string: str) -> datetime.date:
    """Parse a date and expose invalid calendar values as ValueError."""
    return datetime.date.fromisoformat(date_string)


def datetime_add_days(dt: datetime.datetime, days: int) -> datetime.datetime:
    return dt + datetime.timedelta(days=days)


def datetime_subtract_days(dt: datetime.datetime, days: int) -> datetime.datetime:
    return dt - datetime.timedelta(days=days)


def datetime_add_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
    return dt + datetime.timedelta(hours=hours)


def datetime_subtract_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
    return dt - datetime.timedelta(hours=hours)


def datetime_to_utc(dt: datetime.datetime) -> datetime.datetime:
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("A timezone-aware datetime is required")
    return dt.astimezone(datetime.timezone.utc)


def show_zoneinfo_conversion(dt: datetime.datetime) -> None:
    try:
        madrid = dt.astimezone(ZoneInfo("Europe/Madrid"))
    except ZoneInfoNotFoundError:
        print("Europe/Madrid timezone data is unavailable")
    else:
        local = dt.astimezone()
        print("UTC: ", dt)
        print("Local timezone: ", local)
        print("Europe/Madrid: ", madrid)


def read_file_with_datetime(filename: str) -> list:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

if __name__ == '__main__':
    test_datetime()
    date_and_time_examples()
    dt_str = cast_datetime_to_string(generate_random_datetime(now, random_future_datetime))
    print("Current date and time as string: ", dt_str)
    dt_obj = cast_string_to_datetime(dt_str)
    print("String to datetime object: ", dt_obj)
    iso_dt = parse_iso_datetime("2026-09-08T12:30:00Z")
    print("ISO 8601 with Z: ", iso_dt)
    print("Formatted ISO with Z: ", format_iso_with_z(iso_dt))
    formatted_dt = format_datetime(generate_random_datetime(now, random_future_datetime))
    print("Formatted date and time: ", formatted_dt)
    diff = datetime_difference(
        generate_random_datetime(now, random_future_datetime),
        generate_random_datetime(now, random_future_datetime),
    )
    print("Difference between random datetimes: ", diff)
    new_dt = datetime_add_days(generate_random_datetime(now, random_future_datetime), 5)
    print("Date after adding 5 days: ", new_dt)
    new_dt = datetime_subtract_days(generate_random_datetime(now, random_future_datetime), 5)
    print("Date after subtracting 5 days: ", new_dt)
    new_dt = datetime_add_hours(generate_random_datetime(now, random_future_datetime), 5)
    print("Date after adding 5 hours: ", new_dt)
    new_dt = datetime_subtract_hours(generate_random_datetime(now, random_future_datetime), 5)
    print("Date after subtracting 5 hours: ", new_dt)
    madrid_dt = iso_dt.astimezone(ZoneInfo("Europe/Madrid"))
    print("Comparison with same instant: ", compare_datetimes(iso_dt, madrid_dt))
    print("Inside interval: ", is_within_interval(iso_dt, now, random_future_datetime))
    print("Parsed date: ", parse_date("2026-09-08"))
    try:
        parse_date("2026-02-30")
    except ValueError as error:
        print("Invalid date: ", error)
    naive_dt = datetime.datetime(2026, 9, 8, 12, 30)
    try:
        compare_datetimes(naive_dt, iso_dt)
    except ValueError as error:
        print("Naive/aware mismatch: ", error)
    show_zoneinfo_conversion(iso_dt)