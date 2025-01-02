import subprocess

def download_and_extract_audio(video_url, output_format="mp3"):
    try:
        # Command untuk download audio saja dan convert ke format MP3
        command = [
            "yt-dlp",
            "-f", "bestaudio",  # Download audio dengan kualitas terbaik
            "--extract-audio",  # Ekstrak audio saja
            "--audio-format", output_format,  # Format audio (default: mp3)
            "--audio-quality", "192K",  # Kualitas audio
            "-o", "%(title)s.%(ext)s",  # Nama file output berdasarkan judul video
            video_url
        ]
        print("Sedang mendownload dan mengonversi ke MP3...")
        subprocess.run(command)
        print("Selesai! File MP3 tersimpan di folder kerja.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ")
    download_and_extract_audio(url)