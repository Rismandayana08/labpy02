## Nama : Aldi Rismandayana
## Kelas : TI.24.A1

# LABPY02
## Code Program Diskon Tiket
```python
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

    return f"Total harga yang harus dibayar oleh anda adalah: Rp{int(harga)}"

# Input dari user
tipe_tiket = input("Masukkan jenis tiket anda (reguler/vip): ")
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower() == 'ya'

print(hitung_harga_tiket(tipe_tiket, member))
```
## Output Program 
````markdown
Masukkan jenis tiket anda (reguler/vip): vip
Apakah Anda memiliki kartu member? (ya/tidak): ya
Total harga yang harus dibayar oleh anda adalah: Rp80000

Masukkan jenis tiket anda (reguler/vip): vip
Apakah Anda memiliki kartu member? (ya/tidak): tidak
Total harga yang harus dibayar oleh anda adalah: Rp100000

Masukkan jenis tiket anda (reguler/vip): reguler
Apakah Anda memiliki kartu member? (ya/tidak): ya
Total harga yang harus dibayar oleh anda adalah: Rp40000

Masukkan jenis tiket anda (reguler/vip): reguler
Apakah Anda memiliki kartu member? (ya/tidak): tidak
Total harga yang harus dibayar oleh anda adalah: Rp50000
````
## Cara Kerja Program 
- Mulai (start)
- Input Tipe Tiket : pengguna memasukan jenis tiket, yaitu berupa REGULER dan VIP
- Program memeriksa pilihan tiket :
    1. Jika pengguna memilih "reguler", harga tiket di-set ke harga reguler.
    2. Jika memilih "VIP", harga tiket di-set ke harga VIP.
    3. Jika pilihan tidak valid, program memberi tahu pengguna dan berhenti.
- input Status Member :
  Program kemudian bertanya apakah pengguna memiliki kartu member
  dengan jawaban "ya" atau "tidak". Jawaban ini juga diubah menjadi huruf kecil.
- Program memeriksa apakah pengguna adalah member :
     1. Jika "ya", total harga dihitung dengan diskon 20%.
     2. Jika "tidak", total harga sama dengan harga tiket yang dipilih.
     3. Akhir (End) : proses selesai




## Flowchart Diskon Tiket
  ![Flowchart](new/flowcharttiket.png)







## Flowchart Kalkulator
  ![Flowchart](new/Flowchartkalkulator.png)

