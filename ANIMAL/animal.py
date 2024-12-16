#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#buat minimal 3 class child (burung, ikanular, dll) setiap class child itu memiliki 2 properti dan method  
#buat minimal 3 objek dari masing masing class child

class Animal:
    #konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak): #self utk menginisiasi
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    #method informasi
    def info_animal(self):
        print("Nama Hewan\t\t:" , self.nama, 
              "\nMakanan\t\t\t:" , self.makanan,
              "\nHidup di\t\t:" , self.hidup,
              "\nBerkembang biak\t\t:", self.berkembang_biak) #\t utk tab, \n utk enter
        
# #objek
# kucing = Animal('kucing', 'daging', 'hidup di darat', 'melahirkan')
# kucing.info_animal()
# ctrl slash utk mmbuat komen
