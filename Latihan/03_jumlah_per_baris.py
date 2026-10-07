# latihan/03_jumlah_per_baris.py

# Loop luar: Mengontrol nomor baris i dari 1 sampai 4
for i in range(1, 5):
    # Akumulator: Menyimpan dan mereset jumlah total nilai i * j untuk baris ke-i saat ini
    total_baris = 0
    
    # Loop dalam: Mengontrol kolom j dari 1 sampai 3 pada baris ke-i
    for j in range(1, 4):
        # Kondisi: Tidak ada kondisi eksplisit (if)
        
        # Akumulator: Menambahkan hasil perkalian i * j ke dalam total_baris
        total_baris += i * j
    
    # Output: Menampilkan hasil penjumlahan seluruh kolom pada baris ke-i
    print(f"Jumlah baris {i} = {total_baris}")