# 1.) Deklrasikan 5 variabel dengan tipe data yaitu integer, string, boolean, float dan list, dan masing-masing memili tipe data yang berbeda

usia = 20                                                                   # Variebel integer
tinggiBadan = 161.2                                                         # Variabel float
isMagang = False                                                            # Variabel bool
nama = "Achul"                                                              # Variabel string
aset = ["Laptop", "Iphone 11 Pro", "Americano", "Motor", "Akun Github"]     # Variabel list

# 2.) Manipulasi string

# munculkan string dengan print()
print("Halo, berikut informasi tentang diriku:\n")

print(nama)

print(f"jumlah aset yang kumiliki adalah: {len(aset)}\n")

print(f"Kalau namaku di tulis capslock, jadinya {nama.upper()}\n")

print(f"Kalau namaku di tulis kecil, jadinya {nama.lower()}\n")

# 3.) Operasi matematika sederhana

print(f"Usiaku di 10 tahun kedepan yaitu {usia + 10}\n")

print(f"Tinggi badanku dibagi dua sama dengan {tinggiBadan / 2}\n")

print(f"Usiaku dibagi enam sama dengan {usia // 6}\n")

print(f"Jumlah aset ku kalau dibagi 5 yaitu {len(aset) / 5}\n")

print(f"Tinggi badanku kalau dikali sebanyak 4 menjadi {tinggiBadan * 4}\n")

print(f"Jika tinggi badanku dibagi 17, dia akan menghasilkan desimal. Karena pembagiannya tidak sempurna karena menghasil sisa bagi.\n Maka sisa baginya yaitu {tinggiBadan % 17}\n")

# 4.) List dan akses elemen

print(f"Aset paling pertamaku yaitu {aset[0]}\n")

aset.pop()

print(f"Sekarang aset ku paling terakhir dihapus, maka sekarang asetku jadinya {aset}\n")

aset.remove("Americano")

print(f"Astaga... sekarang americano ku diambil Meiske, sekarang sisa asetku menjadi {aset}\n")

aset.remove(aset[2])

print(f"Astaga Tuhan... Salah Aset ku menghilang, sekarang asetku menjadi {aset}\n")

# 5.) Input dan Ouput User

namaUser = str(input("Oh halo! Siapa namamu: "))
umurUser = int(input("\nKalau umurmu berapa : "))

print(f"\nHalooww {namaUser}, senang bertemu denganmu. Kamu kapan ulang tahun ke {umurUser + 1} nya?")