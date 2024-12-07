def reduce_result_p2(target, result, remainder):
  if len(remainder) == 0:
    return target == result
  else:
    return \
     reduce_result_p2(target, result + int(remainder[0]), remainder[1:]) or \
     reduce_result_p2(target, result * int(remainder[0]), remainder[1:]) or \
     reduce_result_p2(target, int(str(result) + str(int(remainder[0]))), remainder[1:])

def reduce_result(target, result, remainder):
  if len(remainder) == 0:
    return target == result
  else:
    return \
     reduce_result(target, result + int(remainder[0]), remainder[1:]) or \
     reduce_result(target, result * int(remainder[0]), remainder[1:])


def run(input_file: str):
  with open(input_file) as ifile:
    lines = ifile.readlines()

  part_1_total = 0
  part_2_total = 0
  for line in lines:
    target = int(line.split(":")[0])
    parts = [int(p) for p in line.rstrip().split(":")[1].lstrip().split(" ")]

    if reduce_result(target, parts[0], parts[1:]):
      part_1_total += target

    if reduce_result_p2(target, parts[0], parts[1:]):
      part_2_total += target

  print(part_1_total)
  print(part_2_total)

if __name__ == "__main__":
  run("test/day7")
  run("input/day7")
