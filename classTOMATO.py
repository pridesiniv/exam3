class Tomato:
    states = {1: 'Первая стадия созревания', 2: 'Вторая стадия созревания',
              3: 'Зрелый'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Tомат {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Cадовник начал работу')
        self._plant.grow_all()
        print('Садовник закончил удобрять томаты')

    def harvest(self):
        print('Проверка спелости томатов')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все томаты созрели!')
        else:
            print('Не все томаты созрели, ещё нужно работать и ждать...')

    @staticmethod
    def knowledge_base():
        print('''Справка по садоводству: Собирайте томаты, когда все созрели
        Не забывайте удобрять и ухаживать
        Хороший томат - алый, твёрдый''')

    # Proverka


if __name__ == '__main__':
    # 1. Вызовите справку по садоводству
    Gardener.knowledge_base()
    # 2. Создайте объекты классов TomatoBush и Gardener
    tomat = TomatoBush(4)
    cadovnuk = Gardener('Otec', tomat)
    # 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
    # 4. Попробуйте собрать урожай
    # 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
    # 6. Соберите урожай
    cadovnuk.work()
    cadovnuk.work()
    cadovnuk.harvest()
    cadovnuk.work()
    cadovnuk.harvest()

