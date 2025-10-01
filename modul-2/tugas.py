JenisKendaraan = input("Masukkan Jenis kendaraan (Mobil pribadi / Truk kecil / Truk besar): ")
JenisPembayaran = input("Masukkan jenis pembayaran (E-Money / Tunai): ")
Jam = float(input("Masukkan jam pembayaran (00.00 - 23.59): "))

if JenisKendaraan == "Mobil pribadi" or "mobil pribadi" or "Mobil Pribadi" or "MOBIL PRIBADI":
    Tarif = 15000
elif JenisKendaraan == "Truk kecil" or "Truk Kecil" or "truk kecil" or "TRUK KECIL":
    Tarif = 25000
elif JenisKendaraan == "Truk besar" or "Truk Besar" or "truk besar" or "TRUK BESAR":
    Tarif = 40000
else :
    print("Jenis kendaraan tidak valid")
    exit()

if JenisPembayaran == "Tunai" or "tunai" or "TUNAI":
    Tarif = Tarif
else:
    Diskon = 0
    Tarif = Tarif
    exit()

if Jam >= 23.00 or Jam < 05.00:
    Tarif = Tarif - (Tarif * 0.20)
    
print("Tarif yang harus dibayar adalah: Rp", int(Tarif))
    
    