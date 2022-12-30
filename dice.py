import random

N = int(input("Number of players? "))
M = int(input("Number of dice for every player? "))
print(f"Player = {N}, Dice = {M}")

def dice_game(num_players, num_dice):
    players = []
    minus = []
    plus = []
    ingame = num_players
    turn = 1

    for i in range(num_players):
        players.append({"id": i+1, "dice": num_dice, "points": 0})
        minus.append(0)
        plus.append(0)

    while ingame > 1:
        print("=" * 20)
        print(f"Turn {turn} roll the dice: ", end="")

        for player in players:
            print(f"\nPlayer #{player['id']} ({player['points']}): ", end="")
            dicemin = 0
            diceplus = 0

            for i in range(player['dice']):
                roll = random.randint(1, 6)
                
                if i != player['dice'] - 1:
                    print(f"{roll},", end="")
                else :
                    print(f"{roll}", end="")
                    
                if roll == 6:
                    player["points"] += 1
                    dicemin += 1
                elif roll == 1:
                    diceplus += 1
                    dicemin += 1
            
            player_index = player['id'] - 1
            minus[player_index] = dicemin
            plus[player_index] = diceplus
        
        print("")
        print("=" * 20)
        input("\nClick enter to continue")

        for player in players:
            player_index = player['id'] - 1
            player['dice'] -= minus[player_index]
            next_player_index = (players.index(player) + 1) % len(players)
            if players[next_player_index]['dice'] != 0:
                players[next_player_index]['dice'] += plus[player_index]
        
        turn += 1

        dices = []
        for player in players:
            dices.append(player['dice'])
        lose = dices.count(0)
        ingame = num_players - lose
    
    score = []
    for player in players:
        score.append(player['points'])

    winning = max(score)
    index = [index for index in range(len(score)) if score[index] == winning]
    
    if len(index) == 1:
        for i in index:
            index = i
        return players[index]
    else:
        return "tie"
        
winner = dice_game(N, M)
if winner != "tie":
    print(f"Player {winner['id']} won with {winner['points']} points!")
else :
    print(f"It's a Tie!")
