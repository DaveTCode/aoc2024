from dataclasses import dataclass
import re

robot_regex = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

@dataclass
class Robot:
  x: int
  y: int
  dx: int
  dy: int

def safety_score(robots, width, height):
  q1 = q2 = q3 = q4 = 0
  for robot in robots:
    if robot.x == (width - 1) / 2 or robot.y == (height - 1) / 2:
      continue
    elif robot.x < (width - 1) / 2 and robot.y < (height - 1) / 2:
      q1 += 1
    elif robot.x > (width - 1) / 2 and robot.y < (height - 1) / 2:
      q2 += 1
    elif robot.x > (width - 1) / 2 and robot.y > (height - 1) / 2:
      q3 += 1
    elif robot.x < (width - 1) / 2 and robot.y > (height - 1) / 2:
      q4 += 1

  return q1*q2*q3*q4


def run_v2(input_file: str, width: int, height: int, seconds: int):
  with open(input_file) as ifile:
    robot_lines = [l.rstrip() for l in ifile.readlines() if l.rstrip() != ""]

  robots = [Robot(int(robot_regex.match(robot_line).group(1)), 
                  int(robot_regex.match(robot_line).group(2)), 
                  int(robot_regex.match(robot_line).group(3)), 
                  int(robot_regex.match(robot_line).group(4))) for robot_line in robot_lines
  ]

  for i in range(seconds):
    m = [[" " for _ in range(width)] for _ in range(height)]
    overlap_count = 0
    for robot in robots:
      robot.x = (robot.x + robot.dx) % width
      robot.y = (robot.y + robot.dy) % height

      if m[robot.y][robot.x] == "1":
        m[robot.y][robot.x] = str(int(m[robot.y][robot.x]) + 1)
        overlap_count += 1
      else:
        m[robot.y][robot.x] = "1"

    #if overlap_count == 0:
    print("___", i, "____", "\n", "\n".join(["".join(row) for row in m]), "\n\n")


  q = safety_score(robots, width, height)

  print(q)

if __name__ == "__main__":
  #run_v2("test/day14", 11, 7, 100)
  run_v2("inputs/day14", 101, 103, 7700)
