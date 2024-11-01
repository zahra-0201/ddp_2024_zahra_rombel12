print("Nomor 1")
kendaraan = ['scoopy', 'motor', 200, 'pink', 2]
kendaraan.append('Rp. 25.000.000')
kendaraan.append('matic')
print(kendaraan)
kendaraan.insert(2, 'honda')
print(kendaraan)
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

print()
print("Nomor 2")
hitungluas = input("""Pilih salah satu angka dibawah
1. Hitung luas persegi
2. Hitung luas lingkaran
3. Hitung luas segitiga
""")
match hitungluas:
    case "1":
        print("Menghitung luas persegi")
        sisi = int(input("Masukkan nilai sisi "))
        luaspersegi = sisi*sisi
        print("Nilai luas persegi dengan sisi", sisi, "cm adalah", luaspersegi, "cm^2")
    case "2":
        print("Menghitung luas lingkaran")
        r = int(input('Masukkan nilai jari jari '))
        tinggi = int(input('Masukkan nilai tinggi '))
        phi = 22/7
        luaslingkaran = int((2*phi*r*tinggi)+(2*phi*r**2))
        print("Nilai luas lingkaran dengan jari-jari", r, "cm dan tinggi", tinggi, "cm adalah", luaslingkaran, "cm^2")
    case "3":
        print("Menghitung luas segitiga")
        alas = int(input('Masukkan nilai alas '))
        tinggiS = int(input('Masukkan nilai tinggi '))
        luassegitiga = alas*tinggiS/2
        print("Nilai luas segitiga dengan alas", alas, "cm dan tinggi", tinggiS, "cm adalah", luassegitiga, "cm^2")
    case _:
        print("Pilihan tidak valid")
