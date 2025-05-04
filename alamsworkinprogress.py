import random


questions = [
    {
        "question": "What is the main cause of Climate Change?",
        "options": ["A. Volcanoes", "B. Deforestation", "C. Burning fossil fuels", "D. Funny people"],
        "answer": "C"
        


    },
    {
        "question": "Which gas is most responsible for global warming?",
        "options":["A. Oxygen", "B. Carbon Dioxide", "C. Jinn", "D. Hydrogen"],
        "answer": "B"

    },
    {
        "question": "Which human activity greatly contributes to Climate Change?",
        "options": ["A. Farming", "B. Fishing", "C. Burning fossil fuels", "D. Recycling"],
        "answer": "C"
    },
    {
        "question": "What is the main cause of rising sea-levels?",
        "options": ["A. Ocean pollution", "B. Melting ice caps", "C. Overfishing", "D. Earthquakes"],
        "answer": "B"

    }
]

def start_quiz():
    name = input("WELCOME to the aMaZiNg Climate Change quiz!! What is your Name: ")
    print(f"Hello, {name}! Lets begin.\n")

score = 0
lives = 3

random.shuffle(questions)

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    while True:
        answer = input("Enter an answer. A B C or D: ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print(f"{answer}, was an invalid input, ENTER A CORRECT INPUT")

    if answer == q["answer"]:
        print("That is the correct answer :)\n")
        score += 1
    else:
        print(f"INCORRECT answer !! The correct answer was {q['answer']}.\n")
        lives -= 1

    print(f"lives left: {'❤️' * lives}\n")

    if lives == 0:
        print("Game Over. Your out of lives!\n")
        break

print(f"Quiz finished! Your final score: {score}/4\n")

   #personlized feedback

if score == 4:
    print("Excellent work!!!")
if score == 3:
    print("Good job, you know a lot!!")
elif score >= 2:
    print("Life can be tough sometimes, learn from your mistakes")
else:
    print("This is not your field")

retry = input("\nWould you like to retake this quiz? (yes/no): ")
if retry == "yes":
    start_quiz()
else:
    print("Thank You for playing! And take care of our lovely environment")