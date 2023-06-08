import PIL.Image

def main():
    print("PRINT")
    path = input("Enter the path to the image field : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ");

ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 100):
    old_width, old_height = image.size
    new_height = new_width * old_height / old_width
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str

import PIL.Image
def main():
    path = input("Enter the path to the image field : \n")
    # ^^^^^^^^ put image address here
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
    #resize image
    image = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);
main()






import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Hotel

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/hotels.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to the Trivia!")
    print('''
:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:
''')

    user_input = input('Enter "c" to create a new player\nEnter "r" to see scores of existing players\nEnter "u" to update an existing player\nEnter "d" to delete a player\n')

    while user_input not in ['c', 'r', 'u', 'd']:
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
        if player:
            player_name = input("Please enter the new name for this player: ")
            player.name = player_name
            session.commit()
            print(f"Success! Player #{player.id} has been updated to have the name {player.name}!")
        else:
            print("Player not found!")

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
            if player:
                session.delete(player)
                session.commit()
                print(f"Success! Player #{player.id}: {player.name} has been deleted from the database!")
            else:
                print("Player not found!")

answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
    print("Correct!")
else:
    print(f"The answer is '1781', not {answer!r}")

