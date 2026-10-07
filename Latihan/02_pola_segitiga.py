# latihan/02_pola_segitiga.py

n = int(input("n: "))

# Loop luar: Mengontrol jumlah baris dari baris ke-1 hingga ke-n
for i in range(1, n + 1):
    # Loop dalam: Mengontrol jumlah simbol '*' yang dicetak pada baris ke-i (sebanyak i kali)
    for j in range(i):
        # Kondisi: Tidak ada kondisi eksplisit (if)
        
        # Output: Mencetak satu simbol '*' tanpa berpindah baris (diakhiri spasi)
        print("*", end=" ")
    
    # Counter/Akumulator: Menggunakan variabel i secara implisit sebagai penentu batas iterasi loop dalam
    
    # Output: Pindah ke baris baru setelah semua bintang pada baris ke-i selesai dicetak
    print()