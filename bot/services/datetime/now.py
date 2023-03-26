from datetime import datetime
from locale import setlocale, LC_ALL, Error
from pytz import timezone


def now_us():
    try:
        setlocale(LC_ALL, "en_US.UTF-8")
    except Error:
        print("Unsupported locale: en_US.UTF-8")
        return None
    now = datetime.now()
    return now.strftime("%A, %d %B %Y %H:%M:%S")


def now_ca():
    try:
        setlocale(LC_ALL, "en_CA.UTF-8")
    except Error:
        print("Unsupported locale: en_CA.UTF-8")
        return None
    now = datetime.now(timezone("Canada/Eastern"))
    return now.strftime("%A, %d %B %Y %H:%M:%S")
