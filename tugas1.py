#1. Buat variabel list dengan value: [namaKendaraan, Jenis Kendaraan, ccKendaraan, warna kendaraan, roda kendaraan] 
# tambahkan dari list tersebut di belakang dengan value: [harga kendaraan, tipe kendaraan] 
# tambahkan setelah jenis kendaraan dengan value (merk kendaraan]

#A
kendaraan=['Honda beat','sepeda motor',120,'merah',2]
print("kendaraan saya")
print(kendaraan)
print("=========")

#B
kendaraan.append(200000000)
print(kendaraan)
kendaraan.extend({20000000,"metic"})
print(kendaraan)
print("=========")

#C
kendaraan.insert(2,'Honda')
print(kendaraan)
print("=======")