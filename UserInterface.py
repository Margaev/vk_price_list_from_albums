from tkinter import *


class UserInterface:

    def __init__(self, records):
        self.root = Tk()
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.root, selectmode=MULTIPLE, width=50, height=25, yscrollcommand=self.scrollbar.set)
        self.selected_items = tuple()
        self.button = Button(self.root, bg="red", text=u"Добавить выбранные альбомы",
                             command=lambda: self.set_selected_items(self.listbox.curselection()))

        self.add_records(records)

        self.listbox.pack(fill=BOTH)
        self.button.pack()

        self.scrollbar.config(command=self.listbox.yview)

        self.root.mainloop()

    def add_records(self, records):
        for r in records:
            self.listbox.insert(END, r)

    def set_selected_items(self, items):
        self.selected_items = items

    def get_selected_items(self):
        return self.selected_items
