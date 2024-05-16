# Write code below 💖

import random
import time

class Pokemon:
  def __init__(self, id, name, type, description):
    self.id = id
    self.name = name
    self.type = type
    self.description = description

  def display_details(self):
    print(f"ID: {self.id}\n"
    f"Name: {self.name}\n"
    f"Type: {self.type}\n"
    f"Description: {self.description}")

class PokeMoves:
  def __init__(self, move1, move2):
    self.move1 = move1
    self.move2 = move2

  def display_move(self):
    print(f"""
      1) {self.move1}\n
      2) {self.move2}\n
      """)

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)  # adjust this value for the speed of the animation
  
  # def pokemon_stats(self):


bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass', 'The more sunlight Ivysaur bathes in, the more strength wells up within it, allowing the bud on its back to grow larger.')
charmander = Pokemon(2, 'Charmander', 'Fire', 'The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.')
squirtle = Pokemon(3, 'Squirtle', 'Water', 'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.')
mew = Pokemon(151, 'Mew', 'Pyschic', 'When viewed through a microscope, this Pokémon’s short, fine, delicate hair can be seen.')

bulb_move = PokeMoves('Vine Whip', 'Tackle')
char_move = PokeMoves('Ember', 'Scratch')
squi_move = PokeMoves('Water Gun', 'Bite')

effective = [
  'Vine Whip',
  'Ember'
  'Water Gun'
]

ascii_pokemon = """                                                                           
,------.        ,--.              ,-----.            ,--.    ,--.  ,--.        
|  .--. ' ,---. |  |,-. ,---.     |  |) /_  ,--,--.,-'  '-.,-'  '-.|  | ,---.  
|  '--' || .-. ||     /| .-. :    |  .-.  \' ,-.  |'-.  .-''-.  .-'|  || .-. : 
|  | --' ' '-' '|  \  \\   --.    |  '--' /\ '-'  |  |  |    |  |  |  |\   --. 
`--'      `---' `--'`--'`----'    `------'  `--`--'  `--'    `--'  `--' `----'                                                                                                                                                                                                                                                  
"""
print(ascii_pokemon)
print("""
  1) Bulbasaur 🌿,\n
  2) Charmander 🔥,\n
  3) Squirtle 💧
  """)

