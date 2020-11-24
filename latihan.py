print("Nama : Pikri Ramdani")
print("NIM : 312010162")
print("Kelas : TI>20.A.1")
print("===========================")
print("Latihan - Modul Praktikum 4")
print()
print()

print("Membuat list dengan 5 elemen")
data = [4, 5, 7, 8, 9]
print(data)
# akses list
print("Menampilkan element ke 3")
print(data[2])

print("ambil nilai elemen ke 2 sampai ke 4")
print(data[1:4])

print("Ambil nilai terakhir")
print(data[-1])

# ubah elemen list
print("Ubah elemen ke 4 dengan nilai lainnya")
data[3] = 11
print(data[3])

print("ubah elemen ke 4 sampai terakhir")
data[3:5] = [12, 14]
print(data)

# tambah elemen list
print("ambil 2 bagian dari list pertama(A) dan jadikan list ke 2(B)")
baris = data[2:4]
print(baris)

print("tambah list B dengan nilai string")
baris.append("Pikri")
print(baris)

print("tambah list B dengan 3 nilai")
baris.extend(["Ramdani", 3, 4])
print(baris)

print("gabung list B dengan list A")
gabung = baris+data
print(gabung)