import customtkinter as ctk
from collections import defaultdict
import weakref
from functools import partial

window = ctk.CTk()
window.geometry('600x600')
window.title('Test')
window.resizable(False, False)

place_frame = ctk.CTkFrame(master=window, height=560, width=560, fg_color='red')
place_frame.grid(column=0, row=1, rowspan=7)
info_frame = ctk.CTkFrame(master=window, height=40, width=600, fg_color='green')
info_frame.grid(column=0, row=0)

changed = []


def save_coords(self):
    print('here')


# class KeepRefs(object):
#     __refs__ = defaultdict(list)
#
#     def __init__(self):
#         self.__refs__[self.__class__].append(weakref.ref(self))
#
#     @classmethod
#     def get_instances(cls):
#         for inst_ref in cls.__refs__[cls]:
#             inst = inst_ref()
#             if inst is not None:
#                 yield inst


class Button(ctk.CTkButton):
    def __init__(self, x, y, *args, **kwargs):
        # __refs__ = defaultdict(list)

        ctk.CTkButton.__init__(self, *args, **kwargs)
        # self.__refs__[self.__class__].append(weakref.ref(self))
        self.x = x
        self.y = y

    def get_coords(self):
        # print(self.x, self.y)
        return self.x, self.y


    # def get_instances(cls):
    #     for inst_ref in cls.__refs__[cls]:
    #         inst = inst_ref()
    #         if inst is not None:
    #             yield inst

def get(button):
    print(button)
    print(button.get_coords())


buttons = {}

for i in range(9):
    for j in range(9):
        ctk.CTkFrame(master=place_frame, height=60, width=60, fg_color='blue').grid(column=j, row=i)
        # buttons[Button(x=i, y=j, master=place_frame, width=20, text='0', command=seve_coords())] = f'{i}{j}'
        # buttons[f'{i}{j}'].grid(column=j, row=i)

        buttons[f'{i}{j}'] = Button(x=i, y=j, master=place_frame, width=20, text='0')
        # print(buttons[f'{i}{j}'].x, buttons[f'{i}{j}'].y)
        buttons[f'{i}{j}'].configure(command=partial(get, buttons[f'{i}{j}']))
        buttons[f'{i}{j}'].grid(column=j, row=i)
        print(buttons[f'{i}{j}']._command)


        # Button(x=i, y=j, master=place_frame, width=20, text='0', command=save_coords(Button.get_coords())).grid(column=j, row=i)

        # , command = save_coords(buttons[f'{i}{j}'].get_coords()

print(buttons)
# print(list(Button.get))


window.mainloop()


