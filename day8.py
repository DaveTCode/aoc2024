def p1_points(location, second_location, width, height):
  points = []
  d_x = abs(location[0] - second_location[0])
  d_y = abs(location[1] - second_location[1])

  if location[0] <= second_location[0] and location[1] <= second_location[1]:
    p1 = (location[0] - d_x, location[1] - d_y)
    p2 = (second_location[0] + d_x, second_location[1] + d_y)
  elif location[0] > second_location[0] and location[1] <= second_location[1]:
    p1 = (location[0] + d_x, location[1] - d_y)
    p2 = (second_location[0] - d_x, second_location[1] + d_y)

  for p in [p1, p2]:
    if p[0] >= 0 and p[1] >= 0 and p[0] < width and p[1] < height:
      points.append(p)

  return points

def all_points_from_line_in_map(location, second_location, width, height):
  points = [location, second_location]
  d_x = abs(location[0] - second_location[0])
  d_y = abs(location[1] - second_location[1])

  if location[0] <= second_location[0] and location[1] <= second_location[1]:
    p1 = (location[0] - d_x, location[1] - d_y)
    p2 = (second_location[0] + d_x, second_location[1] + d_y)

    more = True
    while more:
      more = False
      for p in [p1, p2]:
        if p[0] >= 0 and p[1] >= 0 and p[0] < width and p[1] < height:
          points.append(p)
          more = True

      p1 = (p1[0] - d_x, p1[1] - d_y)
      p2 = (p2[0] + d_x, p2[1] + d_y)
  elif location[0] > second_location[0] and location[1] <= second_location[1]:
    p1 = (location[0] + d_x, location[1] - d_y)
    p2 = (second_location[0] - d_x, second_location[1] + d_y)

    more = True
    while more:
      more = False
      for p in [p1, p2]:
        if p[0] >= 0 and p[1] >= 0 and p[0] < width and p[1] < height:
          points.append(p)
          more = True

      p1 = (p1[0] + d_x, p1[1] - d_y)
      p2 = (p2[0] - d_x, p2[1] + d_y)

  return points

def run(input_file: str):
  with open(input_file) as ifile:
    map = [list(line.rstrip()) for line in ifile.readlines()]

  antennas = {}
  for y, row in enumerate(map):
    for x, col in enumerate(row):
      if col != ".":
        frequency_antennas = antennas.get(col, [])
        frequency_antennas.append((x, y))
        antennas[col] = frequency_antennas

  part_1_antinodes = set()
  part_2_antinodes = set()
  for _, locations in antennas.items():
    for ix, location in enumerate(locations):
      for second_location in locations[ix+1:]:
        part_1_antinodes = part_1_antinodes.union(p1_points(location, second_location, len(map[0]), len(map)))
        part_2_antinodes = part_2_antinodes.union(all_points_from_line_in_map(location, second_location, len(map[0]), len(map)))

  print(len(part_1_antinodes))
  print(len(part_2_antinodes))


if __name__ == "__main__":
  run("test/day8")
  run("input/day8")
