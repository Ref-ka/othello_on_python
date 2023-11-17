import time
from OthelloBack2 import main
import customtkinter as ctk
from functools import partial


place = [[0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1]]

window_height = 520
window_width = 480
chip = 1
revers_chip = 2

window = ctk.CTk()
window.geometry(f'{window_width}x{window_height}')
window.title('Othello')
window.resizable(False, False)

# window = tk.Tk()
# window.title('Othello')
# window.geometry(f'{window_width}x{window_height}')
# window.resizable(False, False)

# under_place_frame = tk.Frame(window, height=560, width=560, bg='#000000')
# under_place_frame.grid(row=1, column=0, rowspan=7)
under_place_frame = ctk.CTkFrame(master=window, height=560, width=560, fg_color='#483D8B')
under_place_frame.grid(column=0, row=1, rowspan=7)
# info_frame = tk.Frame(window, height=40, width=600, bg='#FFE4E1')
# info_frame.grid(row=0, column=0)
info_frame = ctk.CTkFrame(master=window, height=40, width=600, fg_color='#9370DB')
info_frame.grid(column=0, row=0)


class Button(ctk.CTkButton):
    def __init__(self, x, y, *args, **kwargs):

        ctk.CTkButton.__init__(self, *args, **kwargs)
        self.x = x
        self.y = y

    def get_coords(self):
        # print(self.x, self.y)
        return self.x, self.y


def get(button):
    # print(button)
    print(button.get_coords())
    update(button.get_coords())


# for i in range(8):
#     if i != 1 and i != 3 and i != 5:
#         tk.Frame(info_frame, height=1, width=31, bg='#FFE4E1').grid(row=0, column=i)

# for i in range(1, 9):
#     for j in range(8):
#         tk.Frame(under_place_frame, height=65, width=65, bg='#696969').grid(row=i, column=j, padx=5, pady=5)

# tk.Frame(under_place_frame, height=20, width=20, bg='#000000').grid(row=5, column=3)
# tk.Frame(under_place_frame, height=20, width=20, bg='#000000').grid(row=4, column=4)
# tk.Frame(under_place_frame, height=20, width=20, bg='#FFFFFF').grid(row=4, column=3)
# tk.Frame(under_place_frame, height=20, width=20, bg='#FFFFFF').grid(row=5, column=4)


buttons = {}

for i in range(7, -1, -1):
    for j in range(8):
        ctk.CTkFrame(master=under_place_frame, height=60, width=60, fg_color='grey', border_color='#696969', border_width=5).grid(column=j, row=7 - i)
        # buttons[Button(x=i, y=j, master=place_frame, width=20, text='0', command=seve_coords())] = f'{i}{j}'
        # buttons[f'{i}{j}'].grid(column=j, row=i)

        buttons[f'{i}{j}'] = Button(x=j, y=i, master=under_place_frame, width=28, text='', fg_color='#A9A9A9')
        # print(buttons[f'{i}{j}'].x, buttons[f'{i}{j}'].y)
        buttons[f'{i}{j}'].configure(command=partial(get, buttons[f'{i}{j}']))
        buttons[f'{i}{j}'].grid(column=j, row=7 - i)
        if place[i][j] == 1:
            buttons[f'{i}{j}'].configure(fg_color='black')
        if place[i][j] == 2:
            buttons[f'{i}{j}'].configure(fg_color='white')
# print(buttons)

info_text = ctk.CTkLabel(info_frame, text='Firs player turn', height=1, width=30)
info_text.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# cords_input = tk.Entry(info_frame, width=25)
# cords_input.grid(row=0, column=3, padx=5, pady=5, sticky='e')


def update(input_cords):
    global buttons
    global chip
    global revers_chip
    start = time.time_ns()
    print('called with ', input_cords)
    new_place, text, chip_front2, chip_front2_revers, cont = main(input_cords[0], input_cords[1], chip)
    print(chip_front2, chip_front2_revers)
    info_text.configure(text=text)
    # print(place)
    for k in range(8):
        for h in range(8):
            print(new_place[k][h].state, end=' ')
            # print(k, h, 'cords')
            if new_place[k][h].state == 1:
                # print('here')
                # print(buttons[f'{i}{j}'].get_coords())
                # print(8 - k, h, 'black')
                # tk.Frame(under_place_frame, height=20, width=20, bg='#000000').grid(row=9 - k, column=h)
                buttons[f'{k}{h}'].configure(fg_color='black')
                # print(k, h)
                # print(buttons[f'{h}{k}'].y, buttons[f'{h}{k}'].x)
            if new_place[k][h].state == 2:
                # print(8 - k, h, 'white')
                # tk.Frame(under_place_frame, height=20, width=20, bg='#FFFFFF').grid(row=9 - k, column=h)
                buttons[f'{k}{h}'].configure(fg_color='white')
        print()
    # for k in range(8):
    #     for h in range(8):
    #         print(1 if buttons[h, k]., end=' ')
    chip = chip_front2
    revers_chip = chip_front2_revers
    end = time.time_ns()
    print(end - start)


# update_button = tk.Button(info_frame, height=1, width=5, bg='#FFE4C4', command=update)
# update_button.grid(row=0, column=5, padx=5, pady=5, sticky='w')


window.mainloop()
