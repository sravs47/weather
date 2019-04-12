import datetime
from datetime import timedelta

def is_newerthan_1hour(time):
    current_time =datetime.datetime.now()
    total_difference =int(timedelta.total_seconds(current_time-time))
    if total_difference>3600:
        return False
    return True


JSON_MIME_TYPE = 'application/json'


def to_dict(obj):
    return obj.__dict__
