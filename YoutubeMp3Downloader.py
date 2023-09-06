import os
from pathlib import Path
from pytube import YouTube
from moviepy.editor import AudioFileClip

class YoutubeDownloader:
    def __init__(self, url: str, output_dir: str):
        self.url = url
        self.output_dir = output_dir

    def download_video(self) -> str:
        yt = YouTube(self.url)
        video = yt.streams.filter(abr='160kbps').last()
        output_file = video.download(output_path=self.output_dir)
        return output_file

class WebmToMp3Converter:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_mp3(self) -> None:
        audio_clip = AudioFileClip(self.input_file)
        audio_clip.write_audiofile(self.output_file)

def main():
    youtube_url = input("Enter the YouTube URL: ")
    current_directory = os.getcwd()

    downloader = YoutubeDownloader(youtube_url, current_directory)
    downloaded_file = downloader.download_video()

    video_name = Path(downloaded_file).stem
    mp3_output_file = f"{video_name}.mp3"

    converter = WebmToMp3Converter(downloaded_file, mp3_output_file)
    converter.convert_to_mp3()

if __name__ == "__main__":
    main()
