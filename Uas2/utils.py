biodata = {}
sks_list = []
nilai_list = []

def biodata_lengkap():
    return "nama" in biodata and "nim" in biodata

def konversi_nilai_ke_bobot(nilai):
    if nilai >= 85:
        return 4
    elif nilai >= 80:
        return 3.75
    elif nilai >= 75:
        return 3.5
    elif nilai >= 70:
        return 3
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.5
    elif nilai >= 55:
        return 2
    elif nilai >= 45:
        return 1
    else:
        return 0

def konversi_huruf_ke_bobot(huruf):
    mapping = {
        "a": 4, "a-": 3.75, "b+": 3.5,
        "b": 3, "b-": 2.75,
        "c+": 2.5, "c": 2,
        "d": 1, "e": 0
    }
    return mapping.get(huruf.lower(), 0)