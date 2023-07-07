class Dict:
    default_length = 2
    default_coefficient = 0.7

    def __init__(self):
        self.coefficient = Dict.default_coefficient
        self.length = Dict.default_length
        self.list = [[] for _ in range(self.length)]
        self.occupied = 0

    def __hash(self, obj) -> int:
        if obj.__hash__:
            return obj.__hash__() % self.length
        else:
            raise TypeError('Mutable object cannot have a hash')

    def __extend(self, new_length=None):
        self.length = new_length or self.length * 2
        new_list = [[] for _ in range(self.length)]

        for el in self.list:
            for key, value in el:
                new_list[self.__hash(key)].append((key, value))

        self.list = new_list

    def update(self, key, value) -> None:
        index = self.__hash(key)
        if len(self.list[index]) == 0:
            self.occupied += 1

        self.list[index].append((key, value))

        if self.occupied / self.length > self.coefficient:
            self.__extend()

    def get(self, key):
        index = self.__hash(key)

        for k, value in self.list[index]:
            if k == key:
                return value

        return None

    def __setitem__(self, key, value) -> None:
        self.update(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        return self.list.__str__()


if __name__ == '__main__':
    d = Dict()

    for i in range(10):
        d.update(str(i), i)
        print(d[str(i)])

    print(d)
