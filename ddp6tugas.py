#Print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553. Pakai perulangan while. 
print ("No. 1")
index = 0
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]

while index < len(numbers):
    if numbers[index] % 2 != 0:
        print(numbers [index], end=" ")#ditengah kutip dalam end="" harus diberikan spasi
    if numbers [index] == 553:
        break
    index +=1
print("")

print()
#Buatlah output dari menggunakan bahasa pemprograman python dengan: 
#1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = ....
print("No. 2")
JumlahTotalGanjil = 0
BilanganGanjil = 1

while BilanganGanjil <= 19:
    JumlahTotalGanjil += BilanganGanjil
    BilanganGanjil += 2

print("1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 =", JumlahTotalGanjil)
print("")

print()
#Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini
#*
#**
#***
#****
#Dan seterusnya sejumlah baris yang diinputkan. Gunakan for loop dengan range
print("No. 3")
bintang = "*"
JumlahBintang = int(input("Masukkan jumlah bintang: "))
for i in range(1, JumlahBintang + 1):
    print(bintang * i)

