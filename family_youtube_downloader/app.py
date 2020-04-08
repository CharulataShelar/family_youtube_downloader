from flask import Flask, render_template, request
from pytube import YouTube
import os
from pathlib import Path


class YouTubeDownloader:
    download_location = ""
    video_url = ""

    def __init__(self, video_url):
        # self.download_location = os.path.abspath(download_location)
        # self.download_location = download_location
        # self.download_location = os.path.normpath(download_location)
        self.video_url = video_url

    def download(self):
        # print("*********************** D PATH :", self.download_location)
        yt = YouTube(self.video_url)
        # yt.streams.first().download(self.download_location)
        yt.streams.first().download()
        print("Download completed!!!!!!!")


app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Hi There!!</h1>"
    return render_template("index.html")


@app.route('/download', methods=['POST'])
def get_url():
    # download_location = request.form["downloadlocation"]
    video_url = request.form["url"]
    ytd = YouTubeDownloader(video_url)
    ytd.download()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='localhost', debug=True)