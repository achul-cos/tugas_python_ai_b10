def greet(name: str) -> str:
    return f"Halo, {name}!"

def tambah(a: float, b: float = 0) -> float:
    return a + b;

def rata_rata(angka: list[float]) -> float:

    if len(angka) < 1:
        return 0
    
    else:
        jumlah_total = 0

        for a in angka:

            jumlah_total += a

        angka_rata_rata = jumlah_total / len(angka)

        return round(angka_rata_rata, 2)
    
class Student:

    def __init__(self, nama: str, nim: str, nilai: list[float] = [0]):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tambah_nilai(self, skor: float):
        
        self.nilai.append(skor)

    def rata_nilai(self) -> float:

        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:

        if self.rata_nilai() >= threshold:
            return "LULUS"

        else:
            return "TIDAK LULUS"

    def __str__(self):
        return f"Student (nama='{self.nama}', nim='{self.nim}', rata='{self.rata_nilai()}', status={self.status()})" 

if __name__ == "__main__":

    # === FUNCTIONS ===

    print(greet("Arifian"))

    print(tambah(5, 7))

    print(tambah(10))

    print(rata_rata([80, 90, 100]))

    print(rata_rata([]))

    # === CLASS STUDENT ===

    Achul = Student("Achul", "123", [30, 60, 100, 80])
    Steven = Student("Steven", "0987", [78, 56, 32, 98])

    Achul.tambah_nilai(100)
    Steven.tambah_nilai(76)

    print(Achul.rata_nilai())
    print(Steven.rata_nilai())

    print(Achul.status())
    print(Steven.status())