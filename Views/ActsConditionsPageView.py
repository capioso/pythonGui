import csv
import tkinter as tk
from tkinter import ttk


class ActsConditionsPageView:
    def __init__(self, root):
        self.root = root
        self.panel = tk.Frame(self.root, bg="white", height=550)
        self.panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.panel, columns=(
            "Percentage", "Formula", "Meta 2022", "Unit", "Frequency", "Better", "Source"))
        self.tree.heading("#0", text="Indicator")
        self.tree.heading("Percentage", text="Percentage")
        self.tree.heading("Formula", text="Formula")
        self.tree.heading("Meta 2022", text="Meta 2022")
        self.tree.heading("Unit", text="Unit")
        self.tree.heading("Frequency", text="Frequency")
        self.tree.heading("Better", text="Better")
        self.tree.heading("Source", text="Source")

        self.tree.column("#0", minwidth=290, width=290, stretch=tk.YES)
        self.tree.column("Percentage", minwidth=350, width=350, stretch=tk.YES)
        self.tree.column("Formula", minwidth=70, width=70, stretch=tk.YES)
        self.tree.column("Meta 2022", minwidth=400, width=400, stretch=tk.YES)
        self.tree.column("Unit", minwidth=50, width=50, stretch=tk.YES)
        self.tree.column("Frequency", minwidth=90, width=90, stretch=tk.YES)
        self.tree.column("Better", minwidth=80, width=80, stretch=tk.YES)
        self.tree.column("Source", minwidth=70, width=70, stretch=tk.YES)
        self.tree.pack()
        self.tree.bind("<ButtonRelease-1>", self.on_select)
        self.selected_item_label = tk.Label(self.root,
                                            text="",
                                            bg="white",
                                            foreground="black",
                                            wraplength=800,
                                            justify=tk.LEFT,
                                            font=("Times New Roman", 12),
                                            pady=100)
        self.selected_item_label.pack(side=tk.TOP)
        self.insert_data_from_csv("Static/Porcentajes.csv")

    def insert_data_from_csv(self, filename):
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                row_values = [value.replace("\xa0", "") for value in row[1:]]
                self.tree.insert("", "end", text=row[0], values=row_values)

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            formatted_values = "\n".join([
                f"{self.tree.heading(column)['text']}: {value}"
                for column, value in zip(self.tree["columns"], item_values)
            ])
            self.selected_item_label.config(text=formatted_values)
