from flask import Flask, render_template, request
from pytube import YouTube
import os


class YouTubeDownloader:
    download_location = ""
    video_url = ""

    def __init__(self, video_url):
        self.download_location = os.path.abspath(r"C:\Users\Charu\Downloads\YouTube")
        self.video_url = video_url

    def download(self):
        yt = YouTube(self.video_url)
        yt.streams.first().download(self.download_location)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def get_url():
    video_url = request.form["username"]
    ytd = YouTubeDownloader(video_url)
    ytd.download()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='localhost', debug=True)