class Unit:
    # ...
    def move_unit_to_object(self, field, x_coord, y_coord, direction, fly, crawl, speed=1):

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
