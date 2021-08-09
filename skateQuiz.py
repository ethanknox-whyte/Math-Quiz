import random

print("\nWelcome to the Best Skateboard Quiz.\n Please enter either A, B, and C to answer the questions.\n Enjoy!\n\n")

def questions (question, answers, correct_answer: str) -> str:
     # a function for creating the questions, checking the answer the input and verifying the correct answer
    while True:
        print(question)
        print(answers)
        reponse = input("Please enter answer: \n ")
        if response == correct_answer:
            print("Good job!")
            return True
        else:
            print("Whoops, that's wrong \n")
            return False

score = 0


# Questions 
question_1 = ('Who was the star of Pro Skater 2?', ['Tony Hawk, Bob Burnquist, Kareem Campbell'], 'Tony Hawk')
question_2 = ('What was the biggest stair set ever ollied?', ['El Toro, UC Davis, Lyon 25'], 'Tony Hawnk')
question_3 = ('Who ollied the biggest stair set?', ['Nyjah Huston, Tony Hawk, Aaron Homoki'], 'Aaron Homoki')
question_4 = ('Who was the Skate School Teacher in Skate 3?', ['Coach Fred, Coach Frank, Coach Franklin'], 'Coach Frank')
question_5 = ('Who was the 2021 Olympic Skateboarding Champion?', ['Reef Owen, Nyjah Huston, Yuto Horigome'], 'Yuto Horigome') 
question_6 = ('Who is the best skateboarder in NZ?', ['Izy Mutu, Bowman Hansen, Theo Clarke'], 'Bowman Hansen')
question_7 = ('Where was the 2019 X games held?', ['Minneaplois, Los Angeles, Miami'], 'Minneaplois')
question_8 = ('What was skateboarding originally called?', ['Sidewalk Surfing, Street Surfing, Street Waving'], 'Sidewalk Surfing')
question_9 = ('How many skateboard decks are made each month?', ['100,000, 1,000,000, 500,000'], '500,000')
question_10 = ('What part of the body is injured the most in skateboarding?', ['Foot, Wrists, Head'], 'Wrists')

questions(question_1[0],question_1[1],question_1[2])


#TODO
# don't let the user input anything other than a b c
# Lots of repeated code, use a loop
# display the score in a meaningful f string