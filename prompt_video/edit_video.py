import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from pydub import AudioSegment
from prompt_video.utils import get_media_path

class VideoEditor:
    def __init__(self):
        os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/7.0_1/bin/ffmpeg"  # ffmpeg 설치 경로!!
        self.og_video_path = None
        self.cut_video_path = get_media_path('videos', 'cut_video.mp4')
        self.bgm_path = get_media_path('audios', 'new_bgm.mp3')
        self.cut_bgm_path = get_media_path('audios', 'cut_bgm.mp3')
        self.video_with_bgm_path = get_media_path('videos', 'video_with_bgm.mp4')
        self.final_video_path = get_media_path('videos', 'final_video.mp4')

    def cut_video(self, video_path, start_time, end_time):
        self.og_video_path = video_path
        clip = VideoFileClip(video_path).subclip(start_time, end_time)
        clip.write_videofile(self.cut_video_path, codec="libx264")
        return self.cut_video_path

    def cut_audio(self, start_time, end_time):
        audio = AudioSegment.from_mp3(self.bgm_path)
        start_ms = start_time * 1000  # milliseconds
        end_ms = end_time * 1000
        cutting_audio = audio[start_ms:end_ms]
        cutting_audio.export(self.cut_bgm_path, format="mp3")

    def add_bgm_to_video(self):
        video = VideoFileClip(self.cut_video_path)
        bgm = AudioFileClip(self.cut_bgm_path).set_duration(video.duration)
        video = video.set_audio(bgm)
        video.write_videofile(self.video_with_bgm_path, codec="libx264")

    def insert_video(self, start_time, end_time):
        original_video = VideoFileClip(self.og_video_path)
        inserting_video = VideoFileClip(self.video_with_bgm_path)
        pre_clip = original_video.subclip(0, start_time)
        post_clip = original_video.subclip(end_time, original_video.duration)
        final_video = concatenate_videoclips([pre_clip, inserting_video, post_clip])
        final_video.write_videofile(self.final_video_path, codec="libx264")
        return self.final_video_path
