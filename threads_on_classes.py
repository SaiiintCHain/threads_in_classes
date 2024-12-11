import threading
import time


class Knight(threading.Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        count = 100
        counter = 0
        print(f'{self.name}, на нас напали!')
        while count:
            count = count - self.power
            counter += 1
            time.sleep(1)
            print(f'{self.name} сражается {counter} дней (дня), осталось {count} воинов.\n')
        print(f'{self.name}одержал победу спустя {counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()


