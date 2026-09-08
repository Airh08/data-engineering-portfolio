import datetime
import random

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=random.randint(1, 10000))

def generate_random_datetime(start: datetime.datetime, end: datetime.datetime) -> datetime.datetime:
    """
    Generate a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def test_datetime():
    print("Current date and time: ", now)
    print("Tomorrow's date and time: ", tomorrow)
    
def cast_datetime_to_string(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def cast_string_to_datetime(dt_str: str) -> datetime.datetime:
    return datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

def format_datetime(dt: datetime.datetime) -> str:
    return dt.strftime("%A, %B %d, %Y %I:%M%p")

def datetime_difference(dt1: datetime.datetime, dt2: datetime.datetime) -> datetime.timedelta:
    return dt2 - dt1 

def datetime_add_days(dt: datetime.datetime, days: int) -> datetime.datetime:
    return dt + datetime.timedelta(days=days)

def datetime_subtract_days(dt: datetime.datetime, days: int) -> datetime.datetime:
    return dt - datetime.timedelta(days=days)

def dateme_add_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
    return dt + datetime.timedelta(hours=hours)

def datetime_subtract_hours(dt: datetime.datetime, hours: int) -> datetime.datetime:
    return dt - datetime.timedelta(hours=hours)

def datetime_to_utc(dt: datetime.datetime) -> datetime.datetime:
    return dt.astimezone(datetime.timezone.utc)

def read_file_with_datetime(filename: str) -> list:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

if __name__ == '__main__':
    test_datetime()
    dt_str = cast_datetime_to_string(generate_random_datetime(now, tomorrow))
    print("Current date and time as string: ", dt_str)
    dt_obj = cast_string_to_datetime(dt_str)
    print("String to datetime object: ", dt_obj)
    formatted_dt = format_datetime(generate_random_datetime(now, tomorrow))
    print("Formatted date and time: ", formatted_dt)
    diff = datetime_difference(generate_random_datetime(now, tomorrow), generate_random_datetime(now, tomorrow))
    print("Difference between now and tomorrow: ", diff)
    new_dt = datetime_add_days(generate_random_datetime(now, tomorrow), 5)
    print("Date after adding 5 days: ", new_dt)
    new_dt = datetime_subtract_days(generate_random_datetime(now, tomorrow), 5)
    print("Date after subtracting 5 days: ", new_dt)
    new_dt = dateme_add_hours(generate_random_datetime(now, tomorrow), 5)
    print("Date after adding 5 hours: ", new_dt)
    new_dt = datetime_subtract_hours(generate_random_datetime(now, tomorrow), 5)
    print("Date after subtracting 5 hours: ", new_dt)
    utc_dt = datetime_to_utc(generate_random_datetime(now, tomorrow))
    print("Current date and time in UTC: ", utc_dt)