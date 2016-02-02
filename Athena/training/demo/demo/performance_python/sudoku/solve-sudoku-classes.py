import sys
import numpy as np
from time import clock
from copy import copy

N = 9
all_digits = '123456789'

def some(seq):
    for e in seq:
        if e: return e
    return False

class DictSudokuSolver(object):

    def __init__(self):
        def cross(A, B):
            "Cross product of elements in A and elements in B."
            return [a+b for a in A for b in B]

        digits   = '123456789'
        rows     = 'ABCDEFGHI'
        cols     = digits
        squares  = cross(rows, cols)
        unitlist = ([cross(rows, c) for c in cols] +
                    [cross(r, cols) for r in rows] +
                    [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        units = dict((s, [u for u in unitlist if s in u]) 
                     for s in squares)
        peers = dict((s, set(sum(units[s],[]))-set([s]))
                     for s in squares)
        empty_board = dict((s, digits) for s in squares)

        self.squares = squares
        self.empty_board = empty_board
        self.units = units
        self.peers = peers
        self.all_idxs = unitlist

    def eliminate(self, board, loc, val):
        if val not in board[loc]:
            return board
        board[loc] = board[loc].replace(val, '')
        if len(board[loc]) == 0:
            return False
        elif len(board[loc]) == 1:
            val2 = board[loc]
            if not all(self.eliminate(board, loc2, val2) for loc2 in self.peers[loc]):
                return False
        for u in self.units[loc]:
            dplaces = [s for s in u if val in board[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(board, dplaces[0], val):
                    return False
        return board

    def assign(self, board, loc, val):
        other_values = board[loc].replace(val, '')
        if all(self.eliminate(board, loc, val2) for val2 in other_values):
            return board
        else:
            return False

    def initialize(self, spec):
        board = copy(self.empty_board)
        for s, d in enumerate(spec):
            s = self.squares[s]
            if d in all_digits and not self.assign(board, s, d):
                return False
        return board

    def search(self, board):
        if board is False or self.is_solved(board):
            return board
        n, s = min((len(board[s]), s) for s in self.squares if len(board[s]) > 1)
        return some(self.search(self.assign(copy(board), s, d))
                    for d in board[s])

    def is_solved(self, board):
        if all(len(v) == 1 for v in board.values()):
            return True
        return False

    def verify(self, board):
        if (not self.is_solved(board) or
                any(board.values().count(d) != N for d in all_digits) or
                any(set(board[i] for i in idxs) != set(all_digits) for idxs in self.all_idxs)):
            return False
        return True


class ListSudokuSolver(object):

    def __init__(self):
        squares = range(N*N)
        empty_board = [all_digits] * (N * N)

        idxs_from_row = {}
        for row in range(N):
            for i in range(N):
                idxs_from_row.setdefault(row, []).append(row*N+i)

        idxs_from_col = {}
        for col in range(N):
            for i in range(N):
                idxs_from_col.setdefault(col, []).append(i*N+col)

        idxs_from_block = {}
        for sq_row in range(3):
            for sq_col in range(3):
                for i in range(sq_row*3, (sq_row+1)*3):
                    for j in range(sq_col*3, (sq_col+1)*3):
                        idxs_from_block.setdefault((sq_row,sq_col), []).append(i*N+j)

        all_idxs = idxs_from_row.values() + idxs_from_col.values() + idxs_from_block.values()

        units = {}
        peers = {}
        for idx in range(N*N):
            row, col = divmod(idx, N)
            units[idx] = [set(idxs_from_row[row]),
                                   set(idxs_from_col[col]),
                                   set(idxs_from_block[row/3, col/3])]
            peers[idx] = sorted(
                    set(idxs_from_row[row] + 
                        idxs_from_col[col] + 
                        idxs_from_block[row/3,col/3]) - set([idx]))

        self.squares = squares
        self.empty_board = empty_board
        self.units = units
        self.peers = peers
        self.all_idxs = all_idxs

    def eliminate(self, board, loc, val):
        if val not in board[loc]:
            return board
        board[loc] = board[loc].replace(val, '')
        if len(board[loc]) == 0:
            return False
        elif len(board[loc]) == 1:
            val2 = board[loc]
            if not all(self.eliminate(board, loc2, val2) for loc2 in self.peers[loc]):
                return False
        for u in self.units[loc]:
            dplaces = [s for s in u if val in board[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(board, dplaces[0], val):
                    return False
        return board

    def assign(self, board, loc, val):
        other_values = board[loc].replace(val, '')
        if all(self.eliminate(board, loc, val2) for val2 in other_values):
            return board
        else:
            return False

    def initialize(self, spec):
        board = self.empty_board[:]
        for s, d in enumerate(spec):
            if d in all_digits and not self.assign(board, s, d):
                return False
        return board

    def search(self, board):
        if board is False or self.is_solved(board):
            return board
        n, s = min((len(board[s]), s) for s in self.squares if len(board[s]) > 1)
        return some(self.search(self.assign(board[:], s, d))
                    for d in board[s])

    def is_solved(self, board):
        if all(len(v) == 1 for v in board):
            return True
        return False

    def verify(self, board):
        if (not self.is_solved(board) or
                any(board.count(d) != N for d in all_digits) or
                any(set(board[i] for i in idxs) != set(all_digits) for idxs in self.all_idxs)):
            return False
        return True

def read_boards(fh):
    dig_set = set(all_digits + '0')
    boards = []
    for line in fh:
        line = line.strip()
        assert len(line) == N * N
        assert set(line).issubset(dig_set)
        boards.append(line)
    return boards


def main(solver, fname):
    with open(fname, 'r') as fh:
        boards = read_boards(fh)
    times = {}
    solved = {}
    for idx, b in enumerate(boards):
        sys.stderr.write("{} / {}\r".format(idx+1, len(boards)))
        tic = clock()
        ib = solver.initialize(b)
        s = solver.search(ib)
        times[idx] = clock() - tic
        solved[b] = s
    tot_time = sum(times.values())
    median_ms = 1000 * sorted(times.values())[len(times)//2]
    avg_ms = 1000 * tot_time / len(times)
    max_ms = 1000 * max(times.values())
    min_ms = 1000 * min(times.values())
    msg = ("\n{tot_time:4.2f} s total, {avg_ms:3.0f} ms avg, "
    "{median_ms:3.0f} ms median, {max_ms:3.0f} ms max, {min_ms:3.0f} ms min.\n")
    sys.stderr.write(msg.format(**locals()))
    for s in solved.values():
        assert solver.verify(s)

if __name__ == '__main__':
    import sys
    main(ListSudokuSolver(), sys.argv[-1])
    main(DictSudokuSolver(), sys.argv[-1])
