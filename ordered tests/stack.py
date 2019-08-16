class Stack():

    def __init__(self):
        self.__items = []
        self.__index = 0

    def __len__(self):
        return self.__index

    @property
    def is_empty(self):
        return self.__index == 0

    def peek(self):
        if self.is_empty:
            raise IndexError("Cannot peek from an empty stack!")

        return self.__items[self.__index - 1]

    def pop(self):
        if self.is_empty:
            raise IndexError("Cannot pop from an empty stack!")

        self.__index -= 1
        item = self.__items[self.__index]
        self.__items[self.__index] = None
        return item

    def push(self, item):
        if len(self.__items) == self.__index:
            self.__items.append(item)
        else:
            self.__items[self.__index] = item
        self.__index += 1