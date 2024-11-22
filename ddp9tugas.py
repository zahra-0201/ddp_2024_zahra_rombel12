print("NOMOR 1")
def celciusFahrenheit(celcius) :
    konversi=(celcius*9/5)+32
    return konversi
print(celciusFahrenheit(0)) #output: 32
print(celciusFahrenheit(100)) #output: 212

print()
print("NOMOR 2")
def ganjilGenap (bilangan) :
    penentu = bilangan % 2 == 0
    return penentu
print(ganjilGenap(4)) #output: True
print(ganjilGenap(7)) #output: False

print()
print("NOMOR 3")
def nilai(keterangan) :
    if keterangan >= 80:
        print("Lulus")
    elif keterangan <= 60:
        print("Gagal")
nilai(80) #output: Lulus
nilai(60) #output: Gagal

print()
print("NOMOR 4")
def bilGanjil(angka) :
    return[i for i in range(1, angka, 2)]
print(bilGanjil(20)) #output: 1,3,5,7,9,11,13,15,17,19