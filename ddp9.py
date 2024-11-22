#pendeklarasian fungsi 
def hello() :
    print("hello ini adalah fungsi hello")
    print("selamat datang di nurul fikri")
hello() #memanggil fungsi hello
hello() #fungsi bisa dipanggil berkali kali

def nama(nama) :
    print("zahra " + nama)
nama("hasna")
nama("keyla")

def cetak(kata) :
    print(kata)
cetak("halo")

def biodata(nama = "jj", alamat = "depok", umur = 18) : #semua argumen harus diisi
#umur = 18 (default)
    cetak("nama saya adalah " + nama)
    cetak("alamat saya adalah " + alamat)
    cetak("umur saya adalah " + str(umur))
biodata("zahra", "depok", 18) 
biodata()

def perkalian(a, b) : 
    print(a * b)
perkalian(3, 4)

def luaspersegi (a) :
    print(a * a)
luaspersegi(2)

#arbitary menambahkan bintang sblm di argumen
#return pengembalian nilai
def bilangan1(x) :
    return x*4

def bilangan2(y) :
    return y*y

print(bilangan1(2) + bilangan2(3))