from person import Person


class Manager(Person):
    """
    класс со специализаванным методом giveRaise
    """
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

    def __str__(self):
        return '%s => %s' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    bob = Person('Bob Smith', 47)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, job='Manager', pay=50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        print(obj)
