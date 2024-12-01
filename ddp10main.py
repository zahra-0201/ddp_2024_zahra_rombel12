from ddp10aritmatika import *
from ddp10bangundatar import *
from ddp10bangunruang import *


def hitungan_aritmatika():
    print("\nPilih operasi aritmatika yang ingin dilakukan:")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-5): "))

    if pilihan == 1:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil pertambahan:", tambah(a, b))
    elif pilihan == 2:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil pengurangan:", kurang(a, b))
    elif pilihan == 3:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil perkalian:", kali(a, b))
    elif pilihan == 4:
        a = float(input("Masukkan angka pembilang: "))
        b = float(input("Masukkan angka penyebut (tidak boleh nol): "))
        print("Hasil pembagian:", bagi(a, b))
    elif pilihan == 5:
        a = float(input("Masukkan angka dasar: "))
        b = float(input("Masukkan pangkat: "))
        print("Hasil perpangkatan(eksponensial): ", pangkat(a, b))
    else:
        print("Pilihan tidak valid.")


def hitungan_bangun_datar():
    print("\nPilih bangun datar yang ingin dihitung:")
    print("1. Luas Lingkaran")
    print("2. Luas Persegi")
    print("3. Luas Segitiga")
    print("4. Luas Persegi Panjang")
    print("5. Luas Jajar Genjang")
    
    pilihan = int(input("\nMasukkan nomor bangun datar yang dipilih (1-5): "))
    
    if pilihan == 1:
        jari_jari = float(input("Masukkan nilai jari-jari lingkaran: "))
        print("Luas Lingkaran:", luas_lingkaran(jari_jari))
    elif pilihan == 2:
        sisi = float(input("Masukkan nilai sisi persegi: "))
        print("Luas Persegi:", luas_persegi(sisi))
    elif pilihan == 3:
        alas = float(input("Masukkan nilai alas segitiga: "))
        tinggi = float(input("Masukkan nilai tinggi segitiga: "))
        print("Luas Segitiga:", luas_segitiga(alas, tinggi))
    elif pilihan == 4:
        panjang = float(input("Masukkan nilai panjang persegi panjang: "))
        lebar = float(input("Masukkan nilai lebar persegi panjang: "))
        print("Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
    elif pilihan == 5:
        alas = float(input("Masukkan nilai alas jajar genjang: "))
        tinggi = float(input("Masukkan nilai tinggi jajar genjang: "))
        print("Luas Jajar Genjang:", luas_jajar_genjang(alas, tinggi))
    else:
        print("Pilihan tidak valid.")
    
def hitungan_bangun_ruang():
    print("\nPilih bangun ruang yang ingin dihitung:")
    print("1. Luas Permukaan Kubus")
    print("2. Luas Permukaan Balok")
    print("3. Luas Permukaan Tabung")
    print("4. Luas Permukaan Limas")
    print("5. Luas Permukaan Prisma")
    
    pilihan = int(input("\nMasukkan nomor bangun ruang yang dipilih (1-5): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan nilai panjang sisi kubus: "))
        print("Luas Permukaan Kubus:", luas_permukaan_kubus(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan nilai panjang balok: "))
        lebar = float(input("Masukkan nilai lebar balok: "))
        tinggi = float(input("Masukkan nilai tinggi balok: "))
        print("Luas Permukaan Balok:", luas_permukaan_balok(panjang, lebar, tinggi))
    elif pilihan == 3:
        jari_jari = float(input("Masukkan nilai jari-jari tabung: "))
        tinggi = float(input("Masukkan nilai tinggi tabung: "))
        print("Luas Permukaan Tabung:", luas_permukaan_tabung(jari_jari, tinggi))
    elif pilihan == 4:
        luas_alas = float(input("Masukkan nilai luas alas limas: "))
        luas_sisi_tegak = float(input("Masukkan nilai jumlah luas sisi tegak: "))
        print("Luas Permukaan Limas:", luas_permukaan_limas(luas_alas, luas_sisi_tegak))
    elif pilihan == 5:
        luas_alas = float(input("Masukkan nilai luas alas prisma: "))
        keliling_alas = float(input("Masukkan nilai keliling alas prisma: "))
        tinggi = float(input("Masukkan nilai tinggi prisma: "))
        print("Luas Permukaan Prisma:", luas_permukaan_prisma(luas_alas, keliling_alas, tinggi))
    else:
        print("Pilihan tidak valid.")

def main():
    while True:
        print("\nPilih jenis perhitungan:")
        print("1. Operasi Aritmatika")
        print("2. Luas Bangun Datar")
        print("3. Luas Bangun Ruang")
        print("4. Keluar")
        
        pilihan = int(input("\nMasukkan pilihan (1-4): "))
        
        if pilihan == 1:
            hitungan_aritmatika()
        elif pilihan == 2:
            hitungan_bangun_datar()
        elif pilihan == 3:
            hitungan_bangun_ruang()
        elif pilihan == 4:
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
