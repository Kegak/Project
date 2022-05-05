from gui import *
import random
def main():
    window = Tk()
    window.geometry('300x100')
    window.resizable(False, False)
    window.title('Rock, Paper, Scissors against Computer')
    widgets = GUI(window)
    window.mainloop()

def game(p_input):
    comp_score = 0
    p_score = 0
#    for i in range(3):
    while p_input != 'paper':
        if p_input == 'paper':
            break
        elif p_input == 'rock':
            break
        elif p_input == 'scissor':
            break

    while p_input != 'rock':
        if p_input == 'paper':
            break
        elif p_input == 'rock':
            break
        elif p_input == 'scissor':
            break

    while p_input != 'paper':
        if p_input == 'paper':
            break
        elif p_input == 'rock':
            break
        elif p_input == 'scissor':
            break

        c_input = random.randint(1, 3)
        if c_input == 1:
            c_input = 'paper'
        elif c_input == 2:
            c_input = 'rock'
        else:
            c_input = 'scissor'

        if c_input == p_input:
            return f'Computer is {c_input}. You are {p_input}. You tie'
#            comp_score += 1
#            p_score += 1
        elif (c_input == 'paper') and (p_input == 'rock'):
            return f'Computer is {c_input}. You are {p_input}. You lose'
#            comp_score += 1
        elif (c_input == 'paper') and (p_input == 'scissor'):
            return f'Computer is {c_input}. You are {p_input}. You win'
#            p_score += 1
        elif (c_input == 'rock') and (p_input == 'paper'):
            return f'Computer is {c_input}. You are {p_input}. You win'
#            p_score += 1
        elif (c_input == 'rock') and (p_input == 'scissor'):
            return f'Computer is {c_input}. You are {p_input}. You lose'
#            comp_score += 1
        elif (c_input == 'scissor') and (p_input == 'rock'):
            return f'Computer is {c_input}. You are {p_input}. You win'
#            p_score += 1
        elif (c_input == 'scissor') and (p_input == 'paper'):
            return f'Computer is {c_input}. You are {p_input}. You lose'
#            comp_score += 1
#     if comp_score == p_score:
#         print('GAME OVER - IT\'S A TIE')
#     elif comp_score > p_score:
#         print('GAME OVER - COMPUTER WINS')
#     else:
#         print('GAME OVER - YOU WIN')
if __name__ == '__main__':
    main()