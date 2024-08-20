import random
name = " "
question = " "



random_number = random.randint(1,15)
answer = "Magic 8-Ball's answer:" 






prediction = ""

if random_number == 1:
  prediction = "Yes - definitely"
elif random_number == 2:
  prediction = "It is decidely"
elif random_number == 3:
  prediction = "Without a doubt"
elif random_number == 4:
  prediction = "Reply hazy, try again"
elif random_number == 5:
  prediction = "Ask again later"
elif random_number == 6:
  prediction = "Better not tell you"
elif random_number == 7:
  prediction = "My sources say no"
elif random_number == 8:
  prediction = "Outlook not so good"
elif random_number == 9:
  prediction = "Very doubtful"
elif random_number ==10:
  prediction = "Certainly yes"
elif random_number == 11:
  prediction = "I have bad mood"
elif random_number == 12:
  prediction = "I don't believe on it"
elif random_number == 13:
  prediction = "No way"
elif random_number == 14:
  prediction = "Nice try"
elif random_number == 15:
  prediction = "Too late"
else:
  print("Erorr")

if name == " ":
  print("Question:", question)
else:
  print(name, "asks:" , question)




if question == " ":
  print("The question is an empty string")
else:
  print(answer, prediction)




