"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

#comment bisa diganti dengan double """""

kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'

print(kamus)
print(kamus['ayah'])
print(kamus['ibu'])

#Contoh Kasus
print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver disekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 50},
        {'nama': 'Tri', 'jarak': 150},
        {'nama': 'Catur', 'jarak': 200}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Jarak driver #1 adalah {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
