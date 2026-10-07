# latihan/04_hitung_pasangan.py

n = int(input("n: "))

# Counter: Menghitung total pasangan (i, j) yang memenuhi syarat
count = 0

# Loop luar: Mengontrol nilai i dari 1 sampai n
for i in range(1, n + 1):
    # Loop dalam: Mengontrol nilai j dari 1 sampai n
    for j in range(1, n + 1):
        # Kondisi: Memeriksa apakah penjumlahan i + j kurang dari atau sama dengan n
        if i + j <= n:
            # Akumulator/Counter: Menambah nilai count sebanyak 1 jika kondisi terpenuhi
            count += 1

# Output: Menampilkan total pasangan yang memenuhi kondisi
print(f"Banyak pasangan = {count}")