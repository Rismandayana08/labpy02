def hitung_harga_tiket(tipe_tiket, member):
    harga_reguler = 50000
    harga_vip = 100000
    diskon = 0.2

    if tipe_tiket.lower() == 'reguler':
        harga = harga_reguler
    elif tipe_tiket.lower() == 'vip':
        harga = harga_vip
    else:
        return "Tipe tiket tidak valid."

    if member:
        harga *= (1 - diskon)

    return f"Total harga yang harus dibayar: Rp{int(harga)}"

# Input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ")
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower() == 'ya'

print(hitung_harga_tiket(tipe_tiket, member))
