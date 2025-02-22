print('''The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.\nThe hat decides which of the four "Houses" each first-year student goes to :

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin \n''')

G = 0
R = 0
H = 0
S = 0

print('-'*20)
print("Choose Question 1 :")
print("1. Dawn")
print("2. Dusk \n")
Q1 = int(input("Do you like Dawn or Dusk? "))

if Q1 == 1:
  G += 1
  print(f"\n Gryffindor = {G}\n")
elif Q1 == 2:
  H += 1 
  S += 1
  print(f"\n Hufflepuff = {H} and Slytherin = {S}\n")
else : 
  print("\n Wrong Input!\n")

print('-'*20)
print("Choose Question 2 :")
print('''
1. The Good
2. The Great
3. The Wise
4. The Bold \n''')

Q2 = int(input("When I'm dead, I want people to remember me as : "))

if Q2 == 1:
  H += 2
  print(f"\n Hufflepuff = {H} \n")
elif Q2 == 2:
  S += 2
  print(f"\n Slytherin = {S} \n")
elif Q2 == 3:
  R += 2
  print(f"\n Ravenclaw = {R} \n")
elif Q2 == 4 :
  G += 2
  print(f"\n Gryffindor = {G} \n")
else :
  print(" \n Wrong Input! \n")

print('-'*20)
print("Choose Question 3 :")
print('''
1. The Violin
2. The Trumpet
3. The Piano
4. The Drum \n''')

Q3 = int(input("Which kind of instrument most pleases your ear?"))

if Q3 == 1:
  S += 4
  print(f"\n Slytherin = {S} \n")
elif Q3 == 2 :
  H += 4
  print(f"\n Hufflepuff = {H} \n")
elif Q3 == 3 :
  R += 4
  print(f"\n Ravenclaw = {R} \n")
elif Q3 == 4 :
  G += 4
  print(f"\n Gryffindor = {G} \n")
else :
  print("Wrong Input")

print('-'*20)
print("Total Score :")
print(f'''
1. Gryffindor = {G}
2. Ravenclaw = {R}
3. Hufflepuff = {H}
4. Slytherin = {S}

''')
print('-'*20)
total = G + R + H + S
print(f"Total Score Do You Get -->> {total}")
