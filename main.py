from ReadWriteMemory import ReadWriteMemory
import threading, win32api, os, subprocess, keyboard
from tkinter import *
from tkinter.font import Font


class HackedMemory:
    Object = ReadWriteMemory()

    def __init__(self, name_progress):
        hack_memory = HackedMemory.Object
        self.process = hack_memory.get_process_by_name(name_progress)
        self.process.open()

    def call_pointer(self, address, offsets):
        self.pointer = self.process.get_pointer(address, offsets)

    def read_memory(self):
        return self.process.read(self.pointer)

    def write_memory(self, value):
        self.process.write(self.pointer, value)

    def close(self):
        self.process.close()


class HackedProcess:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def address_offsets(self, address, offsets):
        self.address = address
        self.offsets = offsets

    def write_memory(self):
        try:
            self.process = HackedMemory(self.name)
            self.process.call_pointer(self.address, self.offsets)
            self.process.write_memory(self.money)
            self.process.close()
        except Exception:
            win32api.Beep(1000, 100)
            win32api.Beep(1000, 100)
            win32api.Beep(1000, 100)
            os._exit(1)


class MenuHacked(object):
    def __init__(self, width, height):
        self.window = Tk()
        self.width = width
        self.height = height
        self.font = Font(family="SimSun-ExtB", size=16)

    def beepbeep(self):
        self.BeepBeep = win32api.Beep(1000, 100)

    def properties(self, alpha, background):
        self.window.geometry(f"{self.width}x{self.height}+1400+300")
        self.window.title("")
        self.window.wm_overrideredirect(False)
        self.window.wm_attributes('-toolwindow', False)
        self.window.wm_attributes('-topmost', True)
        self.window.wm_attributes('-alpha', alpha)
        self.window.configure(bg=background)

    def status_money(self, event=None):
        self.beepbeep()
        address = 0x10000000 + 0x002020BC
        offsets = [0x18, 0x8, 0x50, 0xD8, 0x10, 0x8, 0x108]
        process = HackedProcess("Kingdom Rush.exe", 999999)
        process.address_offsets(address, offsets)
        process.write_memory()
        # ------------------------------------
        self.label_status_money.config(text="⚫ ON ")
        self.label_status_money.config(bg="black", fg="#00FF00")

    def value_money(self):
        self.label_status_money = Label(self.window, text=" F1   ⇝ MONEY: ")
        self.label_status_money.config(bg="black", fg="yellow")
        self.label_status_money.configure(font=self.font)
        self.window.bind("<F1>", self.status_money)
        self.label_status_money.place(x=40, y=150)
        # -------------------------------------
        self.label_status_money = Label(self.window, text="⚫ OFF")
        self.label_status_money.config(bg="black", fg="#FF0000")
        self.label_status_money.configure(font=self.font)
        self.label_status_money.place(x=230, y=150)

    def status_life(self, event=None):
        self.beepbeep()
        address = 0x10000000 + 0x001F3330
        offsets = [0xC8, 0x8, 0x50, 0xD8, 0x10, 0x8, 0x104]
        process = HackedProcess("Kingdom Rush.exe", 9999)
        process.address_offsets(address, offsets)
        process.write_memory()
        # ------------------------------------
        self.label_status_life.config(text="⚫ ON ")
        self.label_status_life.config(bg="black", fg="#00FF00")

    def value_life(self):
        self.label_status_life = Label(self.window, text=" F2   ⇝  LIFE: ")
        self.label_status_life.config(bg="black", fg="yellow")
        self.label_status_life.configure(font=self.font)
        self.window.bind("<F2>", self.status_life)
        self.label_status_life.place(x=40, y=200)
        # -------------------------------------
        self.label_status_life = Label(self.window, text="⚫ OFF")
        self.label_status_life.config(bg="black", fg="#FF0000")
        self.label_status_life.configure(font=self.font)
        self.label_status_life.place(x=230, y=200)

    def status_exit(self, event=None):
        self.beepbeep()
        self.beepbeep()
        self.beepbeep()
        os._exit(0)

    def exit_window(self):
        self.label_exit = Label(self.window, text=" ESC  ⇝ END TASK NOW ")
        self.label_exit.config(bg="black", fg="yellow")
        self.label_exit.configure(font=self.font)
        self.window.bind("<Escape>", self.status_exit)
        self.label_exit.place(x=40, y=300)

    def show_window(self):
        self.beepbeep()
        self.beepbeep()
        self.beepbeep()
        self.label_show = Label(self.window, text="〔 MENU HACK 〕")
        self.label_show.config(bg="black", fg="red")
        self.label_show.configure(font=self.font)
        self.window.bind("<Escape>", self.status_exit)
        self.label_show.place(x=100, y=350)

        self.label_show = Label(self.window, text="☆ KINGDOM RUSH ☆")
        self.label_show.config(bg="black", fg="yellow")
        self.label_show.configure(font=self.font)
        self.window.bind("<Escape>", self.status_exit)
        self.label_show.place(x=70, y=50)

        self.label_show = Label(self.window, text="☢ MOD BY DUKE ☢")
        self.label_show.config(bg="black", fg="yellow")
        self.label_show.configure(font=self.font)
        self.window.bind("<Escape>", self.status_exit)
        self.label_show.place(x=70, y=400)

    def start(self):
        try:
            self.window.mainloop()
        except KeyboardInterrupt:
            self.beepbeep()
            self.beepbeep()
            self.beepbeep()
            os._exit(1)


if __name__ == "__main__":
    Application = MenuHacked(340, 500)
    Application.properties(0.5, "black")
    Application.value_money()
    Application.value_life()
    Application.exit_window()
    Application.show_window()
    Application.start()

# address = 0x10000000 + 0x0020213C
# offsets = [0x2B4, 0x20, 0x20, 0x44, 0x108]

# address = 0x10000000 + 0x001F32C4
# offsets = [0x50, 0x108, 0x8, 0xC, 0x290, 0x104]
