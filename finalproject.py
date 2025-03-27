#To-do list   
from flask import Flask as fl

class Todo_List:
    def __init__(self, items):
        self.items = list(items)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self):
        pass

    def name_item(self, name):
        self.name = name
