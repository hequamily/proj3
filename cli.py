import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db.models import Player
from questions import play_game
if __name__ == '__main__':
    Base = declarative_base()
    engine = create_engine('sqlite:///db/players.db')
    Base.metadata.create_all(engine, tables=[Player.__table__])
    Session = sessionmaker(bind=engine)
    session = Session()



    

    print(

    '''
:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:
''')
    # while(not user_input in ['c', 'r', 'u', 'd']):
    #     print("Invalid input! Please try again!")
    #     print("What would you like to do?")
    print("Welcome to the Trivia!")
    user_input = input('\n---MENU---\nEnter "c" to create a new player\nEnter "r" to see score of existing players\nEnter "u" to update existing player\nEnter "d" to delete player\nEnter "p" to PLAY\nEnter "quit" to quit\n----------\n')



        
    while(user_input != "quit"):
        if user_input == 'c':
            print("You've chosen to create a new player!")
            player_name = input("Enter the name for the player you would like to create:\n")
            player = Player(name=player_name, score=0)
            session.add(player)
            session.commit()
            print(f"Success! Your new player, {player.name}, has been created!")

        elif user_input == 'r':
            print("You've chosen to get players score!")
            players = session.query(Player)
            print(f"There are {players.count()} players!")
            print("Here is the info of all available players:")
            for player in players:
                print(player)

        elif user_input == 'u':
            print("You're chosen to update existing player!")
            players = session.query(Player)
            print("Here is the info of all available players:")
            for player in players:
                print(player)
            player_id = input("Please enter the integer value for the id of the player that you would like to update: ")
            player = players.filter(Player.id == int(player_id)).first()
            player_name = input("Please enter the name that you would like to update this player to: ")
            player.name = player_name
            session.commit()
            print(f"Success! Player #{player.id} has been updated to have the name {player.name}!")

        elif user_input == 'd':
            print("You've chosen to delete existing player!")
            players = session.query(Player)
            print("Here is the info of all available player:")
            for player in players:
                print(player)
            player_id = input("Please enter the integer value for the id of the player that you would like to delete or enter 'a' to delete all players: ")
            if player_id == 'a':
                players.delete()
                session.commit()
                print(f"Success! All players have been deleted from the database!")
            else:
                player = players.filter(Player.id == int(player_id)).first()
                session.delete(player)
                session.commit()
                print(f"Success! player #{player.id}: {player.name} has been deleted from the database!")       
        elif user_input == "p":
            players = session.query(Player)     
            for player in players:
                print(player)

            player_id = input("Please type player id int you would like to play with\n")
            player = players.filter(Player.id == int(player_id)).first()
            current_score = play_game(player)
            player.score = player.score + current_score
            session.commit()
        else:
            print("Invalid input! Please try again!")
            print("What would you like to do?")
        user_input = input('\n---MENU---\nEnter "c" to create a new player\nEnter "r" to see score of existing players\nEnter "u" to update existing player\nEnter "d" to delete player\nEnter "p" to PLAY\nEnter "quit" to quit\n----------\n')

# answer = input("When was the first known use of the word 'quiz'? ")
# if answer == "yes":
#     print("lets go")
# else:
#     print(f"are you sure you dont want to play{player}")