from dataclasses import dataclass
from typing import Dict, Set


@dataclass(frozen=True)
class Point:
  x: int
  y: int

  def add(self, p):
    return Point(self.x + p.x, self.y + p.y)
  
  def inside(self, field):
    return self.x >= 0 and self.x < len(field[0]) and self.y >= 0 and self.y < len(field)

  def __repr__(self):
    return f"({self.x}, {self.y})"

DIRS = [Point(-1, 0), Point(1, 0), Point(0, 1), Point(0, -1)]

@dataclass
class Region:
  letter: chr
  points: Set[Point]
  edges: Dict[Point, Set[Point]]

  def cost_p1(self):
    return len(self.edges) * len(self.points)
  
  def cost_p2(self):
    return count_sides(self.edges) * len(self.points)

def expand_region(region: Region, p: Point, cell_to_region, field):
  if field[p.y][p.x] != region.letter:
    return

  for dir in DIRS:
    p2 = p.add(dir)

    if p2.inside(field):
      if field[p2.y][p2.x] == region.letter:
        if p2 not in cell_to_region:
          cell_to_region[p2] = region
          region.points.add(p2)
          expand_region(region, p2, cell_to_region, field)
      else:
        edges = region.edges.get(dir, set())
        edges.add(p)
        region.edges[dir] = edges
    else:
      edges = region.edges.get(dir, set())
      edges.add(p)
      region.edges[dir] = edges

def count_sides(region: Region):
  curr_point = region.points[0]

  for dir in DIRS:
    next_point = point

def run(input_file: str):
  with open(input_file) as ifile:
    field = [list(line) for line in [l.rstrip() for l in ifile.readlines()]]

  regions = []
  cell_to_region = {}

  for y, row in enumerate(field):
    for x, cell in enumerate(row):
      p = Point(x, y)
      if p not in cell_to_region:
        new_region = Region(cell, set([p]), {})
        cell_to_region[p] = new_region
        expand_region(new_region, p, cell_to_region, field)
        regions.append(new_region)

  print(sum([r.cost_p1() for r in regions]))
  print(sum([r.cost_p2() for r in regions]))

if __name__ == "__main__":
  run("test/day12")
  #run("inputs/day12")
