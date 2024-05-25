from datetime import datetime, timedelta



def default_start_time():
    now = datetime.now()
    start = now.replace(hour=13, minute=37, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)