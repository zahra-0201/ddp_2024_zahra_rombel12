mylist = [1, 2, 3, 4, 5]
print(mylist[0]) #akan mencetak angka 1
print(mylist[3]) #akan mencetak angka 4
mylist.append(6) #menambahkan value baru
mylist.insert(2,7) #sisipkan value 7 disamping 2
print(mylist)

myList = [1, 2, 3, 4]
myList.insert(0,9)
print(myList)

MyList = [1, 2, 3, 4]
MypopList = MyList.pop(3) #menyimpan sebuah value ke 
print(myList)

mytuple = (1, 2, 3, 4)
print(mytuple[1])

mydictionary = {
    'nama' : 'zahra',
    'nim' : '0110224193',
    'rombel' : 'TI12'
}
print(mydictionary['nama'])
print(type('nim'))


x = range(1,10)
for n in x:
    print(n)

malist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(malist) 
malist.append('hello')
malist.append(100)
print(malist)
mapoplist = malist.pop(4)
print(malist)
print(mapoplist)

absen = {
    'jeje' : 'depok', 'hasna' : 'bogor', 'keyla' : 'kelapa dua', 'bella' : 'bogor'
}
print(absen['jeje'])

warnalampu = input("Masukkan warna lampu: ")
match warnalampu:
    case "merah" | "Merah" | "MERAH" :
        print("Berhenti")
    case "kuning" | "Kuning" | "KUNING" :
        print("Hati-hati")
    case "hijau" | "Hijau" | "HIJAU" :
        print("Jalan")
    case _:
        print("Warna tidak dikenali")