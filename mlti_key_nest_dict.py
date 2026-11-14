import datetime
import os
import string
import random

# template dict perpustakaan
perpus_template = {
    'judul':'judul', 
    'penulis':'penulis', 
    'tahun_terbit': datetime.datetime(1111,1,11), 
    'tanggal_terakhir_pinjam' : datetime.datetime(1111,1,11),
    'status' : "status"
}

data_perpustakaan = {} 
while True: 
    os.system("cls")
    print(f"{'DATA BUKU PERPUSTAKAAN':^96}")  
    print("-"*96)

    perpus = dict.fromkeys(perpus_template.keys()) 
    perpus['judul'] = input("Judul Buku\t\t: ")
    perpus['penulis'] = input("Penulis Buku\t\t: ")
    TAHUN_TERBIT = int(input("Tahun terbit (YYYY)\t: "))
    BULAN_TERBIT = int(input("Bulan terbit (1-12)\t: "))
    TANGGAL_TERBIT = int(input("Tanggal terbit (1-31)\t: "))
    perpus['tahun_terbit'] = datetime.datetime(TAHUN_TERBIT, BULAN_TERBIT, TANGGAL_TERBIT)
    TAHUN_PINJAM = int(input("Tahun pinjam (YYYY)\t: "))
    BULAN_PINJAM = int(input("Bulan pinjam (1-12)\t: "))
    TANGGAL_PINJAM = int(input("Tanggal pinjam (1-31)\t: "))
    perpus['tanggal_terakhir_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    perpus['status'] = input("Status Buku\t\t: ")

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) 
    data_perpustakaan.update({KEY:perpus}) 

    print(f"\n{'KEY':<6} {'Judul':<20} {'Penulis':<17} {'Tahun Terbit':<17} {'Tanggal Pinjam':<17} {'Status':<10}") 
    print('-'*96) 

    for perpus in data_perpustakaan:    
        KEY = perpus      
        JUDUL = data_perpustakaan[KEY]['judul']   
        PENULIS = data_perpustakaan[KEY]['penulis']   
        tahun_terbit = data_perpustakaan[KEY]['tahun_terbit'].strftime("%x") 
        tanggal_terakhir_pinjam = data_perpustakaan[KEY]['tanggal_terakhir_pinjam'].strftime("%x")
        STATUS = data_perpustakaan[KEY]['status']
        print(f"{KEY:<6} {JUDUL:<20} {PENULIS:<17} {tahun_terbit:<17} {tanggal_terakhir_pinjam:<17} {STATUS:<10}")   
    print("\n")
    is_done = input("Tambah data lagi (y/n)? ") 
    if is_done == "n": 
        break
print("\nAkhir dari program, Terima kasih") 