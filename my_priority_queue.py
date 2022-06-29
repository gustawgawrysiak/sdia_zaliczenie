class PriorityQueue:

    def __init__(self):
        self.c = []

    def is_empty(self):
        return self.c == []

    def detach(self):
        if self.is_empty():
            raise ValueError
        return self.c.pop(0)

    def attach(self, x, pri):
        if self.is_empty() or pri <= self.c[-1][1]:
            self.c.append((x, pri))
        elif pri > self.c[0][1]:
            self.c.insert(0, (x, pri))
        else:
            inserted = False
            for tup in range(len(self.c)):
                if inserted:
                    pass
                else:
                    if pri > self.c[tup][1]:
                        self.c.insert(tup, (x, pri))
                        inserted = True

    def front(self):
        if self.is_empty():
            raise ValueError
        return self.c[0]
