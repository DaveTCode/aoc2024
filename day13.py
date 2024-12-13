import math
import re

button_regex = re.compile("Button \w+: X\+(\d+), Y\+(\d+)")
target_regex = re.compile("Prize: X=(\d+), Y=(\d+)")


def run(input_file: str, factor):
  with open(input_file) as ifile:
    lines = [l.rstrip() for l in ifile.readlines() if l.rstrip() != ""]

  machines = [lines[x:x+3] for x in range(0, len(lines), 3)]

  score=0
  for machine in machines:
    bam = button_regex.match(machine[0])
    bbm = button_regex.match(machine[1])
    tm = target_regex.match(machine[2])
    (a,c) = (int(bam.groups()[0]), int(bam.groups()[1]))
    (b,d) = (int(bbm.groups()[0]), int(bbm.groups()[1]))
    (r1, r2) = (int(tm.groups()[0]) + factor, int(tm.groups()[1]) + factor)

    lcm = math.lcm(a, c)
    y = ((r1 * (lcm / a)) - (r2 * (lcm / c))) / ((b * (lcm / a)) - (d * (lcm / c)))
    x = (r1 - (b * y)) / a
    
    if x.is_integer() and y.is_integer():
      score += x * 3 + y

  print(score)

if __name__ == "__main__":
  run("test/day13", 0)
  run("inputs/day13", 0)

  run("test/day13", 10000000000000)
  run("inputs/day13", 10000000000000)
