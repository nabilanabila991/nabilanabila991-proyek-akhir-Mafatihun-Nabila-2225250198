# Modul data_io.py untuk membaca, memvalidasi, dan menulis laporan file

def baca_data(path):
    """Membaca file nilai dan mengembalikan data list berisi dictionary."""
    data_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    parts = baris.split(",")
                    if len(parts) == 2:
                        nama = parts[0].strip()
                        try:
                            nilai = float(parts[1].strip())
                            if validasi_nilai(nilai):
                                data_list.append({"nama": nama, "nilai": nilai})
                        except ValueError:
                            pass  # Abaikan baris jika nilai bukan angka valid
    except FileNotFoundError:
        print(f"Error: File '{path}' tidak ditemukan.")
    return data_list

def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada di rentang valid 0 sampai 100."""
    return 0 <= nilai <= 100

def simpan_laporan(path, hasil_statistik):
    """Menulis ringkasan hasil analisis ke dalam file laporan teks."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write("=== LAPORAN REKAPITULASI NILAI MATEMATIKA ===\n")
            for key, value in hasil_statistik.items():
                file.write(f"{key.replace('_', ' ').title()}: {value}\n")
        print(f"Laporan berhasil disimpan ke folder {path}")
    except Exception as e:
        print(f"Gagal menyimpan laporan: {e}")