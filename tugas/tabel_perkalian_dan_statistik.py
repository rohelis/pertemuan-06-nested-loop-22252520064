# latihan/05_tabel_perkalian_statistik.py

print("Tabel Perkalian dan Statistik")

# 1. Validasi input n dengan loop while
n = int(input("n: "))
while n <= 0:
    print("Nilai n harus berupa integer positif!")
    n = int(input("n: "))

# 2. Inisialisasi akumulator total keseluruhan dan counter hasil genap
total_semua = 0
count_genap = 0

# Loop luar: Mengontrol baris i dari 1 sampai n
for i in range(1, n + 1):
    # Akumulator: Menyimpan total hasil perkalian untuk baris ke-i
    total_baris = 0
    
    # Loop dalam: Mengontrol kolom j dari 1 sampai n
    for j in range(1, n + 1):
        # Hitung hasil perkalian sel
        hasil = i * j
        
        # Akumulator: Menambahkan hasil ke total baris dan total keseluruhan
        total_baris += hasil
        total_semua += hasil
        
        # Kondisi: Memeriksa apakah hasil perkalian bernilai genap
        if hasil % 2 == 0:
            # Counter: Menambah jumlah hasil genap jika kondisi terpenuhi
            count_genap += 1
            
        # Output: Menampilkan angka tabel secara teratur
        print(f"{hasil:4d}", end="")
    
    # Output: Menampilkan total baris ke-i di ujung kanan baris
    print(f" | Jumlah baris {i} = {total_baris}")

# Output: Menampilkan statistik total keseluruhan dan banyak hasil genap
print(f"Total semua = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")