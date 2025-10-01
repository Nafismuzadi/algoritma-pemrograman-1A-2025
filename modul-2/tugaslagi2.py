jenis_kendaraan = input("Masukkan jenis kendaraan (mobil pribadi / truk kecil / truk besar): ").lower()
jenis_pembayaran = input("Masukkan jenis pembayaran (e-money / tunai): ").lower()
jam = float(input("Masukkan jam pembayaran (00.00 - 23.59): "))

# Tentukan tarif
if jenis_kendaraan == "mobil pribadi":
    tarif = 15000
elif jenis_kendaraan == "truk kecil":
    tarif = 25000
elif jenis_kendaraan == "truk besar":
    tarif = 40000
else:
    print("Jenis kendaraan tidak valid!")
    exit()

# Hitung diskon
if jenis_pembayaran == "e-money":
    if jam >= 23.00 or jam < 05.00:   # jam sepi
        tarif -= tarif * 0.20
    else:
        tarif -= tarif * 0.10
elif jenis_pembayaran == "tunai": 
    tarif = tarif
else:
    print("Jenis pembayaran tidak valid!")
    exit()

# Output
print("Tarif jalan tol yang harus dibayar adalah : Rp", int(tarif))
