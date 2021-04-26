import datetime


def add(moment: datetime.datetime):
    gigasecond = datetime.timedelta(seconds=10**9)
    return moment + gigasecond
