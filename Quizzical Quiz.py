# Quizzical Quiz
import random

'''---------------------------'''
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    random.shuffle(ques)
    for que in ques:
        print("-------------------------")
        print(que.get("q"))
        for i in que.get("options"):
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(que.get("a"), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


'''-------------------------'''
def check_answer(answer, guess):

    if answer == guess:
        print("⭐CORRECT!⭐")
        return 1
    else:
        print("🙁WRONG!🙁")
        return 0


'''-------------------------'''
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in ques:
        print(i.get("a"), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(ques)) * 100)
    print("Your score is: " + str(score) + "%")


'''-------------------------'''
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


'''-------------------------'''


# questions = {
#     ""Virtual Keyboards protect the computer against ?": "D",
#     Which of the following food articles contains only one of the five constituents 
#       of die, viz. fats, carbohydrates, proteins, mineral salts, and vitamins?: "D",
#     "Which one of the following substances is obtained by the fractionation of human blood? ": "B",
#     "The brain of a normal human adult weighs about:- ?": "C",
# }

# options = [
#     ["A. Password theft", "B. Trojan programs", "C. Spyware ", "D. ALL OF THE ABOVE "],
#     ["A. Bread", "B. Mango", "C.Milk", "D. Sugar"],
#     ["A. Antivenom serum", "B. Gamma glodulin", "C. Polio vaccine", "D. Diphtheria antitoxin"],
#     ["A. 1 lb", "B. 2 lb", "C. 3 lb", "D. 4 lb"],
# ]

ques = [
    {
        "q": "Virtual Keyboards protect the computer against ❓ ",
        "a": "D",
        "options": [
            "A. Password theft", "B. Trojan programs", "C. Spyware ", "D. ALL OF THE ABOVE "],
    },
    
    {
        "q": ''' Which of the following food articles contains only one of the five constituents 
        of die, viz. fats, carbohydrates, proteins, mineral salts, and vitamins? ❓ ''',
        "a": "D",
        "options": ["A. Bread", "B. Mango", "C.Milk", "D. Sugar"],
    },
    {
        "q": " Which one of the following substances is obtained by the fractionation of human blood? ❓ ",
        "a": "B",
        "options": ["A. Antivenom serum", "B. Gamma glodulin", "C. Polio vaccine", "D. Diphtheria antitoxin"],
    },
    {
        "q": "The brain of a normal human adult weighs about:- ❓",
        "a": "C",
        "options": ["A. 1 lb", "B. 2 lb", "C. 3 lb", "D. 4 lb"],
    },
    
    {
        "q": "The electric charge is stored in a device called ❓ ",
        "a": "B",
        "options": ["A. Inductor", "B. Capacitor", "C. Resistor", "D. Transformer"],
    },
    
    {
        "q": "If the speed of rotation of the earth increases, the weight of the body ❓ ",
        "a": "C",
        "options": ["A. increases", "B. remains unchanged", "C. decreases", "D. may decrease or increase"],
    },
    
    {
        "q": "Federation Cup in India is Associated with which game/ sport ❓",
        "a": "B",
        "options": ["A. Hockey", "B. Football", "C. Basketball", "D. Badminton"],
    },
    
    {
        "q": "The first Indian woman Gymnast to take part in Olympic Games ❓",
        "a": "D",
        "options": ["A. Kalpana Chawla", "B. Anju Bobby George", "C. P.T. Usha", "D. Deepa Karmakar"]
    },
    
    {
        "q": "The react,ion which converts sugar solution into alcohol is an example of ❓ ",
        "a": "C",
        "options": ["A. saponification", "B. hydrogenation", "C.fermentation", "D. hydrolysis"],
    },
    
    {
        "q": "Compressed Natural Gas (CNG) is mainly composed of ❓ ",
        "a": "D",
        "options": ["A. Butane", "B. Propane", "C.Ethane", "D.Methane"],
    },
    
    {
        "q": "Photo chemical smog always contains ❓",
        "a":"B",
        "options":["A. Aluminium ion", "B. Ozone", "C.Methane", "D.Phosphorous"],
    },
    
    {
        "q":"What does the abbreviation 'HIV' stand for ❓",
        "a": "B",
        "options": ["A. Human Immune Direct Virus", "B. Human Immunodeficiency Virus", "C.Human Immunotransmission Virus", "D.Human Immuno Virus"],
    },
    
    {
        "q": " Which of the following is called building block of life ❓",
        "a": "A",
        "options": ["A. Cell", "B. Genes", "C.Muscle fiber", "D. Chromosomes"],
    },
    
    {
        "q": " What is the name of the first Indian satellite in Space ❓",
        "a": "C",
        "options": ["A. METSAT", "B. Kalapna-I", "C.Aryabhatta", "D. INSAT-3D"],
    },
    
    {
        "q":"Friction can be reduced by changing over from ❓",
        "a":"A",
        "options": ["A. sliding to rolling", "B. rolling to sliding", "C.potential energy to kinetic energy", "D. Dynamic to static"],
    }
]

new_game()

while play_again():
    new_game()

print("Thanks for playing the game 👍")

'''------------------------'''
