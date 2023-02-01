# There is no Block scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


def create_enemy():
    enemies_1 = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy_1 = enemies_1[0]

    print(new_enemy_1)

create_enemy()
