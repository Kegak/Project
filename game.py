import random
class Game:
    """
    Sets up a class for the rock paper scissors to run on
    """
    def __init__(self, p_input, c_input):
        """
        Method that allows the user to enter a rock, paper,
        scissors input.
        """
        self.__p_input = p_input
        self.__c_input = c_input
#        comp_score = 0
#        p_score = 0
#       for i in range(3):



    def __str__(self):
        """
        This method generates a computer input, and compares it to
        the player input, it then determines a winner
        """
        if type(self.__p_input) != str:
            raise TypeError
        if self.__p_input != 'paper':
            if self.__p_input != 'rock':
                if self.__p_input != 'scissor':
                    raise ValueError
        if self.__c_input == None:
            self.__c_input = random.randint(1, 3)
        if self.__c_input == 1:
            self.__c_input = 'paper'
        elif self.__c_input == 2:
            self.__c_input = 'rock'
        elif self.__c_input == 3:
            self.__c_input = 'scissor'
        if self.__c_input == self.__p_input:
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You tie'
#            comp_score += 1
#            p_score += 1
        elif (self.__c_input == 'paper') and (self.__p_input == 'rock'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You lose'
#            comp_score += 1
        elif (self.__c_input == 'paper') and (self.__p_input == 'scissor'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You win'
#            p_score += 1
        elif (self.__c_input == 'rock') and (self.__p_input == 'paper'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You win'
#            p_score += 1
        elif (self.__c_input == 'rock') and (self.__p_input == 'scissor'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You lose'
#            comp_score += 1
        elif (self.__c_input == 'scissor') and (self.__p_input == 'rock'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You win'
#            p_score += 1
        elif (self.__c_input == 'scissor') and (self.__p_input == 'paper'):
            return f'Computer is {self.__c_input}. You are {self.__p_input}. You lose'
#            comp_score += 1
#     if comp_score == p_score:
#         print('GAME OVER - IT\'S A TIE')
#     elif comp_score > p_score:
#         print('GAME OVER - COMPUTER WINS')
#     else:
#         print('GAME OVER - YOU WIN')