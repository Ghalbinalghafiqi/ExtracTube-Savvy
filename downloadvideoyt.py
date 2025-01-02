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
        return True
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload {video_url}: {e}")
        return False

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
        return True
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload {video_url}: {e}")
        return False

def main():
    while True:
        try:
            # Meminta jumlah URL dari pengguna
            count = int(input("\nMasukkan jumlah URL YouTube yang ingin diproses: "))
            urls = []

            # Meminta input URL berdasarkan jumlah
            for i in range(count):
                url = input(f"Masukkan URL video ke-{i + 1}: ")
                urls.append(url)

            # Meminta pilihan format
            print("\nPilih format output:")
            print("1. Ekstrak audio (MP3, disimpan di folder 'Lagu')")
            print("2. Download video (MP4, disimpan di folder 'Video')")
            choice = int(input("Masukkan pilihan (1/2): "))

            if choice not in [1, 2]:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue

            print("\nProses dimulai...")
            all_success = True  # Flag untuk mengecek apakah semua proses berhasil
            for url in urls:
                if choice == 1:
                    success = download_audio(url, output_folder="Lagu", output_format="mp3")
                elif choice == 2:
                    success = download_video(url, output_folder="Video")
                
                if not success:
                    all_success = False
                    break  # Keluar dari loop jika terjadi error pada salah satu URL

            if all_success:
                print("\nSemua proses selesai!")
                break  # Keluar dari program jika semua proses berhasil
            else:
                print("\nTerjadi kesalahan pada salah satu URL. Ulangi proses dari awal.")
        except ValueError:
            print("Harap masukkan angka yang valid.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()