#!/usr/bin/env python3
"""Simple interactive two-player Tic-Tac-Toe (terminal).

Usage: python tic_tac_toe.py
"""
import sys

WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def print_board(b):
    rows = [b[0:3], b[3:6], b[6:9]]
    for i, r in enumerate(rows):
        print(' ' + ' | '.join(r))
        if i < 2:
            print('---+---+---')


def check_winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != ' ' and b[a] == b[c] == b[d]:
            return b[a]
    return None


def play_one():
    board = [' '] * 9
    player = 'X'
    while True:
        print_board(board)
        move = input(f"Player {player}, enter move (1-9) or 'q' to quit: ").strip()
        if move.lower() in ('q', 'quit'):
            print('Goodbye')
            sys.exit(0)
        try:
            pos = int(move) - 1
        except ValueError:
            print('Invalid input — enter a number 1-9.')
            continue
        if pos < 0 or pos > 8:
            print('Move out of range — choose 1 through 9.')
            continue
        if board[pos] != ' ':
            print('Square already taken — choose another.')
            continue
        board[pos] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f'Player {winner} wins!')
            return
        if ' ' not in board:
            print_board(board)
            print('Draw!')
            return
        player = 'O' if player == 'X' else 'X'


def main():
    while True:
        play_one()
        again = input('Play again? (y/n): ').strip().lower()
        if again not in ('y', 'yes'):
            break


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nExited')
        sys.exit(0)
