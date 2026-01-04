import streamlit as st
import requests
import os
from pathlib import Path

API_URL = "http://127.0.0.1:8000/generate"
VIDEO_OUTPUT = Path("output/videos")
VIDEO_OUTPUT.mkdir(parents=True, exist_ok=True)

st.title("Shorts Engine Dashboard")
st.write("Create short video series automatically.")

# --- User Input ---
topic = st.text_input("Topic for your series")
episodes = st.number_input("Number of episodes", min_value=1, max_value=20, value=7)
interval = st.number_input("Interval between episodes (hours)", min_value=1, max_value=168, value=24)

if st.button("Generate Series"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        payload = {"topic": topic, "episodes": episodes, "interval_hours": interval}
        with st.spinner("Generating series..."):
            try:
                response = requests.post(API_URL, json=payload)
                data = response.json()
            except Exception as e:
                st.error(f"API request failed: {e}")
                st.stop()

        st.success("Series generated successfully!")
        st.subheader("Scripts Preview")
        for ep in data["videos"]:
            st.markdown(f"**Episode {ep['episode']}**")
            st.video(str(ep["video"]))  # previews video if available
            st.write("")

        st.subheader("Schedule")
        for item in data["schedule"]:
            st.write(f"Video: {item['video']}")
            st.write(f"Post at: {item['post_time']}")
