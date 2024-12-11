import functools

@functools.cache
def blink_at_stone(stone: int, blinks_left: int) -> int:
  if blinks_left == 0:
    return 1
  
  if stone == 0:
    result = blink_at_stone(1, blinks_left - 1)
  elif len(str(stone)) & 1 == 0:
    digits = list(str(stone))
    left = int("".join(digits[:len(digits)//2]))
    right = int("".join(digits[len(digits)//2:]))

    result = blink_at_stone(left, blinks_left - 1) + blink_at_stone(right, blinks_left - 1)
  else:
    result = blink_at_stone(stone * 2024, blinks_left - 1)

  return result

def run(input_file: str):
  with open(input_file) as ifile:
    stones = [int(s) for s in ifile.readline().rstrip().split(" ") if s != ""]

  part_1_result = 0
  part_2_result = 0
  for stone in stones:
    part_1_result += blink_at_stone(stone, 25)
    part_2_result += blink_at_stone(stone, 75)

  print("part 1:", part_1_result)
  print("part 2:", part_2_result)

if __name__ == "__main__":
  run("test/day11")
  run("inputs/day11")
