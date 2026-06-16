# Tugas AI Developer Program Mandiri Infinite Learning Batch 10

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Repository ini merupakan arsip tugas [Nasrullah (Achul)](https://www.github.com/achul-cos) selama menjalani studi independen pada program mandiri batch 10 oleh infinite learning pada bidang AI Developer.


## Daftar Tugas

 - [Tugas 4 - Python Data Structures](#-tugas-4-python-data-structures)
 - [Tugas 5 - Python Function and Class](#-tugas-5-python-function-and-class)
 - [Tugas 6 - Python Modules, File I/O, & OOP Sederhana](#-tugas-6-python-modules,-file-i/o,-&-oop-sederhana)


## Deployment

Untuk menjalankan setiap file tugas disini

```bash
git clone https://github.com/achul-cos/tugas_python_ai_b10.git
```


## Tugas 4 - Python Data Structures

Pada tugas ini, kita melakukan pemograman pada python dan mulai mendeklarasikan variabel dengan tipe-tipe data seperti float, variabel, integer, string dan list.

Serta melakukan operasi seperti `print()` , dan operasi matematika dasar seperi `+ - += > < >= <=` serta operasi lainya.

Berikut file dari [tugas 4](https://github.com/achul-cos/tugas_python_ai_b10/blob/main/tugas4.py)

Untuk run dan menjalankan tugasnya,

```bash
py .\tugas_python_ai_b10\tugas4.py
```

Output yang seharusnya,

```bash
(venv) PS C:\Stupen\tugas_python_ai_b10> py tugas4.py
Ini elemen pertama : americano; Dan ini elemen terakhir : 123

Tampilkan anggota list dari 1 sampai 6, dimana skip setiap dua anggota : ['americano', False, 'Laptop', 123]

Tambahkan list dengan anggota baru 'embegeh' : ['americano', 19, False, 187.5, 'Laptop', True, 123, 'embegeh']

Hapus anggota paling terakhir di list : ['americano', 19, False, 187.5, 'Laptop', True, 123]

Tambahakan anggota string pada list di urutan ke-2 : ['americano', '19 Juta Lapangan Pekerjaan', 19, False, 187.5, 'Laptop', True, 123]

Gabungkan list dengan list lainya : ['americano', '19 Juta Lapangan Pekerjaan', 19, False, 187.5, 'Laptop', True, 123, 19, 'Juta Lapangan', False]

Hapus anggota didalam list sesuai dengan nilai yang ditentukan : ['americano', 19, False, 187.5, 'Laptop', True, 123, 19, 'Juta Lapangan', False]

===============================

Pada tuple, jumlah anggota nya sebanyak : 6

Berikut anggota ke 3 dan 4 dari tuple, Nakamura dan Hirose

tampilkan anggota 1 hingga 3 : Go For It! Nakamura

Dan anggota sisanya : ['Hirose', 2026, 2.2]

===============================

Hasil dari union kedua set : {'pecel', 'gudeg', 'sate', 'onigiri', 'mie_soba_dingin', 'pasta', 'nasi_goreng', 'ramen'}

Hasil dari intersection kedua set : {'sate', 'onigiri'}

Hasil dari difference kedua set : {'nasi_goreng', 'pecel', 'gudeg'}

Hasil dari symmetric_difference kedua set : {'ramen', 'pecel', 'mie_soba_dingin', 'gudeg', 'pasta', 'nasi_goreng'}

===============================

Dict mahasiswa ditambahkan key baru untuk tinggBadan : {'nama': 'achul', 'nim': 3312401030, 'angkatan': 2024, 'kota': 'Batam', 'tinggiBadan': 161.2}

Mengubah nilai pada key kota di dict mahasiswa, 'kota': Jakarta

Menghapus key angkatan pada dict mahasiswa : {'nama': 'achul', 'nim': 3312401030, 'kota': 'Jakarta', 'tinggiBadan': 161.2}

Pada key : nama, maka valuenya : achul
Pada key : nim, maka valuenya : 3312401030
Pada key : kota, maka valuenya : Jakarta
Pada key : tinggiBadan, maka valuenya : 161.2
===============================

Nama-Nama makanan favorti achul : pecel
Nama-Nama makanan favorti achul : nasi goreng
Nama-Nama makanan favorti achul : ketoprak
Nama-Nama makanan favorti achul : ayam geprek

Nama-nama Makanan murah : ['pecel', 'nasi goreng', 'ayam geprek']

===============================

Ini list genap : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Ini list ganjil : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

{'angka': 1, 'jenis': 'ganjil'}
{'angka': 2, 'jenis': 'genap'}
{'angka': 3, 'jenis': 'ganjil'}
{'angka': 4, 'jenis': 'genap'}
{'angka': 5, 'jenis': 'ganjil'}
{'angka': 6, 'jenis': 'genap'}
{'angka': 7, 'jenis': 'ganjil'}
{'angka': 8, 'jenis': 'genap'}
{'angka': 9, 'jenis': 'ganjil'}
{'angka': 10, 'jenis': 'genap'}

{'r', 'p', 'a', ',', 's', 'l', '.', 'g', 'w', 'i', 'j', 'k', 't', 'y', 'o', 'h', 'n', 'd'}

Ada tenant yang sama nih, yaitu kopken dan pada posisi index ke-1
Ada tenant yang sama nih, yaitu baresto dan pada posisi index ke-2
```
## Tugas 5 - Python Function and Class

Pada tugas ini, kita melakukan pemograman pada python terutama pemograman function dan class sederhana

Berikut file dari [tugas 5](https://github.com/achul-cos/tugas_python_ai_b10/blob/main/tugas5.py)

Untuk run dan menjalankan tugasnya,

```bash
py .\tugas_python_ai_b10\tugas5.py
```

Output yang seharusnya,

```bash
(venv) PS C:\Stupen\tugas_python_ai_b10> py tugas5.py
Halo, Arifian!
12
10
90.0
0
74.0
68.0
LULUS
TIDAK LULUS
```
## Tugas 6 - Python Modules, File I/O, & OOP Sederhana

Pada tugas ini, kita melakukan pemograman pada python dan menggunakan external module yang kita gunakan pada proyek kita, serta melakukan pengolahan data sederhana menggunakan numpy dan pandas seperti mencari median, nilai rata-rata, standar deviasi dan lainya.

Serta membuat file berupa ringkasan [ringkasan_tugas6.txt](https://github.com/achul-cos/tugas_python_ai_b10/blob/main/ringkasan_tugas6.txt)

Serta melakukan pemograman class sederhana.

Berikut file dari [tugas 5](https://github.com/achul-cos/tugas_python_ai_b10/blob/main/tugas6.py)

Untuk run dan menjalankan tugasnya,

```bash
pip install numpy
pip install pandas
py .\tugas_python_ai_b10\tugas6.py
```

Output yang seharusnya,

```bash
(venv) PS C:\Stupen\tugas_python_ai_b10> py tugas6.py
Ini data random nilai ujian : [51 92 14 71 60 20 82 86 74 74 87 99 23  2 21 52  1 87 29 37  1 63 59 20
 32 75 57 21 88 48]

Ini rata-rata data random nilai ujian : 50.86666666666667

Ini median data random nilai ujian : 54.5

Ini standar deviasi dari data random : 29.89842061975106

Ini nilai minimum dari data random : 1

Ini adalah nilai maksimum dari data random : 99

===========================================

      nama   nim  nilai      alamat  tinggi
0    Achul   111     51    sagulung   161.2
1    Valdo   222     92    batu aji   162.2
2   Steven   333     14   puskopkar   181.3
3    Tatik   444     71     tembesi   160.1
4     Hasi   555     60      nagoya   159.7
5     Dion   666     20  batu ampar   161.7
6     Arya   777     82  lubuk baja   186.8
7      Oki   888     86       piayu   172.7
8    Kayla   999     74    barelang   160.2
9    Rahel  1000     74    batu aji   160.9
10  Shinta  1100     87     jakarta   162.8

Ini adalah data mahasiswa yang telah ditambahkan kolom status :
      nama   nim  nilai      alamat  tinggi       status
0    Achul   111     51    sagulung   161.2  TIDAK LULUS
1    Valdo   222     92    batu aji   162.2        LULUS
2   Steven   333     14   puskopkar   181.3  TIDAK LULUS
3    Tatik   444     71     tembesi   160.1        LULUS
4     Hasi   555     60      nagoya   159.7  TIDAK LULUS
5     Dion   666     20  batu ampar   161.7  TIDAK LULUS
6     Arya   777     82  lubuk baja   186.8        LULUS
7      Oki   888     86       piayu   172.7        LULUS
8    Kayla   999     74    barelang   160.2        LULUS
9    Rahel  1000     74    batu aji   160.9        LULUS
10  Shinta  1100     87     jakarta   162.8        LULUS

Ini adalah data_mahasiswa 5 teratas :
     nama  nim  nilai     alamat  tinggi       status
0   Achul  111     51   sagulung   161.2  TIDAK LULUS
1   Valdo  222     92   batu aji   162.2        LULUS
2  Steven  333     14  puskopkar   181.3  TIDAK LULUS
3   Tatik  444     71    tembesi   160.1        LULUS
4    Hasi  555     60     nagoya   159.7  TIDAK LULUS

Jumlah data mahasiswa : 11

Jumlah data mahasiswa lulus : 7

Jumlah data mahasiswa tidak lulus : 4

===========================================

Ringkasan Numpy : 

Ini rata-rata data random nilai ujian : 50.86666666666667
Ini median data random nilai ujian : 54.5
Ini standar deviasi dari data random : 29.89842061975106
Ini nilai minimum dari data random : 1
Ini adalah nilai maksimum dari data random : 99

Ringkasan Pandas dan Data Frame : 

Ini adalah data_mahasiswa 5 teratas :
     nama  nim  nilai     alamat  tinggi       status
0   Achul  111     51   sagulung   161.2  TIDAK LULUS
1   Valdo  222     92   batu aji   162.2        LULUS
2  Steven  333     14  puskopkar   181.3  TIDAK LULUS
3   Tatik  444     71    tembesi   160.1        LULUS
4    Hasi  555     60     nagoya   159.7  TIDAK LULUS


Ringkasan OOP: Gradebook : 

<__main__.GradeBook object at 0x0000020EE62EA510>
Rata-rata nilai mahasiswa : 64.6

Persentase kelulusan mahasiswa : 63.64%
```