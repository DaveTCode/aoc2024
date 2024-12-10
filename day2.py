def check_parts(parts):
  increasing = parts[0] < parts[1]

  safe = True
  compare_part = parts[0]
  for part in parts[1:]:
    if increasing:
      if compare_part < part and part - compare_part < 4:
        compare_part = part
      else:
        safe = False
        break
    else:
      if compare_part > part and compare_part - part < 4:
        compare_part = part
      else:
        safe = False
        break

  return safe

def run(input_file: str):
  with open(input_file) as day2:
    lines = day2.readlines()

  count_part_1 = 0
  count_part_2 = 0
  for line in lines:
    parts = [int(p) for p in line.split(" ")]

    all_safe = check_parts(parts)
      
    if all_safe:
      count_part_1 += 1
      count_part_2 += 1
    else:
      for i in range(0, len(parts)):
        if check_parts(parts[:i] + parts[i+1:]):
          count_part_2 += 1
          break

  print(count_part_1)
  print(count_part_2)


if __name__ == "__main__":
  run("test/day2")
  run("inputs/day2")