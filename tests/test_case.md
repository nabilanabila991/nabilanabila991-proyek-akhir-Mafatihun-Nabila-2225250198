# Dokumentasi Test Case - Analisis Nilai Matematika

| ID | Kategori | Input / Kondisi | Expected Result (Hasil yang Diharapkan) |
|---|---|---|---|
| TC01 | Normal | Nilai: 85, 72, 90, 65, 88 | Rata-rata terhitung benar, statistik min/max sesuai |
| TC02 | Batas | Nilai: 0 | Diterima sebagai nilai valid (batas bawah) |
| TC03 | Batas | Nilai: 100 | Diterima sebagai nilai valid (batas atas) |
| TC04 | Invalid | Nilai: 105 atau teks "abc" | Ditolak oleh fungsi validasi dan diabaikan |
| TC05 | Invalid | File `nilai_contoh.txt` tidak ada | Menampilkan pesan `FileNotFoundError` tanpa crash |
| TC06 | Normal | Semua nilai >= KKM (75) | Jumlah tuntas sama dengan total keseluruhan data |