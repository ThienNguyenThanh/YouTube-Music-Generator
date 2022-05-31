import os
import ssl
import time

import ffmpeg
import pytube
from pytube import YouTube

# FOR MACOS ONLY
if os.name == "posix":
    ssl._create_default_https_context = ssl._create_unverified_context

start_time = time.time()

# Get list YouTube video of specific YouTube channel
list_video_urls = pytube.contrib.channel.Channel('https://www.youtube.com/channel/UCdjQPbF_Wk02mvqqQhWxwPw/videos').url_generator()

i=1
while True:
    try:
        video_url = next(list_video_urls)
        video = YouTube(video_url)
        id_tag = video.streams.filter(only_audio=True)[0]
        down_stream = video.streams.get_by_itag(id_tag.itag)
        out_file_name = "".join("video" + str(i)+".mp4")
        down_stream.download(filename=out_file_name)
        i +=1
    except StopIteration:
        break

print(f"Total time: {start_time - time.time()}")


# Modify bitrate with ffmpeg
# vid_input = ffmpeg.probe('video1.mp3')
# curr_bit_rate = next((s for s in vid_input['streams'] if s['codec_type'] == 'audio'),None)['bit_rate'])



