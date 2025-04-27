import random
print("Welcome to The AMAZING Climate HERO QUIZ!!!")
name = str(input("What is Your UserName: "))
print(f"Good Luck, {name}!")

score = 0
Lives = 3

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
    }
]