from flask import Flask,render_template,request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_path = None
    video_name = None

    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.get_by_itag(18)  # Choose the desired stream format (itag=18 for mp4, 360p)
            
            output_dir = 'downloads'
            os.makedirs(output_dir, exist_ok=True)
            
            video_name = f"{yt.title}.mp4"
            video_path = os.path.abspath(os.path.join(output_dir, video_name))

            
            video_stream.download(output_path=output_dir, filename=video_name)
        except Exception as e:
            error_message = str(e)
            return render_template('indes.html', error_message=error_message)

    return render_template('indes.html', video_path=video_path, video_name=video_name)

if __name__ == '__main__':
    app.run(debug=True)
