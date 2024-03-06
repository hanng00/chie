from datetime import datetime, timezone


def get_current_utc_time():
    return datetime.utcnow().replace(tzinfo=timezone.utc)
