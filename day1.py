import math

def run(input_file: str):
  with open(input_file, "r") as input_file:
    lines = input_file.readlines()

  list_1 = []
  list_2 = []
  counts = {}
  for split_line in [line.split(" ") for line in lines]:
    list_1.append(int(split_line[0]))
    list_2.append(int(split_line[-1]))

    if int(split_line[-1]) in counts:
      counts[int(split_line[-1])] += 1
    else:
      counts[int(split_line[-1])] = 1

  list_1.sort()
  list_2.sort()

  total = 0
  for x, y in zip(list_1, list_2):
    total += abs(x - y)

  print(total)

  part2 = 0
  for x in list_1:
    if x in counts:
      part2 += x*counts[x]

  print(part2)

if __name__ == "__main__":
  run("test/day1")
  run("inputs/day1")