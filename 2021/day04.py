import numpy as np

inp = open("input/inputDay04.txt")
numbers = [int(el) for el in inp.readline().strip().split(",")]
lines = inp.readlines()
boards = []
for idx in range(len(lines) // 6):
    start = 6*idx + 1
    end = 6*(idx+1)
    board = [list(map(int, l.strip().split())) for l in lines[start:end]]
    boards += [np.array(board)]
inp.close()
boards = np.array(boards)
masks = np.zeros_like(boards)

# Part 1
for idx in range(len(numbers)):
    nb = numbers[idx]
    masks[boards == nb] = 1
    horiz = np.any(np.all(masks, axis=1), axis=1)
    vert = np.any(np.all(masks, axis=2), axis=1)
    bingo = horiz + vert
    if any(bingo > 0):
        board_idx = np.where(bingo > 0)[0]
        # print(board_idx, nb)
        board = boards[board_idx][0]
        mask = masks[board_idx][0]
        print(np.sum(board * np.abs(mask - 1)) * nb)
        break

# Part 2
lastboard_score = None; selected_boards = set()
for nb in numbers[idx+1:]:
    masks[boards == nb] = 1
    horiz = np.any(np.all(masks, axis=1), axis=1)
    vert = np.any(np.all(masks, axis=2), axis=1)
    bingo = horiz + vert
    if any(bingo > 0):
        board_idx = np.where(bingo > 0)[0]
        board_idx = [idx for idx in board_idx if idx not in selected_boards]
        if board_idx:
            # print(board_idx, nb)
            board = boards[board_idx][0]
            mask = masks[board_idx][0]
            last_board_score = np.sum(board * np.abs(mask - 1)) * nb
            selected_boards.update(board_idx)
print(last_board_score)