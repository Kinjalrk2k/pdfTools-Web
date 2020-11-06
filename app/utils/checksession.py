import time


def check_session_timestamp(timestamp):
    curr_time = int(time.time())
    if curr_time - int(timestamp) >= 600:
        return False
    return True
