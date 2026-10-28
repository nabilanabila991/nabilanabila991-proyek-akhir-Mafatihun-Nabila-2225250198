# Modul utilitas.py untuk fungsi pendukung tampilan atau format teks

def cetak_garis(panjang=45):
    """Mencetak garis pembatas di terminal agar rapi."""
    print("=" * panjang)

def format_pesan_status(pesan):
    """Mengembalikan format teks status operasional."""
    return f"[INFO PROGRAM] {pesan}"