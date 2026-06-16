# 1.) Import & Setup

# Import Module Numpy, Pandas dan OS
import numpy as np
import pandas as pd
import os

# Menentukan seed untuk numpy random agar data random bersifat statis
# disetiap pengujian.
np.random.seed(42)

# 2.) NumPy – Data & Statistik

# Membuat data random int dengan range 0 hingga 100
# dengan jumlah data random yaitu 30
# dan disimpam dalam tipe data list yang berisi anggota bertipe data int
nilai_ujian = np.random.randint(0, 101, size=30)
print(f"Ini data random nilai ujian : {nilai_ujian}\n")

# hitung rata-rata data random tersebut
rata_nilai_ujian = np.mean(nilai_ujian)
print(f"Ini rata-rata data random nilai ujian : {rata_nilai_ujian}\n")

# hitung median (nilai tengah) dari data random tersebut
median_nilai_ujian = np.median(nilai_ujian)
print(f"Ini median data random nilai ujian : {median_nilai_ujian}\n")

# hitung standar deviasi (simpangan) dari data random tersebut
std_nilai_ujian = np.std(nilai_ujian)
print(f"Ini standar deviasi dari data random : {std_nilai_ujian}\n")

# hitung nilai minimum dari data random tersebut
min_nilai_ujian = np.min(nilai_ujian)
print(f"Ini nilai minimum dari data random : {min_nilai_ujian}\n")

# hitung nilai maksimum dari data random tersebut
max_nilai_ujian = np.max(nilai_ujian)
print(f"Ini adalah nilai maksimum dari data random : {max_nilai_ujian}\n")

print(f"===========================================\n")

# 3.) pandas – DataFrame

# Buat data frame pandas dengan minimal 5 baris kolom berserta nilai-nilainya
data_frame = {
    'nama': ['Achul', 'Valdo', 'Steven', 'Tatik', 'Hasi', 'Dion', 'Arya', 'Oki', 'Kayla', 'Rahel', 'Shinta'],
    'nim': ['111', '222', '333', '444', '555', '666', '777', '888', '999', '1000', '1100'],
    'nilai': nilai_ujian[0:11],
    'alamat': ['sagulung', 'batu aji', 'puskopkar', 'tembesi', 'nagoya', 'batu ampar', 'lubuk baja', 'piayu', 'barelang', 'batu aji', 'jakarta'],
    'tinggi': [161.2, 162.2, 181.3, 160.1, 159.7, 161.7, 186.8, 172.7, 160.2, 160.9, 162.8]
}

data_mahasiswa = pd.DataFrame(data_frame)
print(f"{data_mahasiswa}\n")

# Tambahkan kolom 'status' pada dataframe yang berisi 'LULUS' jika data_mahasiswa["nilai"] >= 70, dan sebaliknya yaitu "TIDAK LULUS"
data_mahasiswa["status"] = np.where(data_mahasiswa["nilai"] >= 70, "LULUS", "TIDAK LULUS")
print(f"Ini adalah data mahasiswa yang telah ditambahkan kolom status :\n{data_mahasiswa}\n")

# Tampilkan data mahasiswa 5 teratas saja
print(f"Ini adalah data_mahasiswa 5 teratas :\n{data_mahasiswa.head(5)}\n")

# Hitung jumlah data mahasiswa, mahasiswa lulus dan tidak lulus
jumlah_data_mahasiswa = len(data_mahasiswa)
mahasiswa_lulus = len(data_mahasiswa[data_mahasiswa['status'] == 'LULUS'])
mahasiswa_tidak_lulus = jumlah_data_mahasiswa - mahasiswa_lulus
print(f"Jumlah data mahasiswa : {jumlah_data_mahasiswa}\n")
print(f"Jumlah data mahasiswa lulus : {mahasiswa_lulus}\n")
print(f"Jumlah data mahasiswa tidak lulus : {mahasiswa_tidak_lulus}\n")

print(f"===========================================\n")

# 4.) File I/O – Tulis Ringkasan ke .txt

# Membuat sebuah dokumen dan membukanya, dan menulisnya
with open('ringkasan_tugas6.txt', 'w') as file:

    file.write(
f"""===== Numpy =====

Ini data-data random nilai ujian :
{nilai_ujian}

Rata-rata nilai ujian :
{rata_nilai_ujian}

Median nilai ujian:
{median_nilai_ujian}

Standar Deviasi nilai ujian:
{std_nilai_ujian}

Nilai maksimal dari nilai ujian:
{max_nilai_ujian}

Nilai minimum dari nilai ujian:
{min_nilai_ujian}

===== Pandas | Data Mahasiswa =====

Data mahasiswa 5 teratas:

{data_mahasiswa.head(5)}

Jumlah mahasiswa : {jumlah_data_mahasiswa}

Jumlah mahasiswa lulus : {mahasiswa_lulus}      Tidak lulus : {mahasiswa_tidak_lulus}""")
    
# 5.) OOP Sederhana

class GradeBook:

    def __init__(self, data = data_mahasiswa):
        self.data = data

    def average(self) -> float:
        rata_nilai_mahasiswa = np.mean(self.data["nilai"])

        return round(rata_nilai_mahasiswa, 1)
    
    def pass_rate(self, threshold:float = 70.0) -> float:
        jumlah_mahasiswa = len(self.data)
        jumlah_mahasiswa_lulus = len(self.data[self.data["status"] == "LULUS"])
        jumlah_mahasiswa_tidak_lulus = len(self.data[self.data["status"] != "LULUS"])
        
        persentase_kelulusan = jumlah_mahasiswa_lulus / jumlah_mahasiswa * 100.0

        return round(persentase_kelulusan, 2)
    
    def save_summary(self, path:str = 'ringkasan_tugas6.txt'):

        with open(path, 'a') as file:
            file.write(
f"""
===== GradeBook =====

Rata-rata nilai mahasiswa = {self.average()}

Persentase kelulusan mahasiswa = {self.pass_rate()}""")
    
# 6.) Demo

if __name__ == "__main__":

    # === NUMPY ===
    print(f"Ringkasan Numpy : \n")
    print(f"Ini rata-rata data random nilai ujian : {rata_nilai_ujian}")
    print(f"Ini median data random nilai ujian : {median_nilai_ujian}")
    print(f"Ini standar deviasi dari data random : {std_nilai_ujian}")
    print(f"Ini nilai minimum dari data random : {min_nilai_ujian}")
    print(f"Ini adalah nilai maksimum dari data random : {max_nilai_ujian}")

    # === PANDAS ===
    print(f"\nRingkasan Pandas dan Data Frame : \n")
    print(f"Ini adalah data_mahasiswa 5 teratas :\n{data_mahasiswa.head(5)}\n")

    # === OOP: GRADEBOOK ===
    print(f"\nRingkasan OOP: Gradebook : \n")
    gb = GradeBook()
    print(gb)
    print(f"Rata-rata nilai mahasiswa : {gb.average()}\n")
    print(f"Persentase kelulusan mahasiswa : {gb.pass_rate()}%\n")
    gb.save_summary()

# Link Repo : https://github.com/achul-cos/tugas_python_ai_b10/blob/main/tugas6.py