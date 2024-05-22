import random
import os

# Dictionary of countries and their capitals
countries_and_capitals = {
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "Ukrain": "Kyiv"
}

# Print correct and wrong answers
def display_answers(correct_answers, wrong_answers):
    clear()
    print(f'Correct Answers = {len(correct_answers)} \n{"-" * 30}')
    for i in correct_answers:
        print(f'{i}'.upper())

    print(f"\n{'=-=' * 30}\n")

    print(f'Wrong Answers = {len(wrong_answers)} \n{"-" * 30}')
    for i in wrong_answers:
        print(f'{i}'.upper())

# Clear the terminal screen
def clear():
    os.system('cls||clear')

# Display the game title
def title():
    print(f'+{"-" * 81}+')
    print(f'|{"Capital Quest!":^81}|'.upper())
    print(f'+{"-" * 81}+')

# Display the welcome message and instructions
def welcome():
    print(f'+{"-" * 81}+')
    print(f'|{"Welcome to Capital Quest!":^81}|')
    print(f'|{" ":^81}|')
    print(f'|{" Test your knowledge of world capitals in this fun and fast-paced quiz game.":<81}|')
    print(f'|{" This game features 10 questions where you\'ll match each country to its capital.":<81}|')
    print(f'|{" Can you get them all right? Let\'s find out!":<81}|')
    print(f'+{"-" * 81}+')
    print()

# Main game function
def play():
    while True:
        clear()
        welcome()
        
        correct_answers = []
        wrong_answers = []

        playing = input(f'\n1 - Play \n2 - Exit \n{"-" * 9} \n>  ')

        if playing == '1':
            remaining_countries = countries_and_capitals.copy()
            while remaining_countries:
                clear()
                
                country = random.choice(list(remaining_countries.keys()))
                
                answer = input(f'What is the capital of the {country}? \n>  ')
                
                if answer.lower() == remaining_countries[country].lower() or answer.lower() == 'Brasilia'.lower():
                    print('\nCorrect!')
                    correct_answers.append(f'{country}: {remaining_countries[country]}')
                                        
                else:
                    print(f'\nWrong! The capital of the {country} is {remaining_countries[country]}')
                    wrong_answers.append(f'{country}: {answer} ({remaining_countries[country]})')
                    
                del remaining_countries[country]
                input('\nPress any key to continue...')
                clear()

        elif playing == '2':break

        else: continue
    
        display_answers(correct_answers, wrong_answers)
        print()
        break
    
play()
