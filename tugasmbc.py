'''
SOAL 1

Buatlah program yang meminta data inputan berupa total belanja. 
Program kemudian menghitung berapa diskon yang bisa diperoleh dengan ketentuan sebagai berikut:

Jika total belanja kurang dari Rp. 100.000, tidak mendapat diskon.
Jika total belanja antara Rp. 100.000 – Rp. 500.000, mendapat diskon 10%.
Jika total belanja antara Rp. 500.000 – Rp. 1.000.000, mendapat diskon 20%.
Jika total belanja diatas Rp.1.000.000, mendapat diskon 30%.
Kode program kemudian menampilkan harga yang harus dibayar setelah dikurangi diskon.

==============================================================================='''

print('## Program Python Diskon Potongan Harga ##')
print('=========================================') 
print() 

totalbelanja = int(input('Total Belanja: Rp.'))

if (totalbelanja >= 100000) and (totalbelanja < 500000):
    harga_final = totalbelanja - (0.1*totalbelanja)
    print('Selamat, anda dapat diskon 10%')
elif (totalbelanja >= 500000) and (totalbelanja < 1000000):
    harga_final = totalbelanja - (0.2*totalbelanja)
    print('Selamat, anda dapat diskon 20%')
elif (totalbelanja >= 1000000):
    harga_final = totalbelanja - (0.3*totalbelanja)
    print('Selamat, anda dapat diskon 30%')
else:
    harga_final = totalbelanja
    print('Maaf, anda tidak mendapat diskon')

print('Total yang harus dibayar: Rp.', harga_final)

