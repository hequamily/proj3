import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Hotel

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db/hotels.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to the Trivia!")
    print(':.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:')

    user_input = input('Enter "c" to create a new player\nEnter "r" to see scores of existing players\nEnter "u" to update an existing player\nEnter "d" to delete a player\n')

    while not user_input in ['c', 'r', 'u', 'd']:
        print("Invalid input! Please try again!")
        print("What would you like to do?")
        user_input = input('Enter "c" to create a new player\nEnter "r" to see scores of existing players\nEnter "u" to update an existing player\nEnter "d" to delete a player\n')

    if user_input == 'c':
        print("You've chosen to create a new player!")
        player_name = input("Enter the name for the player you would like to create:\n")
        player = Hotel(name=player_name)
        session.add(player)
        session.commit()
        print(f"Success! Your new player, {player.name}, has been created!")

    elif user_input == 'r':
        print("You've chosen to get players' scores!")
        players = session.query(Hotel)
        print(f"There are {players.count()} players available!")
        print("Here is the info of all available players:")
        for player in players:
            print(player)

    elif user_input == 'u':
        print("You've chosen to update an existing player!")
        players = session.query(Hotel)
        print("Here is the info of all available players:")
        for player in players:
            print(player)
        player_id = input("Please enter the integer value for the ID of the player that you would like to update: ")
        player = players.filter(Hotel.id == int(player_id)).first()
        player_name = input("Please enter the name that you would like to update this player to: ")
        player.name = player_name
        session.commit()
        print(f"Success! Player #{player.id} has been updated to have the name {player.name}!")

    elif user_input == 'd':
        print("You've chosen to delete an existing player!")
        players = session.query(Hotel)
        print("Here is the info of all available players:")
        for player in players:
            print(player)
        player_id = input("Please enter the integer value for the ID of the player that you would like to delete or enter 'a' to delete all players: ")
        if player_id == 'a':
            players.delete()
            session.commit()
            print(f"Success! All players have been deleted from the database!")
        else:
            player = players.filter(Hotel.id == int(player_id)).first()
            session.delete(player)
            session.commit()
            print(f"Success! Player #{player.id}: {player.name} has been deleted from the database!")

    answer = input("When was the first known use of the word 'quiz'? ")
    if answer == "1781":
        print("Correct!")
    else:
        print(f"The answer is '1781', not {answer!r}")
