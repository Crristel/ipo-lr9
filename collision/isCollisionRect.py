from .isCorrectRect import isCorrectRect

class RectCorrectError(Exception):
    pass
def isCollisionRect(list1,list2):
    rectangle_1, rectangle_2=list1,list2
    if not isCorrectRect(rectangle_1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rectangle_2):
        raise RectCorrectError("2й прямоугольник некоректный")
    else:
        (x1,y1),(x2,y2)=rectangle_1
        (x3,y3),(x4,y4)=rectangle_2
    if (x2<x3 or x1>x4 or y1>y4 or y2<y3):
        return False
    return True
