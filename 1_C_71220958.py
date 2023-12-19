print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:1")
print("hasil", billpertama+billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:2")
print("hasil", billpertama-billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:3")
print("hasil", billpertama*billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:4")
print("hasil", billpertama/billkedua)




while True:
    print("\nPilih Menu:")
    print("1. Tambah Penduduk\n2. Tampilkan Urut Nama\n3. Tampilkan Urut Usia")
    
    try:
        pilihan = int(input("Pilihan Anda: "))
    except ValueError:
        print("Masukkan angka sebagai pilihan.")
        continue

    if pilihan == 1:
        nama = input("Masukkan Nama: ")
        try:
            usia = int(input("Masukkan Usia: "))
        except ValueError:
            print("Masukkan angka sebagai usia.")
            continue

        root = tambah_penduduk(root, nama, usia)
        print("Data berhasil ditambahkan!")

    elif pilihan == 2:
        print("Daftar Penduduk:")
        tampilkan_urut_nama(root)

    elif pilihan == 3:
        print("Daftar Penduduk:")
        tampilkan_urut_usia(root)

    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")




