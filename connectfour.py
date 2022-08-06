'''
Uses numbers to drop colors, utilizing the standard connect four rules
Try and connect four of your colored checker pieces in a row, 
 This can be done horizontally, vertically or diagonally. Each player will drop in one checker piece at a time. 
This will give you a chance to either build your row, or stop your opponent from getting four in a row.


@author: Brandon Claspill
'''

# Use this as Main program

# USE Number Keys on Keyboard to drop your piece, Each player is a different color. RED or BLACK
# Choose to play again when the game is over by choosing Y for YES or N for NO. Have Fun !
from game import Game

game = Game()
game.game_loop()