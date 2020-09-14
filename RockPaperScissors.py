import random
taro = random.choice(range(0, 3))
hanako = random.choice(range(0, 3))

WinOrLose = ["Taro's victory", "Hanako's victory", "draw"]

WinOrLoseTable = [[2, 0, 1], [1, 2, 0], [0, 1, 2]]

def janken(taro, hanako):
    print(WinOrLose[WinOrLoseTable[taro][hanako]])

janken(taro, hanako)