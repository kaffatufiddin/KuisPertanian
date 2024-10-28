# PROGRAM KUIS PERTANIAN ANAK MENGGUNAKAN PYTHON
# By: Kaffatufiddin
# YouTube: https://www.youtube.com/@DataWithMasKaff
# LinkedIn: https://www.linkedin.com/in/kaffatufiddin/
# GitHub: https://github.com/kaffatufiddin

from tabulate import tabulate
from datetime import datetime
from playsound import playsound
from colorama import init, Fore 
init() 
import random

# Bank Soal dalam bentuk dictionaries in list
soal = [
    {"pertanyaan": "Hewan apa yang mempunyai belalai?", "pilihan": ["Kucing", "Gajah", "Badak", "Kuda"], "jawaban": "b"},
    {"pertanyaan": "Buah apa yang memiliki duri di kulitnya?", "pilihan": ["Kelengkeng", "Pisang", "Sawo", "Durian"], "jawaban": "d"},
    {"pertanyaan": "Sayuran apa yang berwarna oranye dan sehat untuk mata?", "pilihan": ["Bayam", "Wortel", "Kubis", "Kangkung"], "jawaban": "b"},
    {"pertanyaan": "Tanaman apa yang memiliki biji di dalam polongnya?", "pilihan": ["Jagung", "Buncis", "Tomat", "Mentimun"], "jawaban": "b"},
    {"pertanyaan": "Sayuran apa yang berdaun hijau dan bisa tumbuh di air?", "pilihan": ["Kangkung", "Bayam", "Selada", "Brokoli"], "jawaban": "a"},
    {"pertanyaan": "Sayuran apa yang terkenal digunakan dalam salad dan burger?", "pilihan": ["Bayam", "Brokoli", "Selada", "Wortel"], "jawaban": "c"},
    {"pertanyaan": "Hewan apa yang memiliki kantung di perutnya?", "pilihan": ["Kangguru", "Kambing", "Kelelawar", "Kuda"], "jawaban": "a"},
    {"pertanyaan": "Hewan ternak apa yang menghasilkan telur?", "pilihan": ["Kambing", "Sapi", "Bebek", "Kuda"], "jawaban": "c"},
    {"pertanyaan": "Hewan berkaki empat yang diternak dan diambil bulunya?", "pilihan": ["Ayam", "Kelinci", "Domba", "Kucing"], "jawaban": "c"},
    {"pertanyaan": "Kecap dibuat dari?", "pilihan": ["Jagung", "Kedelai", "Padi", "Singkong"], "jawaban": "b"},
]

# List untuk menyimpan hasil pekerjaan siswa
hasil_kerja_siswa = []

# Fungsi Sound Effect
def sound_opening():
    playsound("sound/opening.mp3")
def sound_warning():
    playsound("sound/warning.mp3")
def sound_hasil():
    playsound("sound/hasil.mp3")
def sound_mulai():
    playsound("sound/mulai_game.mp3")
def sound_jawaban():
    playsound("sound/jawaban.mp3")
def sound_exit():
    playsound("sound/exit.mp3")

# Fungsi untuk validasi nama
def validasi_nama(prompt="Masukkan Nama: "):
    nama = input(prompt)
    while not nama.replace(" ", "").isalpha():
        print(merah("Hanya bisa memasukkan huruf. Silakan ketik nama lagi"))
        sound_warning()
        nama = input(prompt)
    return nama

# Fungsi untuk validasi input numerik
def validasi_numerik(prompt="Masukkan angka: "):
    input_str = input(prompt)
    while not input_str.isdigit():
        print(merah("Input harus berupa angka."))
        sound_warning()
        input_str = input(prompt)
    return int(input_str)

# Fungsi untuk validasi jawaban
def validasi_jawaban(prompt="Jawaban: "):
    jawaban = input(prompt).replace(" ", "")
    while jawaban.lower() not in ["a", "b", "c", "d"]:
        print(merah("Pilih jawaban a, b, c, atau d."))
        sound_warning()
        jawaban = input(prompt)
    return jawaban.lower()

# Fungsi untuk validasi konfirmasi Yes/No
def validasi_konfirmasi(prompt="Jawaban: "):
    input_str = input(prompt).lower().strip()
    while input_str not in ["yes", "yess", "yesss", "ya", "y", "yep", "no", "noo", "nope"]:
        print(merah("Input tidak sesuai. Harap masukkan 'Yes' atau 'No'."))
        sound_warning()
        input_str = input(prompt).lower().strip()
    return input_str == "yes"

# Fungsi validasi kelas
def validasi_kelas():
    while True:
        kelas = input("Masukkan kelas (1-6): ")
        if kelas.isdigit() and 1 <= int(kelas) <= 6:
            return int(kelas)
        else:
            print(merah("Kelas tidak sesuai. Pilih kelas 1-6."))
            sound_warning()

# Fungsi Warna Teks
def merah(teks): return f"{Fore.RED}{teks}{Fore.RESET}"
def hijau(teks): return f"{Fore.GREEN}{teks}{Fore.RESET}"
def kuning(teks): return f"{Fore.YELLOW}{teks}{Fore.RESET}"

# Fungsi Menampilkan Tabel
def tampilkan_tabel(data, headers):
    print(tabulate(data, headers=headers, tablefmt="rst"))

