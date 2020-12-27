
class Counter:
    def __init__(self, min_value, max_value, current_value=None):
        self.__min_value = min_value
        self.__max_value = max_value
        if current_value is None:
            self.__current_value = self.__min_value
        else:
            self.__current_value = current_value

    def step(self):
        if self.__current_value < self.__max_value:
            self.__current_value += 1
        else:
            self.__current_value = self.__min_value

    def get_current_value(self):
        return self.__current_value

    def __str__(self):
        return 'Current value: {c}'.format(c=self.__current_value)


counter = Counter(0, 100)
for _ in range(150):
    print(counter)
    counter.step()
