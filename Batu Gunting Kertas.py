import random

# Menerima Pilihan dari User Antara Batu, Kertas, Gunting
def get_choices():
  player_choice = input("Masukkan pilihanmu (batu, kertas, gunting): ")
  options = ["batu", "kertas", "gunting"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print (f"Kamu memilih {player}, Komputer memilih {computer}")
  if player == computer:
    return "Imbang coy!"
  elif player == "batu":
    if computer == "gunting":
      return "Batu menghancurkan gunting, kamu menang!"
    else:
      return "Batu dilapisi kertas, kamu kalah!"
  elif player == "kertas":
    if computer == "batu":
      return "Kertas melapisi batu, kamu menang!"
    else:
      return "Kertas dipotong gunting, kamu kalah!"
  elif player == "gunting":
    if computer == "kertas":
      return "Gunting memotong kertas, kamu menang!"
    else:
      return "Gunting dihancurkan batu, kamu kalah!"
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)