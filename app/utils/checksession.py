import time


def check_session_timestamp(timestamp, time_limit):
    curr_time = int(time.time())
    if curr_time - int(timestamp) >= time_limit:
        return False
    return True
