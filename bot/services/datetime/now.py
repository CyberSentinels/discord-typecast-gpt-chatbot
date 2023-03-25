from datetime import datetime
from locale import setlocale, LC_ALL
from pytz import timezone

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def now_us():
    setlocale(LC_ALL, 'en_US.UTF-8')
    now = datetime.now()
    return now.strftime('%A, %d %B %Y %H:%M:%S')

def now_ca():
    setlocale(LC_ALL, 'en_CA.UTF-8')
    now = datetime.now(timezone('Canada/Eastern'))
    return now.strftime('%A, %d %B %Y %H:%M:%S')
