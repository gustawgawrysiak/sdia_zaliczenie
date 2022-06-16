class PriorityQueue:

    def __init__(self):
        '''tworzy nową pustą kolejkę priorytetową'''
        self.c = []

    def is_empty(self):
        '''zwraca odpowiedź na pytanie, czy kolejka priorytetowa jest pusta'''
        return self.c == []

    def detach(self):
        '''usuwa element o najwyższym priorytecie -- oraz zwraca parę (element, priorytet);
        w przypadku kilku elementów o najwyższym priorytecie brany jest ten dodany najwcześniej;
        w przypadku pustej kolejki -- wyjątek ValueError'''
        if self.is_empty():
            raise ValueError
        else:
            return self.c.pop(0)

    def attach(self, x):
        '''dokłada nowy element do kolejki priorytetowej'''
        if self.is_empty() or x <= self.c[-1]:
            self.c.append(x)
        elif x > self.c[0]:
            self.c.insert(0, x)
        else:
            inserted = False
            for tup in range(len(self.c)):
                if inserted:
                    pass
                else:
                    if x > self.c[tup]:
                        self.c.insert(tup, x)
                        inserted = True

    def front(self):
        '''zwraca (bez usuwania) element o najwyższym priorytecie jako parę (element, priorytet);
        w przypadku kilku elementów o najwyższym priorytecie brany jest ten dodany najdawniej;
        w przypadku pustej kolejki -- wyjątek ValueError'''
        if self.is_empty():
            raise ValueError
        else:
            return self.c[0]
