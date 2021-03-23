class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.findWordStartingAt(i, j, board, word):
                    return True
        return False
    
    # You can either store the coordinates that have been checked in a dictionary
    # or alter the board as you go. This solution alters the board during recursion,
    # but must reset the value in case the entire word is does not correctly match.
    def findWordStartingAt(self, i, j, board, word):
        
        if len(word) == 0:
            return True
        elif i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        elif board[i][j] != word[0]:
            return False
        board[i][j] = None
        
        letter = word[0]
        word = word[1:]
        
        word_found = \
        self.findWordStartingAt(i + 1, j, board, word) or \
        self.findWordStartingAt(i - 1, j, board, word) or \
        self.findWordStartingAt(i, j + 1, board, word) or \
        self.findWordStartingAt(i, j - 1, board, word)
    
        board[i][j] = letter
        
        return word_found