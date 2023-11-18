import copy

place = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


def choose(x, y):
    while y[0] < 0 or y[1] < 0 or 7 < y[0] or 7 < y[1]:
        h = str(input('На какую координату сходить?\n Ввод: ')).split(' ')
        x[0] = int(h[0])
        x[1] = int(h[1])
        y[0] = x[1] - 1
        y[1] = x[0] - 1
        # print(y)
    return x, y


def main(input_cords, chip, revers_chip):
    first_cords = [0, 0]
    second_cords = [0, 10]
    need_count = 64
    place_view = ''
    count = 0
    cont = True
    check = 0
    count_first = 0
    count_second = 0
    text = ''
    # text_cords = str(text_cords).split(' ')

    first_cords[0] = input_cords[0]
    first_cords[1] = input_cords[1]
    second_cords[0] = input_cords[0]
    second_cords[1] = input_cords[1]

    # if second_cords[0] < 0 or second_cords[0] > 7 or\
    #         second_cords[1] < 0 or second_cords[1] > 7 or\
    #         place[second_cords[0]][second_cords[1]] == chip:
    #     print('check cords')
    #     return place, f'Wrong cords, player {chip}', chip, revers_chip, cont
    # check += 1
    # for i in range(8):
    #     place_view += ''.join(str(place[7 - i]).replace(','" ", '')).strip("['']") + '\n'
    # print(place_view)

    previous_place = copy.deepcopy(place)
    print(previous_place)
    move_algorithm(chip, revers_chip, second_cords)
    print(previous_place)
    if place == previous_place:
        text = f'Wrong cords, another {"second" if chip == 2 else "first"} player turn!'
        return place, text, chip, revers_chip, cont

    if chip == 1:
        text = 'Second player turn'
    if chip == 2:
        text = 'First player turn'
    # choose(first_cords, second_cords)
    print(second_cords)

    for i in range(8):
        for j in range(8):
            if place[i][j] == 1 or place[i][j] == 2:
                count += 1
    if count == need_count:
        # print('check1')
        for i in range(8):
            for j in range(8):
                if place[i][j] == 1:
                    count_first += 1
                if place[i][j] == 2:
                    count_second += 1
        # print(place_view)
        # print(count_first, count_second)
        if count_first < count_second:
            print('Second player win')
            cont = False
            text = 'Game over Second player win'
            return place, text, chip, revers_chip, cont
        else:
            print('First player win')
            cont = False
            text = 'Game over First player win'
            return place, text, chip, revers_chip, cont

    if chip != 0:
        if chip == 1:
            chip = 2
            revers_chip = 1
            # return chip, revers_chip
        else:
            chip = 1
            revers_chip = 2
            # return chip, revers_chip
    # second_cords = [0, 10]
    # place_view = ''
    # print('place')
    return place, text, chip, revers_chip, cont


