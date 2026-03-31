class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boards = collections.defaultdict(set)
            
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if value in rows[row]:
                    return False
                if value in cols[col]:
                    return False
                if value in boards[(row // 3, col // 3)]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boards[(row // 3, col // 3)].add(value)
        return True