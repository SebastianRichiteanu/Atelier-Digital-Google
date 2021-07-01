import copy

print("Memory Savers")
print("-" * 80)

my_lambda = lambda x, y: x + y
my_sum = my_lambda(2, 3)
print(my_sum)

players = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "rank": 6
    },
    {
        "first_name": "Kevin",
        "last_name": "McDonald",
        "rank": 22
    },
    {
        "first_name": "Brad",
        "last_name": "Kelvin",
        "rank": 2
    }
]

print(players)
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player['is top 3'] = player['rank'] <= 3
    return updated_player


top_player = list(map(check_top_3_player, players))
print(top_player)

all_mcdonalds = list(filter(lambda player: player["last_name"] == "McDonald", players))
print(all_mcdonalds)

letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]

print(zip(letters, numbers))
for l, nr in zip(letters, numbers):
    print(nr, l)

my_numbers = [1, 2, 3, 4, 5]

even_squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
print(even_squared_numbers)