# Fungsi untuk menampilkan tabel kunci jawaban
def tampilkan_kunci_jawaban(pertanyaan, jawaban_siswa):
    print(kuning("\nTabel Kunci Jawaban:"))
    alfabet = ['a', 'b', 'c', 'd']  # Atur sesuai dengan pilihan yang ada
    tabel_kunci = []
    for i, question in enumerate(pertanyaan):
        # Menggunakan index() untuk menemukan posisi dari jawaban_siswa dan kunci jawaban
        jawaban_index = alfabet.index(jawaban_siswa[i])
        kunci_index = alfabet.index(question['jawaban'])
        jawaban_siswa_display = f"{jawaban_siswa[i]}. {question['pilihan'][jawaban_index]}"
        kunci_jawaban_display = f"{question['jawaban']}. {question['pilihan'][kunci_index]}"
        tabel_kunci.append([question["pertanyaan"], jawaban_siswa_display, kunci_jawaban_display])

    tampilkan_tabel(tabel_kunci, ["Soal", "Jawaban Kamu", "Kunci"])

# Fungsi untuk memulai kuis dengan konfirmasi
def mulai_kuis():
    print(kuning("Menu Mulai Kuis dipilih."))
    if not validasi_konfirmasi("\nSiap mulai kuis? Yes/No: "):
        print(merah("Kuis dibatalkan. Kembali ke menu utama."))
        return # Kembali ke menu utama
    
    nama = validasi_nama("Masukkan Nama: ")
    kelas = validasi_kelas()
    skor = 0
    benar, salah = 0, 0
    start_time = datetime.now()
    pertanyaan = random.sample(soal, 5)  # Mengambil 5 soal acak dari list soal
    jawaban_siswa = []  # Menyimpan jawaban siswa
    print(hijau(f"Halo {nama.title()}!\nSelamat mengerjakan kuisnya!"))
    sound_mulai()
    print(kuning("\nPetunjuk : ketik jawaban a, b, c, atau d."))

    for i, question in enumerate(pertanyaan, 1):
        print(f"\nSoal {i}: {question['pertanyaan']}")
        pilihan_huruf = ['a', 'b', 'c', 'd']  # Buat list pilihan huruf
        
        for j, pilihan in zip(pilihan_huruf, question["pilihan"]):
            print(f"{j}. {pilihan}")
        jawaban = validasi_jawaban("Jawaban kamu: ")
        
        # Simpan jawaban siswa
        jawaban_siswa.append(jawaban)
        sound_jawaban()
        if jawaban == question["jawaban"]: 
            skor += 20 
            benar += 1
        else: 
            salah += 1
            
    end_time = datetime.now()
    
    # Menghitung Waktu Pengerjaan
    durasi_detik = (end_time - start_time).seconds 
    durasi_menit = durasi_detik // 60
    durasi_detik %= 60

    # Menyimpan hasil kerja siswa
    hasil_kerja = {"nama": nama, "kelas": kelas, "skor": skor, "benar": benar, "salah": salah, "durasi": f"{durasi_menit} menit {durasi_detik} detik"}
    hasil_kerja_siswa.append(hasil_kerja)

    # Menampilkan hasil
    print(hijau(f"Selamat {nama.title()}!\nSkor kamu: {skor}"))
    print(kuning(f"Benar: {benar} | Salah: {salah} | Durasi: {hasil_kerja['durasi']}"))
    sound_hasil()
    # Tampilkan kunci jawaban
    tampilkan_kunci_jawaban(pertanyaan, jawaban_siswa)

# Fungsi untuk melihat peringkat skor
def lihat_peringkat_skor():
    if not hasil_kerja_siswa:
        print(merah("Belum ada hasil kuis yang tersimpan."))
        sound_warning()
        return

    print(kuning("\nTabel Peringkat Skor:"))

    # Konversi durasi ke detik dan urutkan
    for item in hasil_kerja_siswa:
        waktu = item["durasi"].split(" menit ")
        menit = int(waktu[0]) if len(waktu) > 1 else 0
        detik = int(waktu[-1].split()[0])
        item["durasi_detik"] = menit * 60 + detik

    # Urutkan berdasarkan skor dan durasi
    data_skor = sorted(hasil_kerja_siswa, key=lambda x: (-x['skor'], x['durasi_detik']))
    tabel_skor = [[item["nama"], item["kelas"], item["skor"], item["benar"], item["salah"], item["durasi"]] for item in data_skor]
    tampilkan_tabel(tabel_skor, ["Nama", "Kelas", "Skor", "Benar", "Salah", "Durasi"])

    # Hapus kolom durasi_detik setelah pengurutan
    for item in hasil_kerja_siswa:
        del item["durasi_detik"]

# Menu utama
def menu_utama():
    print(hijau("\n============================================="))
    print(hijau("SELAMAT DATANG DI KUIS PERTANIAN UNTUK ANAK"))
    print(hijau("============================================="))
    sound_opening()
    while True:
        print(kuning("\n=== MENU UTAMA ===\n"))
        print("1. Mulai Kuis")
        print("2. Lihat Peringkat Skor")
        print("0. Keluar")

        pilihan = validasi_numerik("Pilih menu : ")

        if pilihan == 1:
            mulai_kuis()
        elif pilihan == 2:
            lihat_peringkat_skor()
        elif pilihan == 0:
            print(merah("Keluar dari program kuis..."))
            print(hijau("Terima kasih telah bermain!"))
            sound_exit()
            break
        else:
            print(merah("Menu tidak ditemukan. Silakan coba lagi."))
            sound_warning()

# Menjalankan program
if __name__ == "__main__":
    menu_utama()