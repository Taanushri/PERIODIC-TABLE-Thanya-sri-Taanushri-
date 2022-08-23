import random

def main():
    """Start a elemants guessing game."""
    print("*******************************************************************************************************************************")
    print("guess an elemant,if you can !")
    print("1.Hidrogen")
    print("2.Helium")
    print("3.Carbon")
    print("4.Nitrogen")
    print("5.Oxygen")
    print("6.Neon")
    
    list = ["Hidrogen","Helium","Carbon","Nitrogen","Oxygen","Neon"]
    x=random.choice(list)
    
    guess = None
    
    while x != guess:
        
        guess= str(input("Pick an elemant between Hidrogen,Helium,Carbon,Nitrogen,Oxygen,Neon:"))
                    
        if x == guess:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Welcome to the end of the game... YOU'RE THE WINNER.",)
        elif x != guess:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("To be a good loser is to learn how to win!!! TRY AGAIN.")
        
main()