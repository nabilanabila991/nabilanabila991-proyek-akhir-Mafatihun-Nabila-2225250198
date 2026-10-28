# Modul analisis.py untuk perhitungan statistik dan penentuan ketuntasan

def hitung_statistik(data_list):
    """Menghitung rata-rata, nilai minimum, dan maksimum dari data siswa."""
    if not data_list:
        return {"rata_rata": 0, "nilai_minimum": 0, "nilai_maksimum": 0, "jumlah_data": 0}
    
    nilai_saja = [item["nilai"] for item in data_list]
    rata_rata = sum(nilai_saja) / len(nilai_saja)
    nilai_min = min(nilai_saja)
    nilai_max = max(nilai_saja)
    
    return {
        "rata_rata": round(rata_rata, 2),
        "nilai_minimum": nilai_min,
        "nilai_maksimum": nilai_max,
        "jumlah_data": len(nilai_saja)
    }

def tentukan_ketuntasan(data_list, kkm=75):
    """Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM."""
    tuntas = 0
    belum_tuntas = 0
    
    for item in data_list:
        if item["nilai"] >= kkm:
            tuntas += 1
        else:
            belum_tuntas += 1
            
    return {"jumlah_tuntas": tuntas, "jumlah_belum_tuntas": belum_tuntas}