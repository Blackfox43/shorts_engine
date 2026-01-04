from datetime import datetime, timedelta

def schedule_series(videos, start_date=None, interval_hours=24):
    if not start_date:
        start_date = datetime.now()
    return [{"video": v["video"], "post_time": start_date + timedelta(hours=i*interval_hours)} for i, v in enumerate(videos)]
