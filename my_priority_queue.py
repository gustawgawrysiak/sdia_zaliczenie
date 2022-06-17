class PriorityQueue:  # pierwsza implementacja, najbardziej prosta i naiwna

    def __init__(self):
        '''tworzy nową pustą kolejkę priorytetową'''
        self.c = []
        # self. przechowuje pary (element, priorytet) posortowane priorytetami
        # jeśli priorytety są równe, to wcześniej są pary wcześniej dodane

    def is_empty(self):
        '''zwraca odpowiedź na pytanie, czy kolejka priorytetowa jest pusta'''
        return self.c == []

    def detach(self):
        '''usuwa element o najwyższym priorytecie -- oraz zwraca parę (element, priorytet);
        w przypadku kilku elementów o najwyższym priorytecie brany jest ten dodany najwcześniej;
        w przypadku pustej kolejki -- wyjątek ValueError'''
        if self.is_empty():
            raise ValueError
        return self.c.pop(0)

    def attach(self, x, pri):
        '''dokłada nowy element do kolejki priorytetowej
        zakładamy, że self.c jest zawsze posortowane priorytetami
        poszukać w self.c miejsca na wstawienie nowej krotki (x, pri) a potem wstawić
        w pierwszej wersji poszukiwanie wykonujemy liniowo (naiwnie, nie binarnie, po kolei)'''
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
        '''zwraca (bez usuwania) element o najwyższym priorytecie jako parę (element, priorytet);
        w przypadku kilku elementów o najwyższym priorytecie brany jest ten dodany najdawniej;
        w przypadku pustej kolejki -- wyjątek ValueError'''
        if self.is_empty():
            raise ValueError
        return self.c[0]
