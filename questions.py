from string import ascii_lowercase


    # user_input = input('Enter "c" to create a new player\nEnter "r" to see score of existing players\nEnter "u" to update existing player\nEnter "d" to delete player\n')

    # while(not user_input in ['c', 'r', 'u', 'd']):
    #     print("Invalid input! Please try again!")
    #     print("What would you like to do?")
    #     user_input = input('Enter "c" to create a new player\nEnter "r" to see score of existing players\nEnter "u" to update existing players\nEnter "d" to delete player\n')

    # if user_input == 'c':
    #     print("You've chosen to create a new player!")
    #     hotel_name = input("Enter the name for the player you would like to create:\n")
    #     hotel = Hotel(name=hotel_name)
    #     session.add(hotel)
    #     session.commit()
    #     print(f"Success! Your new player, {hotel.name}, has been created!")

    # elif user_input == 'r':
    #     print("You've chosen to get players score!")
    #     hotels = session.query(Hotel)
    #     print(f"There are {hotels.count()} hotels available!")
    #     print("Here is the info of all available hotels:")
    #     for hotel in hotels:
    #         print(hotel)

    # elif user_input == 'u':
    #     print("You're chosen to update existing player!")
    #     hotels = session.query(Hotel)
    #     print("Here is the info of all available players:")
    #     for hotel in hotels:
    #         print(hotel)
    #     hotel_id = input("Please enter the integer value for the id of the hotel that you would like to update: ")
    #     hotel = hotels.filter(Hotel.id == int(hotel_id)).first()
    #     hotel_name = input("Please enter the name that you would like to update this hotel to: ")
    #     hotel.name = hotel_name
    #     session.commit()
    #     print(f"Success! Player #{hotel.id} has been updated to have the name {hotel.name}!")

    # elif user_input == 'd':
    #     print("You've chosen to delete existing player!")
    #     hotels = session.query(Hotel)
    #     print("Here is the info of all available player:")
    #     for hotel in hotels:
    #         print(hotel)
    #     hotel_id = input("Please enter the integer value for the id of the hotel that you would like to delete or enter 'a' to delete all players: ")
    #     if hotel_id == 'a':
    #         hotels.delete()
    #         session.commit()
    #         print(f"Success! All players have been deleted from the database!")
    #     else:
    #         hotel = hotels.filter(Hotel.id == int(hotel_id)).first()
    #         session.delete(hotel)
    #         session.commit()
    #         print(f"Success! player #{hotel.id}: {hotel.name} has been deleted from the database!")

            

# answer = input("\nWelcome to the Trivia!\nPRESS ENTER TO START!\nWelcome to the Trivia!\nPRESS ENTER TO START!\nWelcome to the Trivia!\nPRESS ENTER TO START!\nWelcome to the Trivia!\nPRESS ENTER TO START!")


# print(

#     '''
# :.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:
# ''')

# def load_game():
#     print("....PLAYER_NAME....")
# load_game()


# print("Welcome to the Trivia!\nWelcome to the Trivia!")

# print(

#     '''
# :.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:
# ''')

QUESTIONS = {
    "This French general has won 38 out of all 43 listed battles he leads his troops into battle...": [
        "Napoleon Bonaparte", "Toussaint Louverture", "Oscar-Claude Monet", "Joan of Arc"
    ],
    "What general was in command of the United States Army during World War I?": [
        "George S. Patton", "Geranimo", "George Washington", "William T. Sherman"
    ],
    "This volcano eruption was one of the deadliest and most destructive volcanic events in recorded history, what was the volcano called?": [
        "Krakatoa", "Pompei", "Rincon de la Vieja", "Great Sitkin"
    ],
    "Who holds the record in the mile run?": [
        "Hicham El Guerrouj",
        "Haile Gebrselassie",
        "Jim Ryan",
        "Bill Bowerman",
    ],
    "Who was the ruler of the Mongolian Empirer?": [
        "Genghis Khan", "Kublai Khan", "Amir Khan", "Shah Rukh Khan"
    ],
    "This general fought Alexander the great and defeated him with elephants during the punic wars? Who is this general?": [
        "Hanibal Barca", "Scipio Africanus", "Hanno I the Great", "Mago III"
    ],
    "Who was the Persian king from (486–465 bce), the son and successor of Darius I?": [
        "Xerxes I",
        "Cyrus the Great",
        "Nebuchadnezzar",
        "Artaxerxes I",
    ],
    "Who was the 35th presidant of the United States?'": [
        "John F Kennedy", "Richard Nixon", "Abraham Lincoln", "Harry S. Truman"
    ],
    "What is ther biggest island in the world?": [
        "New Guinea", "Japan", "Great Britain", "Tasmania"
    ],
    "Who is the first nordic person to be documented sailing and landing in the Americas?": [
        "Leif Erikson", "while", "each", "loop"
    ],
    "What family ruled Japan from 1603 until the Meiji Restoration in 1868": [
        "Tokugawa", "Fujiwara", "Musashi", "Yamamoto"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "1826", "while", "each", "loop"
    ],
    "Where was the first city to have elecric street lights?": [
        "1880 Wabash, Indiana",
        "1864 Topeka, Kansas",
        "1803 New York, New York",
        "1810 Detroit, Michigan",
    ],

    "What century was the rifle created?": [
        "15th Century",
        "14th Century",
        "16th Century",
        "13th Century",
    ]
}
def play_game(player):
    print(''':.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:''')
    print(f"WELOME TO TRIVIA {player.name}!!!")

    num_correct = 0
    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        while (answer_label := input("\nAnswer? ")) not in labeled_alternatives:
            print(f"Please answer one of {', '.join(labeled_alternatives)}")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            num_correct += 1
            print("⭐ Correct! ⭐")
            print(f"{player.name} Current Score:")
            print(num_correct)
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
            

    print(f"\n{player.name} got {num_correct} correct out of {num} questions")
    print(f"{player.name} new total score is {player.score + num_correct}")
    return num_correct