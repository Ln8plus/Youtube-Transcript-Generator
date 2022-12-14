from yt_dlp import YoutubeDL

def AudioFetcher():
    #Converting youtu.be urls to regular convention.
    url = input('Enter the url of the video: ')
    if 'watch?v=' not in url:
        url = 'https://youtube.com/watch?v=' + url[17:]

    opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with YoutubeDL(opts) as ydl:
        ydl.download([url])
        print('Audio file has finished downloading.')
        print('Now transcribing...')