# Perpus Kecil

Aplikasi manajemen koleksi buku perpustakaan berbasis terminal (*Command Line Interface*) menggunakan Python dengan konsep *Object-Oriented Programming* (OOP) dan penyimpanan file CSV.

## Fitur Utama

* **Login Petugas:** Validasi akun petugas dengan batas maksimal 3 kali percobaan.
* **Tambah Buku:** Menambahkan data buku baru dengan pengecekan duplikat kode buku.
* **Tampilkan Semua Buku:** Menampilkan seluruh koleksi buku dalam format tabel terminal.
* **Cari Buku:** Mencari detail buku berdasarkan kode buku.
* **Perbarui Buku:** Mengubah detail dan jumlah stok buku yang sudah tersimpan.
* **Hapus Buku:** Menghapus data buku dengan konfirmasi pengguna.

## Struktur Folder

```text
Perpus_Kecil/
├── data/
│   ├── data_buku.csv             # Penyimpanan data koleksi buku
│   └── data_petugas.csv          # Penyimpanan data akun petugas
├── aplikasi_perpustakaan.py      # Antarmuka menu & tabel terminal
├── buku.py                       # Class model entitas Buku
├── main.py                       # Titik masuk utama program
├── manajer_perpustakaan.py       # Logika bisnis & operasi CRUD
├── penyimpanan_csv.py           # Operasi baca & tulis file CSV
├── petugas.py                    # Class model entitas Petugas
├── Perpustakaan.jpg              # Diagram Class UML sistem
└── README.md