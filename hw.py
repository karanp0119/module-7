from datetime import datetime
from datetime import timedelta


def main():
    data = datetime.now().time()
    dt = datetime.now()  # stores current time in the variable dt
    print("current time is " + str(data))

    minus = dt - timedelta(seconds=60)  # stores current time minus sixty seconds
    print("minus 60 seconds is " + str(minus))

    add = dt + timedelta(days=730)  # stores current time plus two years
    print("plus two years is " + str(add))

    d = timedelta(days=100) + timedelta(hours=10) + timedelta(minutes=13)  # stores days, hour and minutes
    print(d)

    datetime_object = datetime.now()
    print(datetime_object)
    print('Type :- ', type(datetime_object))


if __name__ == "__main__":
    main()
