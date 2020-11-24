# pertemuan9
Repository ini dibuat untuk memenuhi tugas pada pertemuan ke 9.
<hr>

 Nama   : Pikri Ramdani <br>
 NIM    : 312010162     <br>
Kelas   : TI.20.A.1     <br>

Pada mata kuliah Bahasa Pemrograman - Pertemuan 9 kali ini saya mendapatkan materi *list, Tuple dan Dictianory*.<br>
Nah, untuk praktikum 4 ini materi yang di dapatkan adalah **list**.<br>
<br>
* Didalam materi praktikum 4 ini terdapat 2 tugas. yaitu : Latihan dan Praktikum.<br>

## praktikum 4 - Latihan

* Berikut adalah tugas dari latihan, bisa di lihat pada gambar dibawah ini :<br>
![Soal Tugas Latihan](gambar/soallatihanP4.PNG)<br>
*Berikut jawabn / *source code* / program sederhana yang telah saya buat :
``` python
print("Nama : Pikri Ramdani")
print("NIM : 312010162")
print("Kelas : TI.20.A.1")
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
gabung = baris+datas
print(gabung)
```
* Untuk hasil dari source code tersebut adalah seperti berikut : <br>
![Hasil Soal Latihan](gambar/hasilsoallatihan.PNG)<br>

## Praktikum - Praktikum 4

Untuk tugas yang kedua Tugas praktikum, yaitu tugas untuk membuat program sederhana menampilkan Data nilai mahasiswa<br>
* Berikut soal yang di berikan oleh Dosen :<br>
![Soal Praktikum](gambar/soalpraktikum.PNG)<br>

* Hasil yang di inginkan 
