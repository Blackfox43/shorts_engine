from fastapi import FastAPI
from pydantic import BaseModel
from series import generate_series
from video import create_video
from scheduler import schedule_series

app = FastAPI(title="Shorts Engine")

class SeriesRequest(BaseModel):
    topic: str
    episodes: int = 7
    interval_hours: int = 24

BACKGROUND = "assets/backgrounds/bg1.mp4"

@app.post("/generate")
def generate(req: SeriesRequest):
    series = generate_series(req.topic, req.episodes)
    videos = []

    for ep in series:
        video_path = create_video(ep["script"], BACKGROUND)
        videos.append({"episode": ep["episode"], "video": video_path})

    schedule = schedule_series(videos, interval_hours=req.interval_hours)
    return {"topic": req.topic, "videos": videos, "schedule": schedule}
