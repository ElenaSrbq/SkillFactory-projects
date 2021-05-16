import numpy as np


def game_core_v3(number):
    '''Сравнивается среднее значение предполагаемого промежутка с загаданным.
       Промежуток корректируется в зависимости от того, больше загаданное число или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    upper = 101  # верхняя граница промежутка
    lower = 1  # нижняя граница промежутка
    predict = (upper + lower) // 2
    while number != predict:
        count += 1
        if number > predict:
            lower = predict
        elif number < predict:
            upper = predict
        predict = (upper + lower) // 2
    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)

