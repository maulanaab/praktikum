# Latihan No-1 ------------------------------------------
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# # Menambahkan truk di akhir list
kendaraan.append("truk")
print(f"Kendaraan setelah ditambahkan truk = {kendaraan}")
# # Sisipkan becak pada index ke-1
kendaraan.insert(1, "becak")
print(f"Kendaraan setelah disisipkan becak = {kendaraan}")
# # Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()
print(f"Kendaraan setelah dihapus elemen terakhir = {kendaraan}")
# # Ubah elemen 'sepeda' menjadi 'skuter'
kendaraan[2] = "skuter"
print(f"Kendaraan setelah diubah = {kendaraan}")
# # Tampilkan informasi jumlah total data di dalam list tersebut
total_kendaraan = len(kendaraan)
print(f"Jumlah total data kendaraan = {total_kendaraan}")

# Latihan No-2 ------------------------------------------
angka = [75, 80, 90, 75, 85, 100, 65] 

# # Cari tahu di indeks ke berapa skor 100 berada
Index_100 = angka.index(100)
print(f"Skor 100 berada di index {Index_100}")
# # Hitung ada berapa banyak siswa yang mendapatkan skor 75.
jumlah_75 = angka.count(75)
print(f"Jumlah siswa yang mendapatkan skor 75 = {jumlah_75}")
# # Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
angka.sort()
print(f"Skor ujian setelah diurutkan = {angka}")
# # Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil. 
angka.reverse()
print(f"Skor ujian setelah dibalik urutannya = {angka}")

# Latihan No-3 ------------------------------------------
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print(f"Menu utama sebelum ditambahkan menu tambahan = \n{menu_utama}")
# # Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut
menu_utama.extend(menu_tambahan)
print(f"Menu utama setelah ditambahkan menu tambahan = \n{menu_utama}")

# Latihan No-4 ------------------------------------------
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# # Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut
harga_pensil = data_barang[1][1]
print(f"Harga Pensil = {harga_pensil}")
# # Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: 
# # "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya
for barang in data_barang:
    print(f"Nama = {barang[0]}, Harga = {barang[1]}")