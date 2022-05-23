import ssl
import ffmpeg
import os


from pytube import YouTube

# FOR MACOS ONLY
# ssl._create_default_https_context = ssl._create_unverified_context


# Downloading YouTube video
yt = YouTube('https://www.youtube.com/watch?v=5NV6Rdv1a3I')


# result = yt.streams.filter(only_audio=True)
# for i in result:print(i)


down_stream = yt.streams.get_by_itag(139)
down_stream.download(filename="video1.mp3")


# Modify bitrate with ffmpeg
# vid_input = ffmpeg.probe('video1.mp3')
# curr_bit_rate = next((s for s in vid_input['streams'] if s['codec_type'] == 'audio'),None)['bit_rate'])



