import random

print("\nWelcome to the Best Skateboard Quiz.\n Please enter either A, B, and C to answer the questions.\n Enjoy!\n\n")



score = x
x = 0


 # Question 1
answer_1 = input("Who was the star of Pro Skater 2?\na) Tony Hawk\nb) Bob Burnquist\nc) Kareem Campbell\n")

if answer_1.lower() == "a":
    print("Correct\n")
    x + 1 
else:
    print("Wrong Answer\n")

# Question 2
answer_2 = input("What was the biggest stair set ever ollied?\na) El Toro\nb) UC Davis\nc) Lyon 25\n")

if answer_2.lower() == "c":
    print("Correct\n")
    x + 1
else:
    print("Wrong Anwser\n")

#Question 3
answer_3 = input("Who ollied the biggest stair set?\na) Nyjah Huston\nb) Tony Hawk\nc) Aaron Homoki\n")

if answer_3.lower() == "c":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 4
answer_4 = input("Who was the Skate School Teacher in Skate 3?\na) Coach Fred\nb) Coach Frank\nc) Coach Franklin\n")

if answer_4.lower() == "b":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 5
answer_5 = input("Who was the 2021 Olympic Skateboarding Champion?\na) Reef Owen\nb) Nyjah Huston\nc) Yuto Horigome\n") 

if answer_5.lower() == "c":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 6
answer_6 = input("Who is the 'best' skateboarder in NZ?\na) Izy Mutu\nb) Bowman Hansen\nc) Theo Clarke\n")

if answer_6.lower() == "b":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 7
answer_7 = input("Where was the 2019 X games held?\na) Minneaplois\nb) Los Angeles\nc) Miami\n")
if answer_7.lower() == "b":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 8 
answer_8 = input("What was skateboarding originally called?\na) Sidewalk Surfing\nb) Street Surfing\nc) Street Waving\n")
if answer_8.lower() == "a":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 9
answer_9 = input("How many skateboard decks are made each month?\na) 100,000\nb) 1,000,000\nc) 500,000\n")
if answer_9.lower() == "c":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")

# Question 10
answer_10 = input("What part of the body is injured the most in skateboarding?\na) Foot\nb) Wrists\nc) Head\n")
if answer_10.lower() == "b":
    print("Correct\n")
    x + 1
else:
    print("Wrong Answer\n")


print(score)


    