def run(input_file: str):
  with open(input_file) as ifile:
    lines = ifile.readlines()

  part_1_count = 0
  part_2_count = 0
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if lines[row][col] == "X":
        possibles = []

        if row >= 3: # Up direction
          possibles.append([lines[row][col], lines[row-1][col], lines[row-2][col], lines[row-3][col]])

          if col >= 3: # Up&Left direction
            possibles.append([lines[row][col], lines[row-1][col-1], lines[row-2][col-2], lines[row-3][col-3]])
          if col <= len(lines[row])-4: # Up&Right direction
            possibles.append([lines[row][col], lines[row-1][col+1], lines[row-2][col+2], lines[row-3][col+3]])
        if row <= len(lines) - 4: # Down direction
          possibles.append([lines[row][col], lines[row+1][col], lines[row+2][col], lines[row+3][col]])

          if col >= 3: # Down&Left direction
            possibles.append([lines[row][col], lines[row+1][col-1], lines[row+2][col-2], lines[row+3][col-3]])
          if col < len(lines[row])-4: # Down&Right direction
            possibles.append([lines[row][col], lines[row+1][col+1], lines[row+2][col+2], lines[row+3][col+3]])
        if col >= 3: # Left direction
          possibles.append([lines[row][col], lines[row][col-1], lines[row][col-2], lines[row][col-3]])
        if col <= len(lines[row])-4: # Right direction
          possibles.append([lines[row][col], lines[row][col+1], lines[row][col+2], lines[row][col+3]])
        
        #print(possibles)
        for possible in possibles:
          if "".join(possible) == "XMAS":
            part_1_count += 1
      elif lines[row][col] == "A" and row > 0 and row < len(lines) - 1 and col > 0 and col < len(lines[row]) - 1:
        diag1 = (lines[row-1][col-1] == "M" and lines[row+1][col+1] == "S") or (lines[row-1][col-1] == "S" and lines[row+1][col+1] == "M")
        diag2 = (lines[row+1][col-1] == "M" and lines[row-1][col+1] == "S") or (lines[row+1][col-1] == "S" and lines[row-1][col+1] == "M")

        if diag1 and diag2:
          part_2_count += 1

  print(part_1_count)
  print(part_2_count)

if __name__ == "__main__":
  run("test/day4")
  run("inputs/day4")
