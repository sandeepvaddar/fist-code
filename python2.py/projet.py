print("WelCome to the Game")

playing = input("Do you want to play?  ")

if playing.lower() != "yes":
    quit()

print("Okay!.... Let's statr the Game!:)")
score = 0

answer = input("What does CPU stands for?  ")
if answer == "Central processing unit":
    print("correct")
else:
    print("Incorrect")
    score += 1

answer = input("What does RPU statnd for?   ")
if answer == "Graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM statnd for?   ")
if answer == "Random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
    
answer = input("What does PSU statnd for?   ")
if answer == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " Question correct!")
print("You got " + str((score / 4) * 100) + "%")