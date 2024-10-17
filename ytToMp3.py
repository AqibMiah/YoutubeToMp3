import yt_dlp


def youtube_to_mp3(output_path):
    try:
        youtube_url = input("Please enter the YouTube video URL: ")

        # Setup yt-dlp options to download only the audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print("Download and conversion complete!")

    except Exception as e:
        print(f"Error: {e}")


output_path = "/Users/aqibmiah/Downloads"
youtube_to_mp3(output_path)
