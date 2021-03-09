def play_score(list_player):
  result = 0
  for i in range(0, len(list_player)):
    result += list_player[i] * (len(list_player) - i)
  return result

def part_1(player_1, player_2):
  round = 1
  while len(player_1) != 0 and len(player_2) != 0:
    print("\n-- Round {0} --".format(round))
    round += 1
    print("Player 1's deck:", player_1)
    print("Player 2's deck:", player_2)
    len_1 = len(player_1)
    len_2 = len(player_2)
    play_1 = player_1[0:1][0]
    play_2 = player_2[0:1][0]
    player_1.remove(play_1)
    player_2.remove(play_2)
    
    print("Player 1 plays:", play_1)
    print("Player 2 plays:", play_2)
    if play_2 > play_1: 
      print("Player 2 wins the round!")
      player_2.append(play_2)
      player_2.append(play_1)
    else: 
      print("Player 1 wins the round!")
      player_1.append(play_1)
      player_1.append(play_2)
    print("ok")
  
  print("== Post-game results ==")
  print("Player 1's deck:", player_1)
  print("Player 2's deck:", player_2)

  if len(player_1) == 0:
    return play_score(player_2)
  else:
    return play_score(player_1)


def main():
  # with open("input-day22-example.txt", "r") as file:
  with open("input-day22.txt", "r") as file:
    players = file.read().split("\n\n")
  player_1 = list(map(lambda x: int(x), players[0].split("\n")[1:]))
  player_2 = list(map(lambda x: int(x), players[1].split("\n")[1:]))
  print(player_1)
  print(player_2)
  
  print("Part 1: ", part_1(player_1, player_2))
  
    

if __name__ == "__main__":
  main()
