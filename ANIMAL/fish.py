from animal import Animal

class Fish(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, pernapasan, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.pernapasan = pernapasan
        self.habitat = habitat

    def info_fish(self):
        super().info_animal()
        print(f"Bernapas menggunakan \t:", self.pernapasan,
              "\nHabitat di \t\t:", self.habitat)
        
print()
fish = Fish ('Hiu', 'Daging', 'Laut', 'Bertelur dan Melahirkan', 'Insang', 'Samudra Tropis dan Subtropis')
print("==================================")
print('Info Ikan Hiu')
fish.info_fish()

print()
fish = Fish('Ikan Koi', 'Pelet Ikan, Sayuran', 'Air Tawar', 'Bertelur', 'Insang', 'Air Tawar, seperti danau kecil')
print("==================================")
print('Info Ikan Koi')
fish.info_fish()

print()
fish = Fish('Ikan Arwana', 'Ikan Kecil', 'Sungai besar atau rawa- rawa', 'Bertelur dan melahirkan', 'Insang', 'Daerah Tropis, sungai arus tenang')
print("==================================")
print('Info Ikan Arwana')
fish.info_fish()