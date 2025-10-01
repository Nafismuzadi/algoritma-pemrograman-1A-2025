jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil pribadi / Truk kecil / Truk besar) : ").lower()
jenis_pembayaran = input("Masukkan jenis pembayaran (E-Money / Tunai) : ").lower()
jam = float(input("Masukkan jam pembayaran (00.00 - 23.59) : "))

if jenis_kendaraan == "mobil pribadi":
    tarif = 15000
elif jenis_kendaraan == "truk kecil":
    tarif = 25000
elif jenis_kendaraan == "truk besar":
    tarif = 40000
else:
    print("jenis kendaraan tidak valid")
    exit()
    
if jenis_pembayaran == "e-money":
    tarif = tarif - (tarif * 0.10)
    if jam >= 23.00 or jam <= 05.00:
        tarif = tarif - (tarif * 0.10)
    elif jenis_pembayaran == "tunai":
        tarif = tarif

print("Tarif jalan tol yang harus dibayar adalah : Rp", int(tarif))

        