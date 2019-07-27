# -*- coding: utf-8 -*-

class Player:
    def __init__(self, board, color):
        self._board = board
        self._color = color

    def set_color(self, color):
        self._color = color

    def put(self):
        ables = self._board.able_to_puts(self._color)
        print(self._board.to_string())
        if len(ables) > 0:
            print([f'{idx}:{v}' for idx, v in zip(range(len(ables)), ables)])
            print(f'Input index({self._color}):')
            position_id = int(input('>>'))
            x, y = ables[position_id]
            self._board.put_stone(self._color, x, y)
        else:
            print('Skip! (can not put)')