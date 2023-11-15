import pygame
import random
import time
from button import Button # By importing Button we can access methods from the Button class


pygame.init()
clock = pygame.time.Clock()
# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 227, 0)
RED_ON = (255, 0, 0)
RED_OFF = (227, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 227)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (227, 227, 0)
# Pass in respective sounds for each color

GREEN_SOUND ="bell1.mp3" # bell1
RED_SOUND = "bell2.mp3" # bell2
BLUE_SOUND = "bell3.mp3" # bell3
YELLOW_SOUND = "bell4.mp3" # bell4
# Button Sprite Objects
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 10)
red = Button(RED_ON, RED_OFF, RED_SOUND, 260, 10)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 260, 260) 
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 10, 260)
# Variables
colors = ["green", "red", "blue", "yellow"]
cpu_sequence = []
choice = ""


'''
Draws game board
'''
def draw_board():
# Call the draw method on all four button objects
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)


'''
Chooses a random color and appends to cpu_sequence.
Illuminates randomly chosen color.
'''
def cpu_turn():
    choice = random.choice(colors) # pick random color
    cpu_sequence.append(choice) # update cpu sequence
    if choice == "green":
        green.update(SCREEN)
    # Check other three color options
    if choice == "red":
        red.update(SCREEN)
    if choice == "blue":
        blue.update(SCREEN)
    if choice == "yellow":
        yellow.update(SCREEN)


'''
Plays pattern sequence that is being tracked by cpu_sequence
'''
def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            elif color == "yellow":
                yellow.update(SCREEN)
    else:
        yellow.update(SCREEN)
        pygame.time.wait(500)


'''
After cpu sequence is repeated the player must attempt to copy the same pattern sequence.
The player is given 3 seconds to select a color and checks if the selected color matches the cpu
If player is unable to select a color within 3 seconds then the game is over and the pygame windo
'''
def player_turn():
    turn_time = time.time()
    players_sequence = []
    while time.time() <= turn_time + 3 and len(players_sequence) < len(cpu_sequence):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # button click occured
            # Grab the current position of mouse here
                pos = pygame.mouse.get_pos()
                if green.selected(pos): # green button was selected
                    green.update(SCREEN) # illuminate button
                    print('green selected')
                    players_sequence.append("green") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer
                    # Check other three options
                if red.selected(pos): # green button was selected
                    red.update(SCREEN) # illuminate button
                    print('red selected')
                    players_sequence.append("red") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer
                if blue.selected(pos): # green button was selected
                    blue.update(SCREEN) # illuminate button
                    print('blue selected')
                    players_sequence.append("blue") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer
                if yellow.selected(pos): # green button was selected
                    yellow.update(SCREEN) # illuminate button
                    print('yellow selected')
                    players_sequence.append("yellow") # add to player sequence
                    check_sequence(players_sequence) # check if player choice was correct
                    turn_time = time.time() # reset timer
    # If player does not select a button within 3 seconds then the game closes
    if not time.time() <= turn_time + 3:
        game_over()


'''
Checks if player's move matches the cpu pattern sequence
'''
def check_sequence(players_sequence):
    if players_sequence != cpu_sequence[:len(players_sequence)]:
        game_over()


'''
Quits game and closes pygame window
'''
def game_over():
    pygame.quit()
    quit()


if __name__ == "__main__":
    # Game Loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()

        pygame.display.update()
        draw_board() # draws buttons onto pygame screen
        repeat_cpu_sequence() # repeats cpu sequence if it's not empty
        cpu_turn() # cpu randomly chooses a new color
        player_turn() # player tries to recreate cpu sequence
        pygame.time.wait(1000) # waits one second before repeating cpu sequence
        clock.tick(60)