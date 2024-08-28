import tkinter as tk
from tkinter.font import names

import pandas as pd

import organizer
import customtkinter

dataset = "dataset/csv/cards.csv"

class CardEntry(customtkinter.CTkFrame):
    def __init__(self, master, number, name, quantity):
        super().__init__(master)
        self.number = number
        self.name = name
        self.button = customtkinter.CTkButton(self, text="-", width=30, command=self.decrement_count)
        self.button.grid(row=0, column=0)
        self.entry = customtkinter.CTkEntry(self, width=30)
        self.entry.grid(row=0, column=1)
        self.button = customtkinter.CTkButton(self, text="+", width=30, command=self.increment_count)
        self.button.grid(row=0, column=2)
        self.label = customtkinter.CTkLabel(self, text=f" {number}) {name}")
        self.label.grid(row=0, column=3)

        self.entry.insert(0, f"{quantity}")

    def decrement_count(self):
        value = int(self.entry.get()) - 1
        self.entry.delete(0, "end")
        self.entry.insert(0, value)

    def increment_count(self):
        value = int(self.entry.get()) + 1
        self.entry.delete(0, "end")
        self.entry.insert(0, value)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("PaltaManager")
        self.geometry("700x1000")

        self.label = customtkinter.CTkLabel(self, text="Choose a set by its code")
        self.label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.set_label = customtkinter.CTkLabel(self, text="")
        self.set_label.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Code")
        self.entry.grid(row=1, column=0)
        self.button = customtkinter.CTkButton(self, text="Choose", command=self.check_set)
        self.button.grid(row=1, column=1, padx=10, pady=10)
        self.save_button = customtkinter.CTkButton(self, text="Save CSV", command=self.save_csv)
        self.save_button.grid(row=1, column=2, padx=10, pady=10)
        self.card_view = customtkinter.CTkScrollableFrame(self, width=400, height=800)
        self.card_view.grid(row=2, column=0, columnspan=3)

    def save_csv(self):
        df = pd.read_csv(dataset)
        set_offset = df.loc[df['setCode'] == self.set_label.cget("text")].index[0]
        for card in range(len(df.loc[df['setCode'] == self.set_label.cget("text")])):
            df.loc[card + set_offset, 'quantity'] = entries[card].entry.get()
        df.to_csv(dataset)

    def check_set(self):
        set_list = organizer.load_set(self.entry.get().upper())
        self.set_label.configure(text=self.entry.get().upper())
        self.entry.delete(0, "end")
        global entries
        entries = []
        for card in range(len(set_list)):
            temp_card = CardEntry(self.card_view, set_list.iloc[card]['number'], set_list.iloc[card]['name'], set_list.iloc[card]['quantity'])
            temp_card.grid(row=card, column=0, sticky='w')
            entries.append(temp_card)

app = App()
app.mainloop()