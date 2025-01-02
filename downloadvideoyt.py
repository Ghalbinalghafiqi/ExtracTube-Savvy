import os
import subprocess

def create_folder(folder_name):
    # Membuat folder jika belum ada
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_audio(video_url, output_folder, output_format="mp3"):
    try:
        # Membuat folder tujuan
        create_folder(output_folder)
        
        # Command untuk download audio saja dan convert ke format yang dipilih
        command = [
            "yt-dlp",
            "-f", "bestaudio",  # Download audio dengan kualitas terbaik
            "--extract-audio",  # Ekstrak audio saja
            "--audio-format", output_format,  # Format audio (mp3 atau lainnya)
            "--audio-quality", "192K",  # Kualitas audio
            "-o", f"{output_folder}/%(title)s.%(ext)s",  # Output ke folder yang ditentukan
            video_url
        ]
        print(f"Sedang mendownload dan mengonversi {video_url} ke {output_format.upper()}...")
        subprocess.run(command)
        print(f"Selesai! File {output_format.upper()} dari {video_url} tersimpan di folder '{output_folder}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload {video_url}: {e}")

def download_video(video_url, output_folder):
    try:
        # Membuat folder tujuan
        create_folder(output_folder)

        # Command untuk download video dengan resolusi terbaik
        command = [
            "yt-dlp",
            "-f", "best",  # Download video dengan kualitas terbaik
            "-o", f"{output_folder}/%(title)s.%(ext)s",  # Output ke folder yang ditentukan
            video_url
        ]
        print(f"Sedang mendownload video {video_url} dalam format MP4...")
        subprocess.run(command)
        print(f"Selesai! File video MP4 dari {video_url} tersimpan di folder '{output_folder}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload {video_url}: {e}")

if __name__ == "__main__":
    try:
        # Meminta jumlah URL dari pengguna
        count = int(input("Masukkan jumlah URL YouTube yang ingin diproses: "))
        urls = []

        # Meminta input URL berdasarkan jumlah
        for i in range(count):
            url = input(f"Masukkan URL video ke-{i + 1}: ")
            urls.append(url)

        # Meminta pilihan format
        print("\nPilih format output:")
        print("1. Ekstrak audio (MP3)") 
        print("2. Download video (MP4)")
        choice = int(input("Masukkan pilihan (1/2): "))

        print("\nProses dimulai...")
        for url in urls:
            if choice == 1:
                download_audio(url, output_folder="Lagu", output_format="mp3")
            elif choice == 2:
                download_video(url, output_folder="Video")
            else:
                print("Pilihan tidak valid. Proses dihentikan.")
                break

        print("\nSemua proses selesai!")
    except ValueError:
        print("Harap masukkan angka yang valid.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")