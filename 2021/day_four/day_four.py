"""

1. Count the sum of each board.
2. Generate sets with all of the column and row values
   
   each board will have sets of columns and sets of rows

for each board we want to store the 





Define a winner

Their board needs to be filled in either horizonal markings or vertical


as we mark the board, we want to keep track of the sum of our board



Evaluating a board is O(10)


GraphNode:
  value
  visited
"""

class Board:
    def __init__(self, matrix) -> None:
        """
        columns = [set(22, 8,21,6,1), set(13,2,9,10,12), set(17,23,14,3,20), set(11,4,16,18,15), set(0,24,7,5,19)]
        rows = [set(22,13,17,11,0), set(), set(), set(), set()]

        number_of_visted
        """
        self.items = set()
        self.board_sum = 0
        self.columns = [set() for _ in range(5)]
        self.rows = [set() for _ in range(5)]
        self._preprocess(matrix)
    def _preprocess(self, matrix):

        for row in range(5):
            for col in range(5):
                self.board_sum += matrix[row][col]
                self.items.add(matrix[row][col])
                self.columns[col].add(matrix[row][col])
                self.rows[row].add(matrix[row][col])


class PlayBingoAgainstSquidBruh:
    def __init__(self, moves, matrices) -> None:
        """
        Game Constructor.
        """
        self.moves = moves
        self.boards = []
        self._build_boards(matrices)
    
    def _build_boards(self, matrices):
        for matrix in matrices:
            self.boards.append(Board(matrix))
    def __call__(self):
        """
        Play each move:
            in each move we want to go through all the boards:
                if the move isnt in the board we move onto the next
                else:
                    remove this state from the board and check if that resulted in bingo


        """

        for move in self.moves:

            for board in self.boards:
                if move not in board.items:
                    continue
                # play the move on that row and column
                for curr in range(5):
                    augmented = False
                    if move in board.columns[curr]:
                        augmented = True
                        board.columns[curr].remove(move)
                    if move in board.rows[curr]:
                        augmented = True
                        board.rows[curr].remove(move)
                    if augmented:
                        board.board_sum -= move
                    
                        if len(board.rows[curr]) == 0 or len(board.columns[curr]) == 0:
                            return board.board_sum * move

        # if there is no winning state 
        return -1

def load_input():
    """
    return moves and a list of boards
    """
    import os
    moves = []
    boards = []
    with open(os.path.join(os.getcwd(), '2021/day_four/day_four.txt'), 'rt') as f:
        """
        
        """
        moves = [int(move) for move in next(f).split(",")]
        next(f)
        curr_board = []
        count = 1
        for line in f:
            # Keep a count of 5 when we get to 6 

            if line == '\n':
                boards.append(curr_board)
                count = 1
                curr_board = []
                continue

            curr_line = [int(item) for item in line.replace("\n", "").split(" ") if item != ""]
            curr_board.append(curr_line)
            count += 1
            
    return (moves,boards)

moves, boards = load_input()

new_game = PlayBingoAgainstSquidBruh(moves=moves, matrices=boards)

print(new_game())