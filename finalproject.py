#To-do list

class Todo_List:
    def __init__(self, items):
        self.items = list(items)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

