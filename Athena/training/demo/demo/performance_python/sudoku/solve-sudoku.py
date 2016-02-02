import sys
import numpy as np
from time import clock
from copy import copy

use_dict = False

N = 9
all_digits = '123456789'

def setup_globals_list():
    squares = range(N*N)
    empty_board = [all_digits] * (N * N)
    # empty_board = np.array([all_digits] * (N * N))

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

    return squares, empty_board, units, peers, all_idxs

def setup_globals_dict():
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
    return squares, empty_board, units, peers, unitlist

setup_globals = setup_globals_dict if use_dict else setup_globals_list

squares, empty_board, units, peers, all_idxs = setup_globals()

def assign(board, loc, val):
    other_values = board[loc].replace(val, '')
    if all(eliminate(board, loc, val2) for val2 in other_values):
        return board
    else:
        return False

def eliminate(board, loc, val):
    if val not in board[loc]:
        return board
    board[loc] = board[loc].replace(val, '')
    if len(board[loc]) == 0:
        return False
    elif len(board[loc]) == 1:
        val2 = board[loc]
        if not all(eliminate(board, loc2, val2) for loc2 in peers[loc]):
            return False
    for u in units[loc]:
        dplaces = [s for s in u if val in board[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(board, dplaces[0], val):
                return False
    return board

def str_from_board(b):
    return ''.join(b)

def is_solved(board):
    if all(len(v) == 1 for v in board):
        return True
    return False

def is_solved_dict(board):
    if all(len(v) == 1 for v in board.values()):
        return True
    return False

if use_dict:
    is_solved = is_solved_dict

def initialize(spec, use_dict=False):
    board = copy(empty_board)
    for s, d in enumerate(spec):
        if use_dict:
            s = squares[s]
        if d in all_digits and not assign(board, s, d):
            return False
    return board

def read_boards(fh):
    dig_set = set(all_digits + '0')
    boards = []
    for line in fh:
        line = line.strip()
        assert len(line) == N * N
        assert set(line).issubset(dig_set)
        boards.append(line)
    return boards

def verify(board):
    if (not is_solved(board) or
            any(board.count(d) != N for d in all_digits) or
            any(set(board[i] for i in idxs) != set(all_digits) for idxs in all_idxs)):
        return False
    return True

def search(board):
    if board is False or is_solved(board):
        return board
    n, s = min((len(board[s]), s) for s in squares if len(board[s]) > 1)
    return some(search(assign(copy(board), s, d))
                for d in board[s])

def some(seq):
    for e in seq:
        if e: return e
    return False

def main(fname):
    with open(fname, 'r') as fh:
        boards = read_boards(fh)
    times = {}
    solved = {}
    for idx, b in enumerate(boards):
        sys.stderr.write("{} / {}\r".format(idx+1, len(boards)))
        tic = clock()
        s = search(initialize(b, True))
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
        assert verify(s)

if __name__ == '__main__':
    import sys
    main(sys.argv[-1])
