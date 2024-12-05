def run(input_file: str):
  with open(input_file) as ifile:
    lines = ifile.readlines()

  before_rules = {}
  for line in lines:
    if "|" in line: # rule line
      parts = line.split("|")
      before, after = int(parts[0]), int(parts[1])
      
      if not before in before_rules:
        before_rules[before] = []

      before_rules[before].append(after)

  updates = [[int(n) for n in line.split(",")] for line in lines if "," in line]

  part_1_count = 0
  part_2_count = 0
  for update in updates:
    bad = False
    updating = True
    print(update)
    while updating:
      updating = False
      for ix in range(len(update)):
        val = update[ix]
        for check in before_rules.get(val, []):
          if check in update[:ix]:
            bad = True
            updating = True
            update[update.index(check)] = val
            update[ix] = check
            break
        
        if updating:
          break
    
    print(update)
    if not bad:
      part_1_count += update[int((len(update) - 1) / 2)]
    else:
      part_2_count += update[int((len(update) - 1) / 2)]


  print(part_1_count)
  print(part_2_count)

if __name__ == "__main__":
  run("test/day5")
  run("input/day5")
