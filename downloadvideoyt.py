import subprocess

def download_youtube_video(video_url):
    try:
        # Command untuk download video dengan yt-dlp
        command = ["yt-dlp", video_url]
        print("Sedang mendownload...")
        subprocess.run(command)
        print("Download selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ")
    download_youtube_video(url)