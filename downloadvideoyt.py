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
        print(f"Sedang mendownload dan mengonversi {video_url} ke MP3...")
        subprocess.run(command)
        print(f"Selesai! File MP3 dari {video_url} tersimpan di folder kerja.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload {video_url}: {e}")

if __name__ == "__main__":
    try:
        # Meminta jumlah URL dari pengguna
        count = int(input("Masukkan jumlah URL YouTube yang ingin didownload: "))
        urls = []

        # Meminta input URL berdasarkan jumlah
        for i in range(count):
            url = input(f"Masukkan URL video ke-{i + 1}: ")
            urls.append(url)

        print("\nProses download dimulai...")
        for url in urls:
            download_and_extract_audio(url)

        print("\nSemua proses selesai!")
    except ValueError:
        print("Harap masukkan angka yang valid untuk jumlah URL.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")