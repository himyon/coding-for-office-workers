import random
game_1 = input("가위, 바위, 보 중 어떤것을 내시겠습니까? ")

game = ("가위", "바위", "보")
print(random.choice(game))

a = 0
b = 0
if game_1 == "가위" and game == "바위":
    b = 1
print(a, b)


# elif game_1 =="가위" and game =="보":
#     a + 1
# print(a, b)


# 가위 = 바위 1
# 가위 = 보 1
#
# 바위 = 바위 0
# 바위 = 가위 1
# 바위 = 보 1
#
# 보 = 보 0
# 보 = 바위 1
# 보 = 가위 1

# print("{} vs {}".format(game, game))
