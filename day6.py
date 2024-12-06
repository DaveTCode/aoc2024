def count_steps(x, y, direction, room):
  guard = (x, y)
  visited_positions = set()
  direction = 0
  while True:
    if (len(visited_positions) > 100000):
      print(x,y," Maybe broken")
      break
    if (guard, direction) in visited_positions:
      return -1 # Loop
    
    visited_positions.add((guard, direction))

    if direction == 0: # Up
      new_guard = guard[0], guard[1] - 1
    elif direction == 1: # Right
      new_guard = guard[0] + 1, guard[1]
    elif direction == 2: # Down
      new_guard = guard[0], guard[1] + 1
    elif direction == 3: # Left
      new_guard = guard[0] - 1, guard[1]
    
    # Have we left the map? time to stop?
    if new_guard[0] < 0 or new_guard[0] >= len(room[0]) or new_guard[1] < 0 or new_guard[1] >= len(room):
      break

    # Is the new position already occupied?
    if room[new_guard[1]][new_guard[0]] == "#":
      new_guard = guard
      direction = (direction + 1) % 4
    else:
      guard = new_guard
  
  return len(set([pos[0] for pos in visited_positions]))


def run(input_file: str):
  with open(input_file) as ifile:
    lines = ifile.readlines()

  # Find the initial position
  for ix, line in enumerate(lines):
    if "^" in line:
      guard = (line.find("^"), ix)
      break

  fullmap = [list(line.rstrip()) for line in lines]
  part_1 = count_steps(guard[0], guard[1], 0, fullmap)

  loops = 0
  for row, line in enumerate(lines):
    print("Starting row ", row)
    for col, cell in enumerate(lines[row]):
      if cell == ".":
        fullmap[row][col] = "#"
        if count_steps(guard[0], guard[1], 0, fullmap) == -1:
          loops += 1
        fullmap[row][col] = "."

  print(part_1)
  print(loops)

if __name__ == "__main__":
  run("test/day6")
  run("input/day6")
