# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas[cite: 13]

## 2. Latar Belakang
Guru matematika sering kali membutuhkan waktu yang cukup lama untuk merekap data nilai siswa secara manual, menghitung rata-rata kelas, serta menentukan siapa saja siswa yang sudah tuntas atau belum tuntas berdasarkan KKM. Oleh karena itu, diperlukan program konsol berbasis Python yang dapat membaca data dari file, menghitung statistik secara otomatis, dan menyimpan laporan ringkas dengan cepat dan konsisten[cite: 7, 8, 13].

## 3. Pengguna dan Tujuan
- **Pengguna Utama:** Guru Matematika[cite: 8].
- **Tujuan:** Membantu guru mendapatkan rekapitulasi nilai, statistik kelas, dan status ketuntasan siswa secara otomatis dan akurat[cite: 8, 13].

## 4. Ruang Lingkup
- Membaca data nilai dari file teks eksternal[cite: 13].
- Memvalidasi rentang nilai (0 s.d. 100)[cite: 13].
- Menghitung nilai rata-rata, minimum, dan maksimum[cite: 13].
- Menentukan jumlah siswa tuntas dan belum tuntas berdasarkan KKM (75)[cite: 13].
- Menyimpan hasil laporan ke dalam file teks[cite: 13].
- *Batasan:* Program berjalan berbasis terminal/konsol (*command line*) menggunakan bahasa Python[cite: 7].

## 5. Kebutuhan (Fungsional & Nonfungsional)
- **Fungsional:**
  - F01: Program dapat membaca data nilai dari file[cite: 8].
  - F02: Program memvalidasi nilai berada di rentang 0–100[cite: 8].
  - F03: Program menghitung rata-rata, nilai minimum, dan maksimum[cite: 8].
  - F04: Program menentukan status tuntas atau belum tuntas[cite: 8].
  - F05: Program menyimpan laporan ke file teks[cite: 8].
- **Nonfungsional:** Mudah dijalankan dari terminal VS Code dan pesan kesalahan mudah dipahami[cite: 8].

## 6. Spesifikasi Input, Proses, dan Output (IPO)
- **Input:** File teks (`nilai_contoh.txt`) berisi nama dan nilai siswa[cite: 9].
- **Proses:** Membaca baris file, memvalidasi angka, menghitung statistik matematika, dan mengklasifikasikan ketuntasan[cite: 9].
- **Output:** Tampilan ringkasan di terminal dan file laporan tersimpan di folder `output/`[cite: 9, 10].

## 7. Algoritma (Pseudocode)
```text
MULAI
Baca data dari file nilai_contoh.txt
Untuk setiap baris data:
    Validasi format dan rentang nilai (0-100)
    Simpan data yang valid ke dalam list/dictionary
Hitung statistik (rata-rata, min, max)
Tentukan status ketuntasan siswa berdasarkan KKM
Tampilkan ringkasan hasil analisis ke terminal
Simpan laporan ke folder output/
SELESAI