ascii_bulb = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀
"""
ascii_char = """
⠀⠀⠀⠀⠀⠀⠀⡀⠠⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠈⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣜⠃⠀⠀⠀⢘⢳⢆⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠔⠉⠀⠀⠀⠀⣜⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⡀⠀⠀⠀⠀⠈⠉⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀
⠀⡤⢄⣳⣦⠤⠤⠤⠄⣄⡲⡪⠀⡇⠀⢀⡀⢤⠀⠀⠀⢠⠒⢋⠤⠀
⠘⢝⠁⠈⠙⠷⠒⠒⠾⠓⢎⠀⠀⠁⠉⠁⠈⢛⠆⠀⠀⠈⢷⣿⠀⣆
⠀⠀⠑⢄⠀⡘⠀⠀⠀⠀⠀⠣⡀⠀⠀⣀⠔⠁⠀⠀⠀⢀⠃⠹⢷⡄
⠀⠀⠀⠀⠑⡇⠀⠀⠀⠀⠀⠀⢡⠀⠈⡄⠀⠀⠀⠀⠀⠈⠣⢤⡼⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡆⠀⠰⠀⠀⠀⠀⠀⠀⠀⡌⡇⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⢀⠌⢠⠃⠀
⠀⠀⠀⠀⡐⠉⠣⡀⠀⠀⠀⠀⢀⠃⠂⠐⡎⠁⠒⠂⠈⠀⣠⠏⠀⠀
⠀⠀⠀⠀⡀⠀⠀⠈⠒⡤⠀⠠⠊⠀⠀⠀⡠⣀⣀⠠⢄⠾⠃⠀⠀⠀
⠀⠀⣀⡤⠚⠲⠀⠀⠸⡁⠀⢘⠄⠀⠀⣠⠋⠁⠀⠉⠁⠀⠀⠀⠀⠀
⠀⠈⠛⡊⠂⠀⠀⠒⠂⠁⠀⠘⢖⣔⣶⡲⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
ascii_squir = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠐⠒⠒⠂⠠⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⡠⢠⠂⠀⠀⠀⠡⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⢰⣷⣾⠀⠀⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠜⢨⠢⠔⡀⠀⠠⠘⠛⠛⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⢀⣀⣀⠀⠀⠀⠰⠀⠀⠀⠀⠡⡀⠀⠈⠀⠒⠂⠄⡀⢀⠀⡀⠀
⠀⡴⠊⠀⠀⠀⠉⢆⠀⡔⢣⠀⠀⠀⠀⠐⡤⣀⠀⠀⠀⠀⠀⣀⠄⠀⠀
⢸⠀⠀⠀⢠⠀⠀⠈⣼⠀⠀⠣⠀⠀⠀⡰⡀⠀⠉⠀⠀⠰⠉⠀⠁⠠⢄
⢰⠀⠀⠀⠀⠇⠀⢀⢿⠀⢀⠇⡐⠀⠈⠀⠈⠐⠠⠤⠤⠤⠀⠀⠀⠀⢨
⠀⢓⠤⠤⠊⠀⠀⢸⠀⠣⠀⡰⠁⠀⠀⡀⠀⠀⠀⠸⠀⢰⠁⠐⠂⠈⠁
⠀⠀⠑⢀⠀⠀⠀⠈⣄⠖⠉⠑⢄⠠⠊⠀⠢⢄⣠⣃⣀⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⠠⢀⣀⠎⠀⠀⠀⠈⡄⠀⠀⠀⢠⢃⠠⠃⠐⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⢀⠯⠉⠤⢴⡃⠁⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⡁⠀⠀⠀⠠⠂⠀⠀⠀⠀⠑⢄⠀⠀⢀⠲⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠒⠑⠔⠁⠀⠀⠀⠀⠀⠀⠀⠁⠉⠀⠀⠀⠀⠀⠀
"""
ascii_battle = """
                                             
,-----.            ,--.    ,--.  ,--.        
|  |) /_  ,--,--.,-'  '-.,-'  '-.|  | ,---.  
|  .-.  \' ,-.  |'-.  .-''-.  .-'|  || .-. : 
|  '--' /\ '-'  |  |  |    |  |  |  |\   --. 
`------'  `--`--'  `--'    `--'  `--' `----' 
"""
ascii_mew = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠿⢟⣛⣩⣤⣶⣶⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⠿⠸⣿⣿⣿⣿⣿⣿⡿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠞⠉⠀⠀⠀⣿⠋⠻⣿⣿⣿⠀⣦⣿⠏⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀
⢠⠏⠀⠀⠀⠀⠀⠻⣤⣷⣿⣿⣿⣶⢟⣁⣒⣒⡋⠉⠉⠁⠀⠀⠀⠈⠉⡧
⢻⡀⠀⠀⠀⠀⠀⣀⡤⠌⢙⣛⣛⣵⣿⣿⡛⠛⠿⠃⠀⠀⠀⠀⠀⢀⡜⠁
⠀⠉⠙⠒⠒⠛⠉⠁⠀⠸⠛⠉⠉⣿⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⣿⣿⣷⡄⠞⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⡻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣑⡙⠻⠿⠿⠈⠙⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⡀⠀⠀⠀⠀⢹⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠸⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⡿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⠀⠀⠀⠀
"""

# CHOOSE POKEMON ==============================================================================
poke_name = ''

pl_pokemon = int(input("Choose a starter: "))


while pl_pokemon != 1 and pl_pokemon != 2 and pl_pokemon !=3:
  print("Pokemon not Found!\n")
  pl_pokemon = int(input("Choose a starter: "))
       
if pl_pokemon == 1:
  print("\nYou choose Bulbasaur!\n" + ascii_bulb)
  bulbasaur.display_details()
  poke_name = 'Bulbasaur'
elif pl_pokemon == 2:
  animate_text("\nYou choose Charmander!\n" + ascii_char)
  charmander.display_details()
  poke_name = 'Charmander'
