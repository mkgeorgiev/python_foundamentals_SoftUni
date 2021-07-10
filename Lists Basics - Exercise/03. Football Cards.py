referee_cards = input().split()
a_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a_team_red_card = False
b_team_red_card = False
game_terminated = False
for team_player_number in range(len(referee_cards)):
    team_number = referee_cards[team_player_number].split("-")
    for element in range(len(team_number)):
        if team_number[element] == "A":
            a_team_red_card = True
        elif team_number[element] == "B":
            b_team_red_card = True
        else:
            if a_team_red_card:
                if int(team_number[element]) in a_team:
                    a_team.remove(int(team_number[element]))
                a_team_red_card = False
            elif b_team_red_card:
                if int(team_number[element]) in b_team:
                    b_team.remove(int(team_number[element]))
                b_team_red_card = False
    if len(a_team) <7 or len(b_team) < 7:
        game_terminated = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if game_terminated:
    print("Game was terminated")