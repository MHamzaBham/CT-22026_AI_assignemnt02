import random
import time
import random
import matplotlib.pyplot as plt

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(board, position, player):
    board[position] = player

def is_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[pos] == player for pos in line) for line in win_positions)

def is_full(board):
    return ' ' not in board

def terminal(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move_minimax(board):
    best_score = -float('inf')
    move = None
    for pos in moves(board):
        board[pos] = 'O'
        score = minimax(board, 0, False)
        board[pos] = ' '
        if score > best_score:
            best_score = score
            move = pos
    return move

def minimax_alphabeta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in moves(board):
            board[move] = 'O'
            score = minimax_alphabeta(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in moves(board):
            board[move] = 'X'
            score = minimax_alphabeta(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def best_move_alphabeta(board):
    best_score = -float('inf')
    move = None
    for pos in moves(board):
        board[pos] = 'O'
        score = minimax_alphabeta(board, 0, -float('inf'), float('inf'), False)
        board[pos] = ' '
        if score > best_score:
            best_score = score
            move = pos
    return move

def play_game(ai_type='minimax'):
    board = create_board()
    human = 'X'
    ai = 'O'
    current_player = human if random.choice([True, False]) else ai

    print("Starting new game!")
    print("Board positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")
    print_board(board)

    while not terminal(board):
        if current_player == human:
            valid_move = False
            while not valid_move:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if move in range(0, 9) and board[move] == ' ':
                        make_move(board, move, human)
                        valid_move = True
                        current_player = ai
                    else:
                        print("Invalid move. Spot already taken or out of range. Try again.")
                except ValueError:
                    print("Please enter a valid number between 1 and 9.")
        else:
            print("AI is making a move...")
            if ai_type == 'minimax':
                move = best_move_minimax(board)
            else:
                move = best_move_alphabeta(board)
            make_move(board, move, ai)
            current_player = human

        print_board(board)

    if is_winner(board, human):
        print("Congratulations! You win!")
    elif is_winner(board, ai):
        print("AI wins! Better luck next time!")
    else:
        print("It's a tie!")

play_game(ai_type='minimax')

play_game(ai_type='alphabeta')

def measure_performance():
    minimax_times = []
    alphabeta_times = []

    for _ in range(50):
        board = create_board()

        for _ in range(random.randint(3, 6)):
            move = random.choice(moves(board))
            make_move(board, move, random.choice(['X', 'O']))

        if terminal(board):
            continue

        start = time.time()
        best_move_minimax(board)
        end = time.time()
        minimax_times.append(end - start)

        start = time.time()
        best_move_alphabeta(board)
        end = time.time()
        alphabeta_times.append(end - start)

    avg_minimax_time = sum(minimax_times) / len(minimax_times)
    avg_alphabeta_time = sum(alphabeta_times) / len(alphabeta_times)

    print(f"Average Minimax Time: {avg_minimax_time:.6f} seconds")
    print(f"Average Alpha-Beta Pruning Time: {avg_alphabeta_time:.6f} seconds")

    return avg_minimax_time, avg_alphabeta_time

def plot_performance(minimax_time, alphabeta_time):
    algorithms = ['Minimax', 'Alpha-Beta Pruning']
    times = [minimax_time, alphabeta_time]

    plt.figure(figsize=(8,6))
    bars = plt.bar(algorithms, times, color=['blue', 'green'])
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance Comparison: Minimax vs Alpha-Beta Pruning')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.25, yval + 0.0005, f'{yval:.6f}')

    plt.show()

minimax_time, alphabeta_time = measure_performance()
plot_performance(minimax_time, alphabeta_time)

