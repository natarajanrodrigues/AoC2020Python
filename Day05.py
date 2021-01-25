with open("input-day05.txt", "r") as file:
# with open("input-day05-example.txt", "r") as file:
  entries = [line[:-1] for line in file.readlines()]  


def seat_id (boarding_pass):
  return int( ( seat_id_decode(boarding_pass[0:7], 'F', 128) * 8 ) + seat_id_decode(boarding_pass[7:], 'L',  8))

def seat_id_decode(sequence, left_char, num_slots):
  limit_l = 0;
  limit_r = num_slots - 1;
  half = num_slots / 2

  for i in sequence:
    if (i == left_char):
      limit_r = limit_r - half
    else:
      limit_l = limit_l + half
    half /= 2
  
  if (limit_l < limit_r):
    return limit_l
  return limit_r


def part_2(entries):
  board_list = list(map(lambda x : seat_id(x), entries))
  max_seat = max(board_list)
  min_seat = min(board_list)
  for i in range(min_seat, max_seat):
    if i not in board_list and i - 1 in board_list and i + 1 in board_list:
      return i



# Part1
print("Result 1: ", max(list(map(lambda x : seat_id(x), entries))) )



# Part2
print("Result 2: ", part_2(entries)) 


