#2. Buat program python dengan match case untuk menghitung luas bangun datar
# jika pilih 1, maka menghitung luas persegi
#jika pilih 2, maka menghitung luas lingkaran
#jika pilih 3, maka menghitung luas segitiga
#Kalau pilihannya tidak ada maka ada keterangan: salah pilih


print('ini adalah progam sederhana untuk menghitung luas bangun datar')
print("pilih menu angka 1-3 : \n1.persegi\n2.lingkaran\n3.segitiga")
pilihmenu= int(input("silahkan pilih menu dengan mengetikan angka 1-3:"))

match pilihmenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi=int(input("silahkan masukan nilai yang mau dihitung "))
        hitung=sisi*sisi
        print(f"luas persegi adalah : {hitung}")
    case 2:
        print("ini adalah menu untuk menghitung luas lingkaran")
        jari=int(input("silahkan masukan nilai yang mau dihitung"))
        hitung=int(22/7*jari*jari)
        print(f"luas lingkaran adalah : {hitung}")
    case 3:
        print("ini adalah menu untuk menghitung luas segitiga")
        alas=int(input("silahkan masukan alas" ))
        tinggi=int(input("silahkan masukan tinggi" ))
        hitung=int(1/2*alas*tinggi)
        print(f"luas segitiga adalah : {hitung}")
    case _:
        print("pilihan tidak valid,silahkan pilih antar 1-3")