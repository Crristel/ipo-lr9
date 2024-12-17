def isCorrectRect(coordinates):
    LeftCoord,RightCoord=coordinates
    xLeft, yLeft=LeftCoord
    xRight,yRight=RightCoord
    if not isinstance(coordinates,list) or len(coordinates)!=2:
        return False
    elif not (
        isinstance(xLeft, (int, float))
        and isinstance(yLeft, (int, float))
        and isinstance(xRight, (int, float))
        and isinstance(yRight, (int, float))
        ):
        return False
        
    elif ((xLeft > xRight) or (yLeft > yRight)):
        return False
    elif not all(
        isinstance(coord_pair, tuple) and len(coord_pair) == 2
        for coord_pair in coordinates):

        return False
        
    return True
