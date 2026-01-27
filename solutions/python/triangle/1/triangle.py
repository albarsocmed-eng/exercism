def inequality(sides):
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]

def equilateral(sides):
    is_valid = inequality(sides)
    if is_valid == True:    
        x = set()
        for i in sides:
            if i <= 0:
                return False
            else:
                x.add(i)
        return len(x) == 1
    else:
        return False

def isosceles(sides):
    is_valid = inequality(sides)
    if is_valid == True:   
        x = set()
        for i in sides:
            if i <= 0:
                return False
            else:
                x.add(i)
        return len(x) <= 2
    else:
        return False

def scalene(sides):
    is_valid = inequality(sides)
    if is_valid == True:  
        x = set()
        for i in sides:
            if i <= 0:
                return False
            else:
                x.add(i)
        return len(x) == 3 
    else:
        return False
