import random

t_map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

t_nodes = []

def print_map():
    print('-------------')
    for row in range(0, 3):
        t_row = ''
        for col in range(0, 3):
            node = [row, col]
            t_nodes.append(node)
            t_row += str(t_map[row][col]) + ' | '

        print(f"| {t_row} ")

    print('-------------')


def userInput():
    invalid_input = True
    while invalid_input:
        while True:
            try:
                user_input = int(input("Enter position: "))
                break
            except ValueError:
                print("Please enter only numbers! (0 - 9)")

        if user_input in range(0, 9):
            node1 = t_nodes[user_input]
            if t_map[node1[0]][node1[1]] != 'x' and t_map[node1[0]][node1[1]] != '-':
                t_map[node1[0]][node1[1]] = 'x'
                invalid_input = False
            else:
                print('This position is already marked!')
        else:
            print("Please enter numbers in range of 0 - 9!")


def botInput():
    bot_input = 0
    invalid_input = True
    while invalid_input:
        bot_input = random.randint(0, 9)

        if bot_input in range(0, 9):
            node1 = t_nodes[bot_input]
            if t_map[node1[0]][node1[1]] != 'x' and t_map[node1[0]][node1[1]] != '-':
                t_map[node1[0]][node1[1]] = '-'
                invalid_input = False
    return bot_input


def verify_winner():
    x_count = 0
    o_count = 0
    winner = ''

    if len(winner) < 1:
        for row in t_map:
            for col in row:
                if col == 'x':
                    x_count += 1

                if col == '-':
                    o_count += 1

            if x_count == 3:
                winner = 'x'
                break

            if o_count == 3:
                winner = '-'
                break

            x_count = 0
            o_count = 0

    if len(winner) < 1:
        for col in range(3):
            for row in range(3):
                if t_map[row][col] == 'x':
                    x_count += 1
                
                if t_map[row][col] == '-':
                    o_count += 1
            
            if x_count == 3:
                winner = 'x'
                break

            if o_count == 3:
                winner = '-'
                break
            
            x_count = 0
            o_count = 0
    
    if len(winner) < 1:
        for i in range(3):
            if t_map[i][i] == 'x':
                x_count += 1
            
            if t_map[i][i] == '-':
                o_count += 1
            
        if x_count == 3:
            winner = 'x'


        if o_count == 3:
            winner = '-'

        
        x_count = 0
        o_count = 0

    if len(winner) < 1:
        for i in range(3):
            if t_map[0][2] == 'x' and t_map[1][1] == 'x' and t_map[2][0] == 'x':
                x_count += 1
            
            if t_map[0][2] == '-' and t_map[1][1] == '-' and t_map[2][0] == '-':
                o_count += 1
            
        if x_count == 3:
            winner = 'x'


        if o_count == 3:
            winner = '-'

        
        x_count = 0
        o_count = 0

    return winner


def reset():
    i = 0
    for row in range(3):
        for col in range(3):
            t_map[row][col] = i
            i += 1


def play_tictactoe():
    playing = True
    while playing:
        print_map()
        for node_count in range(5):
            userInput()
            if node_count < 4:
                botInput()

            if node_count > 1:
                get_winner = verify_winner()
                if len(get_winner) > 0:
                    if get_winner == 'x':
                        print('Hooray, you won!')
                    if get_winner == '-':
                        print('You loose!')
                    print_map()
                    break

                if node_count == 4 and len(get_winner) == 0:
                    print("It's a draw!")
                    print_map()
                    break

            print_map()
        
        play_again = input('Play again? (y/n): ')
        if play_again == 'y' or play_again == 'Y':
            playing = True
            reset()
        else:
            playing = False


play_tictactoe()