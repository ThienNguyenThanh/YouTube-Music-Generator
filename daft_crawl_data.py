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
video_info['title'] = []
video_info['publish_date'] = []
video_info['length'] = []
video_info['views'] = []
video_info['url'] = []

while True:
    try:
        video_url = next(list_video_urls)
        video = YouTube(video_url)

        video_info['title'].append(video.title)
        video_info['publish_date'].append(video.publish_date)
        video_info['length'].append(video.length)
        video_info['views'].append(video.views)
        video_info['url'].append(video_url)

        # Only takes audio smaller 10 minutes and has audio stream !!! 
        if video.length < 600 and len(video.streams.filter(only_audio=True)) > 0:   

            # Filter audio stream only!
            id_tag = video.streams.filter(only_audio=True)[0]         # use the stream has lowest bitrate !!!
         
            down_stream = video.streams.get_by_itag(id_tag.itag)    # get a specific stream.

            down_audio_title = video.title.replace('/','')       # Remove '/' character in audio title.

            output_file_name = down_audio_title + ".wav"
            down_stream.download( output_path="./free_piano_tutorials_dataset",filename=output_file_name)
    except StopIteration:
        break

print(f"Total time: {time.time() - start_time }")

# Export to csv file
pd.DataFrame.from_dict(video_info).to_csv('free_piano_tutorials_dataset_info.csv', index=False, header=True)



# Modify bitrate with ffmpeg
# vid_input = ffmpeg.probe('video1.mp3')
# curr_bit_rate = next((s for s in vid_input['streams'] if s['codec_type'] == 'audio'),None)['bit_rate'])



