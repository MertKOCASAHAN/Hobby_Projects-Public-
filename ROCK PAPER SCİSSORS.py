import random
def oyun():
   main = ("taş", "kağıt", "makas")
   x = input("Taş/Kağıt/Makas - seçim yap:").lower()
   y = random.choice(main)
   print(f"Bilgisayar: {y}")
   if x == y:
       print("*******")
       print("BERABERE !")
       print("*******")
   elif x == "taş" and y == "makas":
       print("*******")
       print("KAZANDINIZ!")
       print("*******")
   elif x == "kağıt" and y == "taş":
       print("*******")
       print("KAZANDINIZ!")
       print("*******")
   elif x == "makas" and y == "kağıt":
       print("*******")
       print("KAZANDINIZ!")
       print("*******")
   else:
       print("KAYBETTİNİZ !")
oyun()

print("*******")
while True:
   xy =input("TEKRAR OYNAMAK İSTER MİSİNİZ?!(EVET/HAYIR):").lower()
   print("*******")
   if xy == "evet":
    oyun()
   else:
    print("GÖRÜŞÜRÜZ !")
    input()


