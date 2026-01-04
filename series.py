def generate_series(topic, episodes=7):
    series = []
    for i in range(1, episodes + 1):
        series.append({
            "episode": i,
            "title": f"{topic} – Part {i}",
            "script": f"{'Stop scrolling.' if i == 1 else 'Remember this.'} This is something most people miss about {topic}. {'Follow for Part ' + str(i + 1) if i < episodes else 'Follow for more.'}"
        })
    return series
