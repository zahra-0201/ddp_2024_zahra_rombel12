from animal import Animal

class Snake(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bisa, bentukkepala):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bisa = bisa
        self.bentukkepala = bentukkepala

    def info_snake(self):
        super().info_animal()
        print(f"Jenis Bisa Ular \t:", self.bisa,
              "\nBentuk Kepalanya \t:", self.bentukkepala)
        
print()
snake = Snake('Ular Kobra', 'Daging', 'Hutan', 'Bertelur', 'Berbisa', 'Segitiga dan lebar')
print("==================================")
print("Info Ular Kobra")
snake.info_snake()

print()
snake = Snake('Ular Sanca', 'Daging', 'Hutan hujan tropis', 'Bertelur', 'Tidak Berbisa', 'Bulat dan besar')
print("==================================")
print("Info Ular Sanca")
snake.info_snake()

print()
snake = Snake('Ular Weling', 'Daging', 'Sungai/rawa', 'Bertelur', 'Berbisa', 'Kecil dan lonjong')
print("==================================")
print("Info Ular Weling")
snake.info_snake()
