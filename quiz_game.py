print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("OK!  Let's play :) ")
score = 0

answer = input("What does PC stand for? ")
if answer.lower() == "personal computer":
  print("Correct!")
  score +=1
else:
  print("Wrong answer :(")

answer = input("The two most common operating systems are Mac and... ")
if answer.lower() == "windows":
  print("Correct!")
  score +=1
else:
  print("Wrong answer :(")

answer = input("What does AWS stand for? ")
if answer.lower() == "amazon web services":
  print("Correct!")
  score +=1
else:
  print("Wrong answer :(")


answer = input("I am a small mammal but I am also used to click around your computer! I am a... ")
if answer.lower() == "mouse":
  print("Correct!")
  score +=1
else:
  print("Wrong answer :(")

print("You got " + str(score) + " questions correct!")
print("That means you got " +str((score / 4) * 100) + "%. of the questions correct.")