# latihan/01_pasangan_indeks.py

# Counter: Menghitung total pasangan yang tercetak
count = 0

# Loop luar: Berjalan untuk i = 1, 2, 3
for i in range(1, 4):
    # Loop dalam: Berjalan untuk j = 1, 2, 3, 4 pada setiap nilai i
    for j in range(1, 5):
        # Kondisi: Tidak menggunakan kondisi (if)
        
        # Output: Mencetak pasangan (i, j)
        print(i, j)
        
        # Akumulator/Counter: Menambah nilai count sebanyak 1
        count += 1

# Output: Mencetak hasil akhir total pasangan
print(f"Banyak pasangan = {count}")