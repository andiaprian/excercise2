#KONSTRUKSI DASAR PYTHON
#SEQUENTIAL: Eksekusi Berurutan
print("Hello World!")
print("by Apriana")
print("Tanggal 16 Desember 2020")
print("----"*10)

#PERCABANGAN : Eksekusi Terpilih
ingin_cepat = True
if ingin_cepat:
    print('Jalan Lurus ya!')
else:
    print('Jalan Lain')

#PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #Jumlah perulangan = 5 - 1 = 4
    print(f'Hallo anak #{index_anak}')