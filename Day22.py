import copy

def play_score(list_player):
  result = 0
  for i in range(0, len(list_player)):
    result += list_player[i] * (len(list_player) - i)
  return result

def part_1(player_1, player_2):
  round = 1
  while len(player_1) != 0 and len(player_2) != 0:
    # print("\n-- Round {0} --".format(round))
    round += 1
    # print("Player 1's deck:", player_1)
    # print("Player 2's deck:", player_2)
    len_1 = len(player_1)
    len_2 = len(player_2)
    play_1 = player_1[0:1][0]
    play_2 = player_2[0:1][0]
    player_1.remove(play_1)
    player_2.remove(play_2)
    
    # print("Player 1 plays:", play_1)
    # print("Player 2 plays:", play_2)
    if play_2 > play_1: 
      # print("Player 2 wins the round!")
      player_2.append(play_2)
      player_2.append(play_1)
    else: 
      # print("Player 1 wins the round!")
      player_1.append(play_1)
      player_1.append(play_2)
    # print("ok")
  
  # print("== Post-game results ==")
  # print("Player 1's deck:", player_1)
  # print("Player 2's deck:", player_2)

  if len(player_1) == 0:
    return play_score(player_2)
  else:
    return play_score(player_1)

def play_game(player_1, player_2, game_number, game_number_origin, next_game):

  # print("\n=== Game {0} ===".format(game_number))
  round = 0
  
  cache_game_p1 = []
  cache_game_p2 = []
  
  while len(player_1) != 0 and len(player_2) != 0:

    # Avoid Loop Rule
    if player_1 in cache_game_p1 and player_2 in cache_game_p2:
      return 1

    cache_game_p1.append(copy.deepcopy(player_1))
    cache_game_p2.append(copy.deepcopy(player_2))
    

    round += 1
    # print("\n-- Round {0} (Game {1}) --".format(round, game_number))
    # print("Player 1's deck:", player_1)
    # print("Player 2's deck:", player_2)
    len_1 = len(player_1)
    len_2 = len(player_2)
    play_1 = player_1[0:1][0]
    play_2 = player_2[0:1][0]
    player_1.remove(play_1)
    player_2.remove(play_2)
    
    # print("Player 1 plays:", play_1)
    # print("Player 2 plays:", play_2)

    if play_1 <= len(player_1) and play_2 <= len(player_2):
      # print("Playing a sub-game to determine the winner...")
      
      next_game += 1
      results = play_game(player_1[:play_1], player_2[:play_2], next_game, game_number, next_game)

      winner = results
      if winner == 2:
        # print("Player 2 wins round {0} of game {1}!".format(round, game_number))
        player_2.append(play_2)
        player_2.append(play_1)  
      elif winner == 1:
        # print("Player 1 wins round {0} of game {1}!".format(round, game_number))
        player_1.append(play_1)
        player_1.append(play_2)
      else:
        return results
    else: 
      if play_2 > play_1: 
        # print("Player 2 wins round {0} of game {1}!".format(round, game_number))
        player_2.append(play_2)
        player_2.append(play_1)
      else: 
        # print("Player 1 wins round {0} of game {1}!".format(round, game_number))
        player_1.append(play_1)
        player_1.append(play_2)
    # print("")
  
  if game_number != 1: 
    if len(player_1) == 0:
      # print("The winner of game {0} is player 2!\n".format(game_number))
      # print("...anyway, back to game {0}.".format(game_number_origin))
      return 2
    else:
      # print("The winner of game {0} is player 1!\n".format(game_number))
      # print("...anyway, back to game {0}.".format(game_number_origin))
      return 1
  else:
    if len(player_1) == 0:
      return play_score(player_2)
    else:
      return play_score(player_1)



def part_2(player_1, player_2):
  
  return play_game(player_1, player_2, 1, 1, 1)
  
    


def main():
  # with open("input-day22-example.txt", "r") as file:
  with open("input-day22.txt", "r") as file:
    players = file.read().split("\n\n")
  player_1 = list(map(lambda x: int(x), players[0].split("\n")[1:]))
  player_2 = list(map(lambda x: int(x), players[1].split("\n")[1:]))
  print(player_1)
  print(player_2)
  
  print("Part 1: ", part_1(copy.deepcopy(player_1), copy.deepcopy(player_2)))
  print("Part 2: ", part_2(copy.deepcopy(player_1), copy.deepcopy(player_2)))
  
    

if __name__ == "__main__":
  main()
