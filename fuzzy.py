def fuzzyfikasi_stok(jumlah_stok):
    # Keanggotaan Minim
    if jumlah_stok <= 30:
        minim = 1
    elif 30 < jumlah_stok <= 40:
        minim = (40 - jumlah_stok) / (40-30)
    else:
        minim = 0

    # Keanggotaan Sedang
    if 35 < jumlah_stok <= 40:
        sedang = (jumlah_stok - 35) / (40 - 35)
    elif 40 < jumlah_stok <= 45:
        sedang = (45 - jumlah_stok) / (45 - 40)
    else:
        sedang = 0

    # Keanggotaan Banyak
    if 40 < jumlah_stok <= 45:
        banyak = (jumlah_stok - 40) / (45 - 40)
    elif jumlah_stok > 45:
        banyak = 1
    else:
        banyak = 0

    return {"minim": minim, "sedang": sedang, "banyak": banyak}

def fuzzyfikasi_permintaan(permintaan):
    # Keanggotaan Rendah
    if permintaan <= 10:
        rendah = 1
    elif 10 < permintaan <= 30:
        rendah = (30 - permintaan) / (30-10)
    else:
        rendah = 0

    # Keanggotaan Sedang
    if 10 < permintaan <= 20:
        sedang = (permintaan - 10) / (20 - 10)
    elif 20 < permintaan <= 30:
        sedang = (30 - permintaan) / (30 - 20)
    else:
        sedang = 0

    # Keanggotaan Tinggi
    if 20 < permintaan <= 40:
        tinggi = (permintaan - 20) / (40 - 20)
    elif permintaan > 40:
        tinggi = 1
    else:
        tinggi = 0

    return {"rendah": rendah, "sedang": sedang, "tinggi": tinggi}

def rule_base(fuzzy_stok, fuzzy_permintaan):
    rules = []
    # Rule 1: Jika stok minim dan permintaan rendah, maka produksi kecil
    rules.append((min(fuzzy_stok['minim'], fuzzy_permintaan['rendah']), 10))

    # Rule 2: Jika stok minim dan permintaan sedang, maka produksi sedang
    rules.append((min(fuzzy_stok['minim'], fuzzy_permintaan['sedang']), 25))

    # Rule 3: Jika stok minim dan permintaan tinggi, maka produksi besar
    rules.append((min(fuzzy_stok['minim'], fuzzy_permintaan['tinggi']), 40))

    # Rule 4: Jika stok sedang dan permintaan rendah, maka produksi tidak produksi
    rules.append((min(fuzzy_stok['sedang'], fuzzy_permintaan['rendah']), 0))

    # Rule 5: Jika stok sedang dan permintaan sedang, maka produksi kecil
    rules.append((min(fuzzy_stok['sedang'], fuzzy_permintaan['sedang']), 10))

    # Rule 6: Jika stok sedang dan permintaan tinggi, maka produksi sedang
    rules.append((min(fuzzy_stok['sedang'], fuzzy_permintaan['tinggi']), 25))

    # Rule 7: Jika stok banyak dan permintaan rendah, maka produksi tidak produksi
    rules.append((min(fuzzy_stok['banyak'], fuzzy_permintaan['rendah']), 0))

    # Rule 8: Jika stok banyak dan permintaan sedang, maka produksi tidak produksi
    rules.append((min(fuzzy_stok['banyak'], fuzzy_permintaan['sedang']), 0))

    # Rule 9: Jika stok banyak dan permintaan tinggi, maka produksi kecil
    rules.append((min(fuzzy_stok['banyak'], fuzzy_permintaan['tinggi']), 10))

    return rules

def defuzzyfikasi(rule_outputs):
    # total numerik (sigma(mu * z)) / sigma(mu)
    total_numerik = sum(mu * z for mu, z in rule_outputs)
    total_mu = sum(mu for mu, z in rule_outputs)
    z = total_numerik / total_mu
    return z

def kategori_produksi(hasil):
    if hasil == 0:
        return "Tidak Produksi"
    elif 0 < hasil <= 10:
        return "Produksi Kecil"
    elif 10 < hasil <= 25:
        return "Produksi Sedang"
    elif hasil > 25:
        return "Produksi Besar"
    else:
        return "Kategori Tidak Dikenali"


# stok = input("Jumlah stok: ")
# permintaan = input("Jumlah Permintaan: ")

# fuzzy_stok = fuzzyfikasi_stok(int(stok))
# fuzzy_permintaan = fuzzyfikasi_permintaan(int(permintaan))
# arr = rule_base(fuzzyfikasi_stok(int(stok)), fuzzyfikasi_permintaan(int(permintaan)))
# hasil = defuzzyfikasi(arr)
# kategori = kategori_produksi(hasil)

# print("\n")
# print(f"Stok Minim: {fuzzy_stok['minim']}")
# print(f"Stok Sedang: {fuzzy_stok['sedang']}")
# print(f"Stok Banyak: {fuzzy_stok['banyak']}")
# print("\n")
# print(f"Permintaan Rendah: {fuzzy_permintaan['rendah']}")
# print(f"Permintaan Sedang: {fuzzy_permintaan['sedang']}")
# print(f"Permintaan Tinggi: {fuzzy_permintaan['tinggi']}")
# print("\n")
# print(f"Rule Base: {arr}")
# print("\n")
# print(f"Hasil Jumlah ({kategori}): {hasil}")