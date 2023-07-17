
'''SOAL 2

Buatlah program dalam bahasa Python untuk menentukan gaji karyawan mingguan dengan ketentuan sebagai berikut:

Golongan = A maka upah per jam 5000
Golongan = B maka upah per jam 7000
Golongan = C maka upah per jam 8000
Golongan = D maka upah per jam 10000
Ketentuan tambahan :

Jika jam kerja karyawan lebih dari 48 jam per minggu maka akan mendapat uang lembur dengan perhitungan uang lembur = (jam kerja-48)*4000.
Jika jam kerja kurang dari 48 jam maka pegawai tidak akan mendapat uang lembur. Perhitungan gaji pegawai adalah upah + uang lembur.
Input berupa nama karyawan, golongan dan jam kerja.
Outputnya adalah nama karyawan dan gaji yang diterima.'''

while True:

    print("===========TUGAS MBC SOAL NO 2==========")
    print("========MENGHITUNG GAJI KARYAWAN========")
    print("============by KELOMPOK 1 GIS===========")

    nama_karyawan = input("Masukkan nama karyawan: ")
    golongan = input("Masukkan golongan (A/B/C/D): ").lower()
    jam_kerja = int(input("Masukkan jam kerja: "))

    if golongan == 'a':
        upah_per_jam = 5000
    elif golongan == 'b':
        upah_per_jam = 7000
    elif golongan == 'c':
        upah_per_jam = 8000
    elif golongan == 'd':
        upah_per_jam = 10000
    else:
        print("Golongan tidak valid!")
     if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    gaji = (jam_kerja * upah_per_jam) + uang_lembur

    print("Nama karyawan:", nama_karyawan)
    print("Gaji yang diterima: Rp.", gaji)

    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if ulangi.lower() != "ya":
        break

