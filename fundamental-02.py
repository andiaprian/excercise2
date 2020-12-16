# tipe data skalar => tipe data sederhana
anak1 = 'Edgar'
anak2 = 'Radit'
anak3 = 'Raisa'
anak4 = 'Noah'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list/daftar/array
anak = ['Edgar', 'Radit', 'Raisa', 'Noah']
print(anak)
anak.append('Riri')
print(anak)

#sapa anak ke-2
print(f'\nHai {anak[1]}!')

#cara lain menyapa anak
print('\nSapa semua anak')
for b in anak: #mengganti variable 'refactor'
    print(f'Hai {b}!')

print('\nSapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')
