def count_trails(topo, ends, x: int, y: int, cell: int):
  if cell == 9:
    ends.add((x, y))
    return 1
  
  trails = 0
  for d_x, d_y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
    new_x = x + d_x
    new_y = y + d_y
    if new_x >= 0 and new_x < len(topo[0]) and new_y >= 0 and new_y < len(topo):
      if topo[new_y][new_x] == cell + 1:
        trails += count_trails(topo, ends, new_x, new_y, cell + 1)

  return trails

def run(input_file: str):
  with open(input_file) as ifile:
    topo = [[int(c) for c in l.rstrip()] for l in ifile.readlines()]

  part_1_count = 0
  part_2_count = 0
  for y, row in enumerate(topo):
    for x, cell in enumerate(row):
      if cell == 0:
        ends = set()
        trail_count = count_trails(topo, ends, x, y, cell)
        part_1_count += len(ends)
        part_2_count += trail_count

  print(part_1_count)
  print(part_2_count)


if __name__ == "__main__":
  run("test/day10")
  run("inputs/day10")
