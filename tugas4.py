# 1.) List – akses & manipulasi

list = ["americano", 19, False, 187.5, "Laptop", True, 123]

print(f"Ini elemen pertama : {list[0]}; Dan ini elemen terakhir : {list[-1]}\n")

print(f"Tampilkan anggota list dari 1 sampai 6, dimana skip setiap dua anggota : {list[0:7:2]}\n")

list.append("embegeh") # Tambahkan anggota baru pada list

print(f"Tambahkan list dengan anggota baru 'embegeh' : {list}\n")

list.pop() # Hapus anggota paling terakhir pada list

print(f"Hapus anggota paling terakhir di list : {list}\n")

list.insert(1, "19 Juta Lapangan Pekerjaan") # Tambahkan anggota string di list pada urutan ke 2

print(f"Tambahakan anggota string pada list di urutan ke-2 : {list}\n")

list.extend([19, "Juta Lapangan", False]) # Gabungkan list dengan list baru

print(f"Gabungkan list dengan list lainya : {list}\n")

list.remove("19 Juta Lapangan Pekerjaan") # Hapuskan anggota pada list yang bernilai "19 Juta Lapangan Pekerjaan"

print(f"Hapus anggota didalam list sesuai dengan nilai yang ditentukan : {list}\n")

print(f"===============================\n")

# 2.) Tuple – immutability & unpacking

tuple = ("Go", "For It!", "Nakamura", "Hirose", 2026, 2.2)

print(f"Pada tuple, jumlah anggota nya sebanyak : {len(tuple)}\n")

print(f"Berikut anggota ke 3 dan 4 dari tuple, {tuple[2]} dan {tuple[3]}\n")

anggota_1, anggota_2, anggota_3, *sisa_anggota = tuple

print(f"tampilkan anggota 1 hingga 3 : {anggota_1} {anggota_2} {anggota_3}\n")

print(f"Dan anggota sisanya : {sisa_anggota}\n")

print(f"===============================\n")

# 3.) Set – keunikan & operasi himpunan

makanan_favorit_nakamura = {"onigiri", "nasi_goreng", "sate", "pecel", "gudeg"}

makanan_favorit_hirose = {"pasta", "onigiri", "ramen", "mie_soba_dingin", "sate"}

print(f"Hasil dari union kedua set : {makanan_favorit_nakamura | makanan_favorit_hirose}\n")

print(f"Hasil dari intersection kedua set : {makanan_favorit_nakamura & makanan_favorit_hirose}\n")

print(f"Hasil dari difference kedua set : {makanan_favorit_nakamura - makanan_favorit_hirose}\n")

print(f"Hasil dari symmetric_difference kedua set : {makanan_favorit_nakamura ^ makanan_favorit_hirose}\n")

print(f"===============================\n")

# 4.) Dictionary – key/value dasar

mahasiswa = {
    "nama": "achul",
    "nim": 3312401030,
    "angkatan": 2024,
    "kota": "Batam"
}

mahasiswa["tinggiBadan"] = 161.2    # Tambahkan key baru pada data dict mahasiswa

print(f"Dict mahasiswa ditambahkan key baru untuk tinggBadan : {mahasiswa}\n")

mahasiswa["kota"] = "Jakarta"       # Mengubah value pada key kota

print(f"Mengubah nilai pada key kota di dict mahasiswa, 'kota': {mahasiswa['kota']}\n")

del mahasiswa["angkatan"]           # Menghabus key angkatan pada dict mahasiswa

print(f"Menghapus key angkatan pada dict mahasiswa : {mahasiswa}\n")

for key, value in mahasiswa.items():

    print(f"Pada key : {key}, maka valuenya : {value}")

print(f"===============================\n")

# 5.) Nested structures

makanan_favorit_achul = [
    {
        "nama": "pecel",
        "harga": 15000,
        "rating": 4.5
    },
    {
        "nama": "nasi goreng",
        "harga": 12000,
        "enak": 4.0        
    },
    {
        "nama": "ketoprak",
        "harga": 20000,
        "enak": 3.5
    },
    {
        "nama": "ayam geprek",
        "harga": 18000,
        "enak": 2.5
    }
]

makanan_murah = []

for m in makanan_favorit_achul:

    print(f"Nama-Nama makanan favorti achul : {m["nama"]}")

for m in makanan_favorit_achul:

    if(m["harga"] < 20000):

        makanan_murah.append(m["nama"])

print(f"\nNama-nama Makanan murah : {makanan_murah}\n")

print(f"===============================\n")

# 6.) Comprehension & utilitas

list_genap = []
list_ganjil = []

for i in range(1, 21):

    if(i % 2 == 0):
        list_genap.append(i)
    else:
        list_ganjil.append(i)

print(f"Ini list genap : {list_genap}\n")
print(f"Ini list ganjil : {list_ganjil}\n")

for i in range(1, 11):

    if(i % 2 == 0):
        angka_genap = {
            "angka": i,
            "jenis": "genap"
        }

        print(angka_genap)

    else:
        angka_ganjil = {
            "angka": i,
            "jenis": "ganjil"
        }

        print(angka_ganjil)

kalimat = "Tapi pada hari ini, di Jogja, saya akan lawan."

set_kalimat = {k.lower() for k in kalimat if k != " "}

print(f"\n{set_kalimat}\n")

tenant_gb = ["mixue", "kopken", "baresto", "guardian", "marugame"]

tenant_mm = ["shinlin", "momoyo", "watson", "baresto", "kopken"]

for t in tenant_gb:
    
    if t in tenant_mm:

        print(f"Ada tenant yang sama nih, yaitu {t} dan pada posisi index ke-{tenant_gb.index(t)}")