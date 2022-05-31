import os
import ssl
import time

import pandas as pd
# import ffmpeg
import pytube
from pytube import YouTube

# FOR MACOS ONLY
if os.name == "posix":
    ssl._create_default_https_context = ssl._create_unverified_context

start_time = time.time()

# Get list YouTube video of specific YouTube channel
list_video_urls = ( pytube.contrib
                          .playlist
                          .Playlist('https://www.youtube.com/playlist?list=PLzZfeWyGFlb8iBee7i6-RRjBT7SxjT5-0')
                          .url_generator() )

video_info = {}
video_info['url'] = []


i=1
while True:
    try:
        video_url = next(list_video_urls)
        video_info['url'].append(video_url)
        video = YouTube(video_url)

        if video.length < 600:   # Only takes audio smaller 10 minutes.

            # Filter audio stream only!
            id_tag = video.streams.filter(only_audio=True)[0]         # use the stream has lowest bitrate !!!
            down_stream = video.streams.get_by_itag(id_tag.itag)   

            down_audio_title = video.title.replace('/','')       # Remove '/' character in audio title.

            out_file_name = "".join(down_audio_title+".wav")
            down_stream.download( output_path="./dataset",filename=out_file_name)
            i +=1
    except StopIteration:
        break

print(f"Total time: {start_time - time.time()}")

# Export to csv file
# pd.DataFrame.from_dict(video_info).to_csv(r'test.csv', index=False, header=True)



# Modify bitrate with ffmpeg
# vid_input = ffmpeg.probe('video1.mp3')
# curr_bit_rate = next((s for s in vid_input['streams'] if s['codec_type'] == 'audio'),None)['bit_rate'])



