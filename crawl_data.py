import ssl

from pytube import YouTube

# from vctube import VCtube

ssl._create_default_https_context = ssl._create_unverified_context

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

# print(yt.streams.filter(only_audio=True))

down_stream = yt.streams.get_by_itag(140)
down_stream.download(timeout=60)


# video_title = "YouTube Rewind 2019: For the Record | #YouTubeRewind"
# video_url = "http://youtube.com/watch?v=2lAe1cqCOXo"
# lang = "en"

# vc = VCtube(video_title, video_url, lang)

# vc.download_audio()
