#memanggil file gempa dan import semua method/fungsi
from gempa import *
#membuat objek gempa dengan argumen
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)
#informasi gempa 
print("===Info Gempa===")
print()
gempa1.dampak()
print()

print()
gempa2.dampak()

print()
gempa3.dampak()

print()
gempa4.dampak()

print()
gempa5.dampak()