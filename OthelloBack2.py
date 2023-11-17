import copy


class Chip:

    def __init__(self, state, y, x):
        self.state = state
        self.x = x
        self.y = y


# class Place:
#
#     def __init__(self):
#         self.field = []
#         for i in range(9):
#             self.field.append([])
#             for j in range(9):
#                 if (i == 3 and j == 3) or (i == 4 and j == 4):
#                     self.field[i].append(Chip(1, j, i))
#                 elif (i == 3 and j == 4) or (i == 4 and j == 3):
#                     self.field[i].append(Chip(2, j, i))
#                 else:
#                     self.field[i].append(Chip(0, j, i))
#
#     def upd(self, x, y):


field = [[], [], [], [], [], [], [], []]
for i in range(8):
    for j in range(8):
        if (i == 3 and j == 3) or (i == 4 and j == 4):
            field[i].append(Chip(2, i, j))
        elif (i == 3 and j == 4) or (i == 4 and j == 3):
            field[i].append(Chip(1, i, j))
        else:
            field[i].append(Chip(0, i, j))

for i in range(8):
    for j in range(8):
        print(field[i][j].state, end=' ')
    print()


def main(x, y, chip):
    cont = True
    count = 0
    first_count = 0
    second_count = 0
    memory = []
    previous_field = copy.deepcopy(field)
    for i in range((y - 1) if y - 1 >= 0 else y, (y + 2) if y + 2 <= 7 else y + 1):
        for j in range((x - 1) if x - 1 >= 0 else x, (x + 2) if x + 2 <= 7 else x + 1):
            # print(i, j, field[i][j].state, field[i][j].x, field[i][j].y)
            if field[i][j].state == 0 or field[i][j].state == chip:
                # print('pass', field[i][j].state, field[i][j].x, field[i][j].y)
                pass
            else:
                iter_y_minus = range(i, 0, -1)

                iter_y_plus = range(i, 8, 1)
                iter_x_minus = range(j, 0, -1)
                iter_x_plus = range(j, 8, 1)
                if i > y:
                    print('i>y')
                    for k in iter_y_plus:
                        if j > x:
                            for n in iter_x_plus:
                                if field[k][n] == 0:
                                    break
                                elif field[k][n] == 1:
                                    for cords in memory:
                                        field[cords[0]][cords[1]].state = chip
                                    memory = []
                                    break
                                else:
                                    memory.append([k, n])
                        elif j < x:
                            for n in iter_x_minus:
                                if field[k][n] == 0:
                                    break
                                elif field[k][n] == 1:
                                    for cords in memory:
                                        field[cords[0]][cords[1]].state = chip
                                    memory = []
                                    break
                                else:
                                    memory.append([k, n])
                        else:
                            if field[k][0] == 0:
                                break
                            elif field[k][0] == 1:
                                for cords in memory:
                                    field[cords[0]][cords[1]].state = chip
                                memory = []
                                break
                            else:
                                memory.append([k, 0])
                elif i < y:
                    print('i<y')
                    for k in iter_y_minus:
                        if j > x:
                            for n in iter_x_plus:
                                if field[k][n] == 0:
                                    break
                                elif field[k][n] == 1:
                                    for cords in memory:
                                        field[cords[0]][cords[1]].state = chip
                                    memory = []
                                    break
                                else:
                                    memory.append([k, n])
                        elif j < x:
                            for n in iter_x_minus:
                                if field[k][n] == 0:
                                    break
                                elif field[k][n] == 1:
                                    for cords in memory:
                                        field[cords[0]][cords[1]].state = chip
                                    memory = []
                                    break
                                else:
                                    memory.append([k, n])
                        else:
                            if field[k][0] == 0:
                                break
                            elif field[k][0] == chip:
                                for cords in memory:
                                    field[cords[0]][cords[1]].state = chip
                                memory = []
                                break
                            else:
                                memory.append([k, 0])
                else:
                    # print('else')
                    for n in iter_x_plus if j > x else iter_x_minus:
                        # print(y, n)
                        if field[y][n].state == 0:
                            break
                        elif field[y][n].state == chip:
                            # print('write')
                            memory.append([y, x])
                            for cords in memory:
                                field[cords[0]][cords[1]].state = chip
                                # print(field[cords[0]][cords[1]].state)
                            memory = []
                            break
                        else:
                            print('memory')
                            memory.append([y, n])

    for i in range(8):
        for j in range(8):
            if field[i][j] == 1:
                count += 1
                first_count += 1
            elif field[i][j] == 2:
                count += 1
                second_count += 1
    if count == 64:
        if first_count < second_count:
            cont = False
            text = 'Game over Second player win'
            return field, text, chip, 2 if chip == 1 else 1, cont
        else:
            cont = False
            text = 'Game over First player win'
            return field, text, chip, 2 if chip == 1 else 1, cont
    if field == previous_field:
        text = f'Wrong cords, another {"second" if chip == 2 else "first"} player turn!'
        return field, text, chip, 2 if chip == 1 else 1, cont
    for i in range(8):
        for j in range(8):
            print(field[i][j].state, end=' ')
        print()
    return field, 'Second player turn' if chip == 1 else 'First player turn', 2 if chip == 1 else 1, chip, cont

# main(5, 4, 1)