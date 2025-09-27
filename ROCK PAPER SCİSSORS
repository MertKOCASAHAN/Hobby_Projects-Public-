

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
   zxy = input("Tekrar oynamak ister misiniz? (evet/hayır:").lower()
   while zxy == "evet":
       oyun()
def game():
   main = ("rock", "paper", "scissors")
   x = input("Rock/Paper/Scissors - make your choice:").lower()
   y = random.choice(main)
   print(f"Computer: {y}")
   if x == y:
       print("*******")
       print("DRAW !")
       print("*******")
   elif x == "rock" and y == "scissors":
       print("*******")
       print("YOU WIN !")
       print("*******")
   elif x == "paper" and y == "rock":
       print("*******")
       print("YOU WIN!")
       print("*******")
   elif x == "scissors" and y == "paper":
       print("*******")
       print("YOU WIN!")
       print("*******")
   else:
       print("*******")
       print("YOU LOSE !")
       print("*******")
   zxy = input(" Do you want to play again? (yes/no):").lower()
   while zxy == "yes":
      game()

def spiel():
   main = ("stein", "papier", "schere")
   print("*******")
   x = input("Stein/Papier/Schere - deine Wahl:").lower()
   y = random.choice(main)
   print(f"Computer: {y}")
   if x == y:
       print("*******")
       print("UNENTSCHIEDEN !")
       print("*******")
   elif x == "taş" and y == "makas":
       print("*******")
       print("DU HAST GEWONNEN !")
       print("*******")
   elif x == "kağıt" and y == "taş":
       print("*******")
       print("DU HAST GEWONNEN !")
       print("*******")
   elif x == "makas" and y == "kağıt":
       print("*******")
       print("DU HAST GEWONNEN !")
       print("*******")
   else:
       print("*******")
       print("DU HAST VERLOREN !")
       print("*******")
   zxy = input("Noch einmal spielen? (ja/nein):").lower()
   while zxy == "ja":
       spiel()

xyz = input("Dil ? / Language ? / Sprache ? : tr = Türkçe, en = English, de = Deutsch:").lower()
if xyz == "tr":
    oyun()
if xyz == "en":
    game()
if xyz == "de":
    spiel()
