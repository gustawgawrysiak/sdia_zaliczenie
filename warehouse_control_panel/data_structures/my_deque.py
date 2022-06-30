class Deque:
    
    def __init__(self):
        self.lista = []
        
    def push_front(self, item):
        self.lista.insert(0, item)

    def pop_front(self):
        if self.lista != []:
            return self.lista.pop(0)
        else:
            raise ValueError
        
    def front(self):
        if self.lista != []:
            return self.lista[0]
        else:
            raise ValueError
        
    def push_back(self, item):
        self.lista.append(item)

    def pop_back(self):
        if self.lista != []:
            return self.lista.pop(-1)
        else:
            raise ValueError
        
    def back(self):
        if self.lista != []:
            return self.lista[-1]
        else:
            raise ValueError
        
    def is_empty(self):
        if self.lista == []:
            return True
