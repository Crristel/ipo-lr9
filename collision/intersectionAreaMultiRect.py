from .isCorrectRect import isCorrectRect

class RectCorrectError(Exception):
    pass

def intersectionAreaMultiRect(rects_coords):
    unique_coords = []

    for num_of_rect, rect in enumerate(rects_coords, start=1):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Некорректный {num_of_rect} прямоугольник")
        
        if rect not in unique_coords:
            unique_coords.append(rect)
    
    total_square = 0
    len_of_lst = len(unique_coords)

    for i in range(len_of_lst):
        for j in range(i + 1, len_of_lst):
            (x1, y1), (x2, y2) = unique_coords[i]
            (x3, y3), (x4, y4) = unique_coords[j]

            if x1 > x4 or y1 > y4 or x2 < x3 or y2 < y3:
                continue

            xCross_left = max(x1, x3)
            yCross_bottom = max(y1, y3)
            xCross_right = min(x2, x4)
            yCross_top = min(y2, y4)

            crossWidth = xCross_right - xCross_left
            crossHeight = yCross_top - yCross_bottom

            if crossWidth > 0 and crossHeight > 0:  
                total_square += crossWidth * crossHeight

    return total_square
