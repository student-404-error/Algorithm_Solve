class Deque:

    rear = 0
    front = 0
    deq = list()
    MAX_SIZE = 100

    def __init__(self) -> None:
        self.rear = 0
        self.front = 0
        self.deq = [0 for _ in range(self.MAX_SIZE)]

    def is_empty(self):
        if self.rear == self.front:
            return True
        return False

    def get_rear(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return -1
        return self.rear

    def get_front(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return -1
        return self.front
    
    