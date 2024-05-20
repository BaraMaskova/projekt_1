"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Mašková
email: baramaskova@seznam.cz
discord: baramaskova
"""

# Předpřipravené texty
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

# Registrovani uzivatele
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Overeni uzivatele
username = input("username: ")
password = input("password: ")

if username in registered_users and registered_users[username] == password:
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")

    # Ziskani vstupu pro vyber textu
    text_choice = input("Enter a number btw. 1 and 3 to select: ")

    # Kontrola vstupu pro vyber textu
    if text_choice.isdigit():
        text_choice = int(text_choice)
        if 1 <= text_choice <= 3:
            print("----------------------------------------")

            # Analyza textu
            text = TEXTS[text_choice - 1]
            words = text.split()
            num_words = len(words)
            titlecase_words = 0
            uppercase_words = 0
            lowercase_words = 0
            num_numbers = 0
            sum_numbers = 0

            for word in words:
                if word.istitle():
                    titlecase_words += 1
                if word.isupper():
                    uppercase_words += 1
                if word.islower():
                    lowercase_words += 1
                if word.isdigit():
                    num_numbers += 1
                    sum_numbers += int(word)

            print("There are", num_words, "words in the selected text.")
            print("There are", titlecase_words, "titlecase words.")
            print("There are", uppercase_words, "uppercase words.")
            print("There are", lowercase_words, "lowercase words.")
            print("There are", num_numbers, "numeric strings.")
            print("The sum of all the numbers is", sum_numbers)
            print("----------------------------------------")

            # Frekvence delek slov
            word_length_freq = {}
            for word in words:
                length = len(word)
                if length in word_length_freq:
                    word_length_freq[length] += 1
                else:
                    word_length_freq[length] = 1

            print("LEN|  OCCURENCES  |NR.")
            print("----------------------------------------")
            for length in sorted(word_length_freq):
                freq = word_length_freq[length]
                print(length, "|", '*' * freq, "|", freq)
else:
    print("unregistered user, terminating the program..")