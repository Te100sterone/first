list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players = len(list_players)
count_players_in_team = int(count_players // 2)
list_players_1 = list_players[:count_players_in_team:1]
list_players_2 = list_players[count_players_in_team::1]
print(list_players_1)
print(list_players_2)
