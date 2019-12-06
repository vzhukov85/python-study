"""
Альтернативные реализации Person и Manager с данными, методами и с перегрузкой операторов
(не оиспользуется в объектах, предусматривающих возможность сохранения)
"""


class Person:
    """
    универсальное представление человекаЖ данные + логика
    """

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1 + percent)

    def __str__(self):
        return '<%s => %s: %s, %s>' % (self.__class__.__name__, self.name, self.job, self.pay)


class Manager(Person):
    """
    класс со специализаванным методом giveRaise
    """

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 47)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', pay=50000, age=50)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        print(obj)
