import re

def run(input_file: str):
  with open(input_file) as ifile:
    input = "".join(ifile.readlines())

  part_1_total = 0
  part_2_total = 0

  for mul_instr in re.finditer("mul\((\d+),(\d+)\)", input):
    mul = int(mul_instr.group(1)) * int(mul_instr.group(2))
    part_1_total += mul

    last_do = input.rfind("do()", 0, mul_instr.start())
    last_dont = input.rfind("don't()", 0, mul_instr.start())

    if last_do > last_dont or (last_do == -1 and last_dont == -1):
      part_2_total += mul

  print(part_1_total)
  print(part_2_total)

if __name__ == "__main__":
  run("test/day3")
  run("inputs/day3")
