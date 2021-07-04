class Queue:
    def __init__(self, maxsize=-1, queue=None):
        if queue is None:
            queue = []
        self.__queue_array = queue
        self.maxsize = maxsize

    def __str__(self):
        return str(self.__queue_array)

    def append(self, value):
        if self.length() == self.maxsize:
            raise OverflowError("Queue is full!")
        self.__queue_array.append(value)

    def get(self, index=0):
        if self.empty():
            return
        info_to_return = self.__queue_array[index]
        self.__queue_array.pop(index)
        return info_to_return

    def remove(self, value):
        self.__queue_array.remove(value)

    def length(self):
        return len(self.__queue_array)

    def full(self):
        return len(self.__queue_array) == self.maxsize

    def empty(self):
        return len(self.__queue_array) == 0

    def reset(self):
        self.__queue_array = []

    def get_value(self, index=0):
        if self.empty():
            return
        info_to_return = self.__queue_array[index]
        return info_to_return