def move_algorithm(x, y, second_cords):
    cord_memory = []

    if place[second_cords[0]][second_cords[1]] == 0:
        print('here cords= ', second_cords)
        # left bottom
        if 0 <= second_cords[0] - 1 <= 7 and 0 <= second_cords[1] - 1 <= 7 and \
                place[second_cords[0] - 1][second_cords[1] - 1] == y:
            print('check left bottom')
            for i in range(1, 8):
                if 0 <= second_cords[0] - 1 - i <= 7 and 0 <= second_cords[1] - 1 - i <= 7:       # Начинаем заполнять клетки,
                    if place[second_cords[0] - 1 - i][second_cords[1] - 1 - i] == x:     # которые запомнили
                        for j in range(0, len(cord_memory), 2):                             # + начальную клетку
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0]][second_cords[1]] = x
                        place[second_cords[0] - 1][second_cords[1] - 1] = x
                        break
                    else:
                        cord_memory.append(second_cords[0] - 1 - i)
                        cord_memory.append(second_cords[1] - 1 - i)
                else:
                    cord_memory = []
                    break

        # mid bottom
        if 0 <= second_cords[0] - 1 <= 7 and 0 <= second_cords[1] <= 7 and \
                place[second_cords[0] - 1][second_cords[1]] == y:
            print('check mid bottom')
            for i in range(1, 8):
                if 0 <= second_cords[0] - 1 - i <= 7 and 0 <= second_cords[1] <= 7:       # Начинаем заполнять клетки,
                    if place[second_cords[0] - 1 - i][second_cords[1]] == x:                # которые запомнили
                        for j in range(0, len(cord_memory), 2):                             # + начальную клетку
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0]][second_cords[1]] = x
                        place[second_cords[0] - 1][second_cords[1]] = x
                        # print(second_cords, second_cords[0] - 1, second_cords[1])
                        break
                    else:
                        cord_memory.append(second_cords[0] - 1 - i)
                        cord_memory.append(second_cords[1])
                        # print(cord_memory)
                else:
                    cord_memory = []
                    break

        # right bottom
        if 0 <= second_cords[0] - 1 <= 7 and 0 <= second_cords[1] + 1 <= 7 and \
                place[second_cords[0] - 1][second_cords[1] + 1] == y:
            print('check right bottom')
            for i in range(1, 8):
                if 0 <= second_cords[0] - 1 - i <= 7 and 0 <= second_cords[1] + 1 + i <= 7:
                    if place[second_cords[0] - 1 - i][second_cords[1] + 1 + i] == x:
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0]][second_cords[1]] = x
                        place[second_cords[0] - 1][second_cords[1] + 1] = x
                        break
                    else:
                        cord_memory.append(second_cords[0] - 1 - i)
                        cord_memory.append(second_cords[1] + 1 + i)
                else:
                    cord_memory = []
                    break

        # left mid
        if 0 <= second_cords[0] <= 7 and 0 <= second_cords[1] - 1 <= 7 and \
                place[second_cords[0]][second_cords[1] - 1] == y:
            print('check left mid, cords = ', second_cords )
            for i in range(1, 8):
                if 0 <= second_cords[0] <= 7 and 0 <= second_cords[1] - 1 - i <= 7:
                    if place[second_cords[0]][second_cords[1] - 1 - i] == x:
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0]][second_cords[1]] = x
                        place[second_cords[0]][second_cords[1] - 1] = x
                        break
                    else:
                        cord_memory.append(second_cords[0])
                        cord_memory.append(second_cords[1] - 1 - i)
                else:
                    cord_memory = []
                    break

        # right mid
        if 0 <= second_cords[0] <= 7 and 0 <= second_cords[1] + 1 <= 7 and \
                place[second_cords[0]][second_cords[1] + 1] == y:
            print('check right mid')
            for i in range(1, 8):
                if 0 <= second_cords[0] <= 7 and 0 <= second_cords[1] + 1 + i <= 7:
                    if place[second_cords[0]][second_cords[1] + 1 + i] == x:
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0]][second_cords[1] + 1] = x
                        place[second_cords[0]][second_cords[1]] = x
                        break
                    else:
                        cord_memory.append(second_cords[0])
                        cord_memory.append(second_cords[1] + 1 + i)
                else:
                    cord_memory = []
                    break

        # left top
        if 0 <= second_cords[0] + 1 <= 7 and 0 <= second_cords[1] - 1 <= 7 and \
                place[second_cords[0] + 1][second_cords[1] - 1] == y:
            print('check left top 1')
            for i in range(1, 8):
                if 0 <= second_cords[0] + 1 + i <= 7 and 0 <= second_cords[1] - 1 - i <= 7:
                    print('check left top 2')
                    if place[second_cords[0] + 1 + i][second_cords[1] - 1 - i] == x:
                        print('check left top 3')
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0] + 1][second_cords[1] - 1] = x
                        place[second_cords[0]][second_cords[1]] = x
                        break
                    else:
                        cord_memory.append(second_cords[0] + 1 + i)
                        cord_memory.append(second_cords[1] - 1 - i)
                else:
                    cord_memory = []
                    break

        # middle top
        if 0 <= second_cords[0] + 1 <= 7 and 0 <= second_cords[1] <= 7 and \
                place[second_cords[0] + 1][second_cords[1]] == y:
            print('check mid top')
            for i in range(1, 8):
                if 0 <= second_cords[0] + 1 + i <= 7 and 0 <= second_cords[1] <= 7:
                    if place[second_cords[0] + 1 + i][second_cords[1]] == x:
                        # print(cord_memory)
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0] + 1][second_cords[1]] = x
                        place[second_cords[0]][second_cords[1]] = x
                        break
                    else:
                        cord_memory.append(second_cords[0] + 1 + i)
                        cord_memory.append(second_cords[1])
                else:
                    cord_memory = []
                    break

        # right top
        if 0 <= second_cords[0] + 1 <= 7 and 0 <= second_cords[1] + 1 <= 7 and \
                place[second_cords[0] + 1][second_cords[1] + 1] == y:
            print('check right top')
            for i in range(1, 8):
                if 0 <= second_cords[0] + 1 + i <= 7 and 0 <= second_cords[1] + 1 + i <= 7:
                    if place[second_cords[0] + 1 + i][second_cords[1] + 1 + i] == x:
                        for j in range(0, len(cord_memory), 2):
                            place[cord_memory[j]][cord_memory[j + 1]] = x
                        place[second_cords[0] + 1][second_cords[1] + 1] = x
                        place[second_cords[0]][second_cords[1]] = x
                        break
                    else:
                        cord_memory.append(second_cords[0] + 1 + i)
                        cord_memory.append(second_cords[1] + 1 + i)
                else:
                    cord_memory = []
                    break


# print(main('1 2', 1, 2))
# main()
