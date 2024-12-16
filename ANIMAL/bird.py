from animal import Animal

class Bird(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        super().info_animal()
        print(f"Warna\t\t\t:", self.warna,
              "\nJenis Paruh\t\t:", self.paruh)

print()      
bird = Bird('Burung Elang', 'Daging', 'Pegunungan', 'Bertelur', 'Cokelat tua', 'Melengkung dan tajam')
print("==================================")
print('Info Burung Elang')
bird.info_bird()

print()
bird = Bird('Burung Merak', 'Biji-bijian', 'Hutan tropis', 'Bertelur', 'Biru, hijau dan emas', 'Pendek')
print("==================================")
print('Info Burung Merak')
bird.info_bird()

print()
bird = Bird('Burung Beo', 'Biji-bijian', 'Hutan Tropis dan subtropis', 'Bertelur','Hijau, merah, biru, kuning', 'Bengkok dan kuat')
print("==================================")
print('Info Burung Beo')
bird.info_bird()