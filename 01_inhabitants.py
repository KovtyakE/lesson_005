# -*- coding: utf-8 -*-
# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
def printing(folks, __name__):
    print("In the", __name__, "living next citizens:", end=' ')
    for citizen in folks:
        if citizen != folks[-1]:
            print(citizen, ",", sep="", end=' ')
        else:
            print(citizen, end=' ')
    print(" ")


from room_1 import folks, __name__
printing(folks, __name__)

from room_2 import folks, __name__
printing(folks, __name__)
