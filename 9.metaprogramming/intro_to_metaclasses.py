class Animal:
    has_legs = True
    speaks = True


class Bird(Animal):
    has_wings = True
    lays_eggs = True
    number_of_legs = 2


class Human(Animal):
    number_of_legs = 2
    has_wings = False
    can_imagine = True


StrangeAnimal = type('StrangeAnimal', (Bird, Human), {'breathes_fire': True})


# Example 2
class CustomPrice(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.value = 1
        return x


class Price(metaclass=CustomPrice):

    _CURR_CHOICES = (
        'Rs',
        'Dollar',
        'Yen'
    )

    _CONVERSION_RATES = {
        'Dollar': 70,
        'Yen': 50,
        'Rs': 1
    }

    def __init__(self, currency):
        if currency not in self._CURR_CHOICES:
            raise ValueError('currency must be one of {}'.format(
                ','.join(self._CURR_CHOICES)
            ))
        self.currency = currency

    def __str__(self):
        return '{} {}'.format(self.currency, self.value)

    def __repr__(self):
        return '{} {}'.format(self.currency, self.value)

    @property
    def rupees(self):
        return '{} {}'.format(
            'Rs',
            self.value * self._CONVERSION_RATES.get(self.currency)
        )


if __name__ == '__main__':
    s = StrangeAnimal()
    print(s.breathes_fire)
    p = Price('Dollar')
    p.rupees
