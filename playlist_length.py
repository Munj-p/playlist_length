import yt_dlp

def get_playlist_duration(playlist_url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

        total_seconds = 0
        for entry in playlist_info["entries"]:
            if "duration" in entry and entry["duration"] is not None:
                total_seconds += entry["duration"]

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f"{hours}h {minutes}m {seconds}s"

playlist_url = "yt_playlist_url"
print("Total Playlist Duration:", get_playlist_duration(playlist_url))
