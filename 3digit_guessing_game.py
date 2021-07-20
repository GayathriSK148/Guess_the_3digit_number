#generate a random 3 digit number
import random
def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

#function for taking a guess as an input
def get_guess():
    return list(input("What is your guess? "))

# Generating the hint:
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues=[]
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')

    if clues == []:
        return ['Nope']
    else:
        return clues

#create the game logic
print("Welcome Code Breaker!")
secret_code = generate_code()
clue_report=[]
while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clues(secret_code, guess)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
