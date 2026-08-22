from collections import deque

class Solution:
    def snakesAndLadders(self, board):

        n = len(board)

        def get_position(square):
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n

            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:

            square, moves = queue.popleft()

            if square == n * n:
                return moves

            for dice in range(1, 7):

                next_square = square + dice

                if next_square > n * n:
                    break

                r, c = get_position(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1
