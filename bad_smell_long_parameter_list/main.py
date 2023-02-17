# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state):
        self.state = state
    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        if self.state == 'crawl':
            return self.speed * 0.5
        else:
            return "Неверное состояние"
    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.fields.set_unit(y=self.y + speed, x=self.x, unit=self)
        if direction == 'DOWN':
            self.fields.set_unit(y=self.y - speed, x=self.x, unit=self)
        if direction == 'LEFT':
            self.fields.set_unit(y=self.y + speed, x=self.x, unit=self)
        if direction == 'RIGHT':
            self.fields.set_unit(y=self.y - speed, x=self.x, unit=self)
