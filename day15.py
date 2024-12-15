def move_board(board, pos, direction):
  next_pos = pos[0] + direction[0], pos[1] + direction[1]
  new_chr = board[next_pos[1]][next_pos[0]]

  if new_chr == "#": # wall, can't do move
    return False
  elif new_chr == ".": # Space, finish move
    board[next_pos[1]][next_pos[0]] = board[pos[1]][pos[0]]
    board[pos[1]][pos[0]] = "."
    return True
  elif new_chr == "O": # Push box
    if move_board(board, next_pos, direction):
      board[next_pos[1]][next_pos[0]] = board[pos[1]][pos[0]]
      board[pos[1]][pos[0]] = "."
      return True
    else:
      return False
    
  return "WHAT"

def calculate_box_gps(board) -> int:
  total = 0
  for row, line in enumerate(board):
    for col, chr in enumerate(line):
      if chr == "O":
        total += (100 * row) + col

  return total


def run(input_file: str):
  with open(input_file) as ifile:
    lines = [l.rstrip() for l in ifile.readlines()]
    board = [list(l) for l in lines if l.startswith("#")]
    moves = "".join([l for l in lines if l != "" and not l.startswith("#")])

  print(board)
  print(moves)

  robot_pos = (0, 0)
  for row, line in enumerate(lines):
    if "@" in line:
      robot_pos = (line.index("@"), row)

  print(robot_pos)

  for move in moves:
    if move == "<":
      d = (-1, 0)
    elif move == ">":
      d = (1, 0)
    elif move == "^":
      d = (0, -1)
    elif move == "v":
      d = (0, 1)

    if move_board(board, robot_pos, d):
      robot_pos = robot_pos[0] + d[0], robot_pos[1] + d[1]

  print(robot_pos)
  print(calculate_box_gps(board))


if __name__ == "__main__":
  run("test/day15")
  run("inputs/day15")
