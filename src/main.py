# Program Utama (main.py)
from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, tentukan_ketuntasan
from utilitas import cetak_garis

def main():
    cetak_garis(50)
    print("      PROGRAM REKAPITULASI & ANALISIS NILAI KELAS")
    cetak_garis(50)
    
    path_file = "data/nilai_contoh.txt"
    
    # 1. Membaca data dari file
    data_siswa = baca_data(path_file)
    
    if not data_siswa:
        print("Tidak ada data valid yang dapat diproses dari file.")
        return
    
    # 2. Proses perhitungan statistik dan ketuntasan
    statistik = hitung_statistik(data_siswa)
    ketuntasan = tentukan_ketuntasan(data_siswa, kkm=75)
    
    # Menggabungkan dictionary hasil analisis
    hasil_laporan = {**statistik, **ketuntasan}
    
    # 3. Menampilkan hasil ringkas ke terminal
    print("\n[HASIL ANALISIS STATISTIK KELAS]")
    print(f"Total Siswa Terdata : {hasil_laporan['jumlah_data']}")
    print(f"Nilai Rata-rata     : {hasil_laporan['rata_rata']}")
    print(f"Nilai Terendah      : {hasil_laporan['nilai_minimum']}")
    print(f"Nilai Tertinggi     : {hasil_laporan['nilai_maksimum']}")
    print(f"Siswa Tuntas (>=75) : {hasil_laporan['jumlah_tuntas']}")
    print(f"Siswa Belum Tuntas  : {hasil_laporan['jumlah_belum_tuntas']}")
    cetak_garis(50)
    
    # 4. Menyimpan laporan ke file output
    simpan_laporan("output/laporan_ringkas.txt", hasil_laporan)

if __name__ == "__main__":
    main()