elif pl_pokemon == 3:
  animate_text("\nYou choose Squirtle!\n" + ascii_squir)
  squirtle.display_details()
  poke_name = 'Squirtle'

# BATTLE =======================================================================================
animate_text(ascii_battle + """\nTrainer X wants to battle!\n
Trainer uses mew!""")
print(ascii_mew)
mew.display_details()

pokemon_user = 100
pokemon_cpu = 100

while pokemon_cpu > 0 and pokemon_user > 0:
    print("""\nMOVES\n
      1) Attack 👊,\n
      2) Run 🏃,\n
      """)
    try:
      pl_option = int(input("Choose what to do: "))
    except ValueError:
      print("INVALID Input")
    
    while pl_option != 1 and pl_option != 2:
      print("Move NOT found!\n")
      pl_option = int(input("Choose what to do next: "))

    if pl_option == 1:
      print(f"\n{poke_name} MOVES\n")


      if pl_pokemon == 1:
        bulb_move.display_move()
        try:
          pl_move = int(input("Choose a move to use: "))
        except ValueError:
          print("INVALID Input!")
        while pl_move != 1 and pl_move != 2:
          print(f"Move NOT found!")
          pl_move = int(input("Choose a move to use: "))  
        if pl_move == 1:
          print(f"{poke_name} use Vine Whip 🌿")
          poke_atk = random.randint(20, 30)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")
        else:
          print(f"{poke_name} use Tackle")
          poke_atk = random.randint(10, 20)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")
      elif pl_pokemon == 2:
        char_move.display_move()
        pl_move = int(input("Choose move to use: "))
        while pl_move != 1 and pl_move != 2:
          print(f"Move NOT found!")
          pl_move = int(input("Choose a move to use: \n")) 
        if pl_move == 1:
          print(f"{poke_name} use Ember 🔥")
          poke_atk = random.randint(20, 30)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")
        else:
          print(f"{poke_name} use Scratch")
          poke_atk = random.randint(10, 20)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")
      elif pl_pokemon == 3:
        squi_move.display_move()
        pl_move = int(input("Choose move to use: "))
        while pl_move != 1 and pl_move != 2:
          print(f"Move NOT found!")
          pl_move = int(input("Choose a move to use: \n")) 
        if pl_move == 1:
          print(f"{poke_name} use Water Gun 💧")
          poke_atk = random.randint(20, 30)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")
        else:
          print(f"{poke_name} use Bite")
          poke_atk = random.randint(10, 20)
          pokemon_cpu -= poke_atk
          print(f"\nMew HP: {pokemon_cpu}")
          poke_uatk = random.randint(10, 40)
          pokemon_user -= poke_uatk
          print(f"{poke_name} HP: {pokemon_user}")

    #   poke_atk = random.randint(20, 30)
    #   pokemon_cpu -= poke_atk
    #   print(f"\nMew HP: {pokemon_cpu}")
    #   poke_uatk = random.randint(50, 100)
    #   pokemon_user -= poke_uatk
    #   print(f"{poke_name} HP: {pokemon_user}")
    elif pl_option == 2:
      print("\nAre u stoooppiiidd 💩")
      poke_uatk = random.randint(99, 100)
      pokemon_user -= poke_uatk
      print(f"\nMew HP: {pokemon_cpu}")
      print(f"{poke_name} HP: {pokemon_user}")

if pokemon_cpu == 0 or pokemon_cpu < pokemon_user:
  print("Lucky B**tard!")
elif pokemon_cpu == 0 and pokemon_user == 0:
  print("ITSS A TTIIEEE")
elif pokemon_user == 0 or pokemon_cpu > pokemon_user:
  print("\nFAAKINGG NAB CANTT WIN A POKEMON FYTT!")

print("""\nCONTINUE?\n
      1) Yes 👍\n
      2) No 👎\n
      """)
continue_input = int(input("Do you wish to continue: "))

if continue_input == 1:
  print("Next Chapter in PROGRESS 🚧")
else:
  print("Thanks for playing ❤️️")