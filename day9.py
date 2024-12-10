def decompress(input: str):
  result = []

  for ix, chr in enumerate(input):
    if ix & 1 == 0:
      result.extend([int(ix / 2)] * int(chr))
    else:
      result.extend(["."] * int(chr))

  return result

def defrag_p1(decompressed):
  result = [x for x in decompressed]
  fwd_ptr = 0
  bk_ptr = len(result) - 1
  while bk_ptr > fwd_ptr:
    if result[bk_ptr] == ".":
      bk_ptr-=1
    elif result[fwd_ptr] != ".":
      fwd_ptr += 1
    else:
      result[fwd_ptr] = result[bk_ptr]
      result[bk_ptr] = "."

  return result

def defrag_p2(decompressed):
  result = [x for x in decompressed]
  bk_ptr = len(result) - 1
  current_id = -1
  current_id_blk_size = 0

  for bk_ptr in range(len(result) - 1, 0, -1):
    if current_id != -1 and current_id != result[bk_ptr]:
      #print("Trying to move ", current_id, bk_ptr + 1, current_id_blk_size)
      for fwd_ptr in range(0, bk_ptr+1):
        if result[fwd_ptr] == ".":
          ok = True
          for i in range(fwd_ptr, fwd_ptr + current_id_blk_size):
            if result[i] != ".":
              ok = False
              break

          if ok:
            # Put new entries in
            for i in range(fwd_ptr, fwd_ptr + current_id_blk_size):
              result[i] = current_id
            # Clear old entries
            for i in range(bk_ptr + 1, bk_ptr + current_id_blk_size + 1):
              result[i] = "."
            
            break
    
    if result[bk_ptr] != ".":
      if current_id != result[bk_ptr]:
        current_id = result[bk_ptr]
        current_id_blk_size = 1
      else:
        current_id_blk_size += 1
    else:
      current_id = -1
      current_id_blk_size = 0

  return result

def checksum(l):
  result = 0
  for ix, n in enumerate(l):
    if n != ".":
      result += ix*n

  return result

def run(input_file: str):
  with open(input_file) as ifile:
    input = ifile.readline()

  decompressed = decompress(input)
  print(checksum(defrag_p1(decompressed)))
  print(checksum(defrag_p2(decompressed)))


if __name__ == "__main__":
  run("test/day9")
  run("inputs/day9")
