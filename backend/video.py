from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import uuid, os

def create_video(script, background_path):
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/videos", exist_ok=True)

    voice_file = f"output/{uuid.uuid4()}.mp3"
    video_file = f"output/videos/{uuid.uuid4()}.mp4"

    gTTS(text=script, lang='en').save(voice_file)

    audio = AudioFileClip(voice_file)
    video = VideoFileClip(background_path).resize((1080, 1920)).set_duration(audio.duration).set_audio(audio)

    caption = TextClip(script, fontsize=60, color="white", size=(900, None), method="caption", align="center") \
        .set_position(("center", "bottom")).set_duration(audio.duration)

    final = CompositeVideoClip([video, caption])
    final.write_videofile(video_file, fps=30, codec="libx264", audio_codec="aac")
    return video_file
