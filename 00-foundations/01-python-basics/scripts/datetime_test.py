import datetime

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

def test_datetime():
    print("Current date and time: ", now)
    print("Tomorrow's date and time: ", tomorrow)

if __name__ == '__main__':
    test_datetime() 