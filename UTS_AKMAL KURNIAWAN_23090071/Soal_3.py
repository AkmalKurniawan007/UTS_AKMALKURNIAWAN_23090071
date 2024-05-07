jumlah_barang = int(input("Masukkan jumlah barang: "))

total = 0
for i in range(jumlah_barang):
    harga_barang = float(input(f"Masukkan harga barang ke-{i+1}: "))
    total += harga_barang

print("Total belanjaan:", total)
