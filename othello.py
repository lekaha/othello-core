# coding=UTF-8
"""
This module is for Othello game that can contain Othello's rule and render the Othello broad while playing.
"""
BROAD_SIZE = 8

WHITE = 0
BLACK = 1
EMPTY = -1

UP = 0x101
DOWN = 0x102
LEFT = 0x103
RIGHT = 0x104
UPPER_LEFT = 0x105
UPPER_RIGHT = 0x106
LOWER_LEFT = 0x107
LOWER_RIGHT = 0x108

def checkMatrix(matrix):
    """
    Checking the matrix as broad is correct in standard Othello broad.
    """
    if type(matrix) != list:
        print type(matrix)
        return False
    if len(matrix) != BROAD_SIZE:
        print len(matrix)
        return False
    for x in matrix:
        if len(x) != BROAD_SIZE:
            return False
    return True

def discStr(value):
    if value is BLACK:
        return "●"
    if value is WHITE:
        return "○"
    if value is EMPTY:
        return "_"

def render(matrix):
    """
    Render Othello broad by a matrix that is 8*8 size.
    """

    if not checkMatrix(matrix):
        return
    string = ""
    string += "   a   b   c   d    e   f   g   h\n"
    # string += " ┌─┬─┬─┬─┬─┬─┬─┬─┐\n"
    string += "1[%s][%s][%s][%s][%s][%s][%s][%s]\n" % \
    (discStr(matrix[0][0]), discStr(matrix[0][1]), discStr(matrix[0][2]), discStr(matrix[0][3]),
        discStr(matrix[1][4]), discStr(matrix[0][5]), discStr(matrix[0][6]), discStr(matrix[0][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "2[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[1][0]), discStr(matrix[1][1]), discStr(matrix[1][2]), discStr(matrix[1][3]), 
        discStr(matrix[1][4]), discStr(matrix[1][5]), discStr(matrix[1][6]), discStr(matrix[1][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "3[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[2][0]), discStr(matrix[2][1]), discStr(matrix[2][2]), discStr(matrix[2][3]),
        discStr(matrix[2][4]), discStr(matrix[2][5]), discStr(matrix[2][6]), discStr(matrix[2][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "4[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[3][0]), discStr(matrix[3][1]), discStr(matrix[3][2]), discStr(matrix[3][3]),
        discStr(matrix[3][4]), discStr(matrix[3][5]), discStr(matrix[3][6]), discStr(matrix[3][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "5[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[4][0]), discStr(matrix[4][1]), discStr(matrix[4][2]), discStr(matrix[4][3]),
        discStr(matrix[4][4]), discStr(matrix[4][5]), discStr(matrix[4][6]), discStr(matrix[4][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "6[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[5][0]), discStr(matrix[5][1]), discStr(matrix[5][2]), discStr(matrix[5][3]),
        discStr(matrix[5][4]), discStr(matrix[5][5]), discStr(matrix[5][6]), discStr(matrix[5][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "7[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[6][0]), discStr(matrix[6][1]), discStr(matrix[6][2]), discStr(matrix[6][3]),
        discStr(matrix[6][4]), discStr(matrix[6][5]), discStr(matrix[6][6]), discStr(matrix[6][7]))
    # string += " ├─┼─┼─┼─┼─┼─┼─┼─┤\n"
    string += "8[%s][%s][%s][%s][%s][%s][%s][%s]\n" %  \
    (discStr(matrix[7][0]), discStr(matrix[7][1]), discStr(matrix[7][2]), discStr(matrix[7][3]),
        discStr(matrix[7][4]), discStr(matrix[7][5]), discStr(matrix[7][6]), discStr(matrix[7][7]))
    # string += " └─┴─┴─┴─┴─┴─┴─┴─┘\n"
    # print string
    return string


def initGame():
    """
    Generate a standard Othello broad in a matrix.
    """
    matrix = [[-1 for x in range(BROAD_SIZE)] for x in range(BROAD_SIZE)] 
    matrix[3][4] = WHITE
    matrix[3][3] = BLACK
    matrix[4][4] = BLACK
    matrix[4][3] = WHITE
    return matrix

def checkInvalidMove(matrix, x, y, value):
    """
    (Deprecated)
    Check the target position of moving is valid or not.
    (Only check the target position is or isn't stand alone place)
    """

    # Over Bundary testing
    if x > (BROAD_SIZE - 1) or y > (BROAD_SIZE - 1) or x < 0 or y < 0:
        return False

    # Current position testing
    if matrix[x][y] != EMPTY:
        return False

    # Invalid place testing
    # At the least one of eight direction should be opponent's disc.
    if (BROAD_SIZE - 1) == x:
        if (BROAD_SIZE - 1) == y: # right-bottom corner
            if (EMPTY == matrix[x - 1][y - 1]) \
                and (EMPTY == matrix[x - 1][y]) \
                and (EMPTY == matrix[x][y - 1]):
                return False
            
        elif 0 == y: # left-bottom corner
            if (EMPTY == matrix[x - 1][y + 1]) \
                and (EMPTY == matrix[x - 1][y]) \
                and (EMPTY == matrix[x][y + 1]):
                return False      

        else: # on bottom boundary not corner
            if (EMPTY == matrix[x - 1][y]) \
                and (EMPTY == matrix[x - 1][y - 1]) \
                and (EMPTY == matrix[x - 1][y + 1]) \
                and (EMPTY == matrix[x][y - 1]) \
                and (EMPTY == matrix[x][y + 1]):
                return False

    elif 0 == x:
        if (BROAD_SIZE - 1) == y: # right-top corner
            if (EMPTY == matrix[x][y - 1]) \
                and (EMPTY == matrix[x + 1][y - 1]) \
                and (EMPTY == matrix[x + 1][y]):
                return False
        elif 0 == y: # left-top corner
            if (EMPTY == matrix[x][y + 1]) \
                and (EMPTY == matrix[x + 1][y + 1]) \
                and (EMPTY == matrix[x + 1][y]):
                return False      
        else: # on top boundary not corner
            if (EMPTY == matrix[x][y - 1]) \
                and (EMPTY == matrix[x + 1][y - 1]) \
                and (EMPTY == matrix[x + 1][y]) \
                and (EMPTY == matrix[x + 1][y + 1]) \
                and (EMPTY == matrix[x][y + 1]):
                return False
    elif 0 == y:
        if (EMPTY == matrix[x - 1][y]) \
            and (EMPTY == matrix[x - 1][y + 1]) \
            and (EMPTY == matrix[x][y + 1]) \
            and (EMPTY == matrix[x + 1][y + 1]) \
            and (EMPTY == matrix[x + 1][y]):
            return False
    elif (BROAD_SIZE - 1) == y:
        if (EMPTY == matrix[x - 1][y]) \
            and (EMPTY == matrix[x - 1][y - 1]) \
            and (EMPTY == matrix[x][y - 1]) \
            and (EMPTY == matrix[x + 1][y - 1]) \
            and (EMPTY == matrix[x + 1][y]):
            return False

    # Not on the boundary
    if ((EMPTY == matrix[x - 1][y]) \
        and (EMPTY == matrix[x - 1][y - 1]) \
        and (EMPTY == matrix[x][y - 1]) \
        and (EMPTY == matrix[x + 1][y - 1]) \
        and (EMPTY == matrix[x + 1][y]) \
        and (EMPTY == matrix[x + 1][y + 1]) \
        and (EMPTY == matrix[x][y + 1]) \
        and (EMPTY == matrix[x - 1][y + 1])):
        return False

    return True

def flip(dir, matrix, x, y, value):
    """
    Flip discs to value by given direction and current position.
    """

    if UP == dir:
        i = x - 1
        willFlip = matrix[i][y]
        while value != willFlip and i > 0:
            i = i - 1
            willFlip = matrix[i][y]
        if willFlip == value:
            for f in xrange(i, x):
                matrix[f][y] = value
            return True
        else:
            return False

    elif UPPER_LEFT == dir:
        i = x - 1
        j = y - 1
        willFlip = matrix[i][j]
        while value != willFlip and i > 0 and j > 0:
            i = i - 1
            j = j - 1
            willFlip = matrix[i][j]
        if willFlip == value:
            for f in xrange(i, x):
                matrix[f][j] = value
                j = j + 1
            return True
        else:
            return False
    elif LEFT == dir:
        i = y - 1
        willFlip = matrix[x][i]
        while value != willFlip and i > 0:
            i = i - 1
            willFlip = matrix[x][i]
        if willFlip == value:
            for f in xrange(i, y):
                matrix[x][f] = value
            return True
        else:
            return False
    elif LOWER_LEFT == dir:
        i = x + 1
        j = y - 1
        willFlip = matrix[i][j]
        while value != willFlip and i < (BROAD_SIZE - 1) and j > 0:
            i = i + 1
            j = j - 1
            willFlip = matrix[i][j]
        if willFlip == value:
            for f in xrange(i, x, -1):
                matrix[f][j] = value
                j = j + 1
            return True
        else:
            return False
    elif DOWN == dir:
        i = x + 1
        willFlip = matrix[i][y]
        while value != willFlip and i < (BROAD_SIZE - 1):
            i = i + 1
            willFlip = matrix[i][y]
        if willFlip == value:
            for f in xrange(i, x, -1):
                matrix[f][y] = value
            return True
        else:
            return False
    elif LOWER_RIGHT == dir:
        i = x + 1
        j = y + 1
        willFlip = matrix[i][j]
        while value != willFlip and i < (BROAD_SIZE - 1) and j < (BROAD_SIZE - 1):
            i = i + 1
            j = j + 1
            willFlip = matrix[i][j]
        if willFlip == value:
            for f in xrange(i, x, -1):
                matrix[f][j] = value
                j = j - 1
            return True
        else:
            return False
    elif RIGHT == dir:
        i = y + 1
        willFlip = matrix[x][i]
        while value != willFlip and i < (BROAD_SIZE - 1):
            i = i + 1
            willFlip = matrix[x][i]
        if willFlip == value:
            for f in xrange(i, y, -1):
                matrix[x][f] = value
            return True
        else:
            return False
    elif UPPER_RIGHT == dir:
        i = x - 1
        j = y + 1
        willFlip = matrix[i][j]
        while value != willFlip and i > 0 and j < (BROAD_SIZE - 1):
            i = i - 1
            j = j + 1
            willFlip = matrix[i][j]
        if willFlip == value:
            for f in xrange(i, x):
                matrix[f][j] = value
                j = j - 1
            return True
        else:
            return False

def checkAroundDisc(matrix, x, y, value):
    """
    Check the target position of moving is valid or not.
    (Only check the target position is or isn't stand alone place)
    """

    # Over Bundary testing
    if x > (BROAD_SIZE - 1) or y > (BROAD_SIZE - 1) or x < 0 or y < 0:
        return False

    # Current position testing
    if matrix[x][y] != EMPTY:
        return False

    changed = False;
    if (BROAD_SIZE - 1) == x:
        if (BROAD_SIZE - 1) == y: # right-bottom corner
            if value != matrix[x - 1][y - 1] and -1 != matrix[x - 1][y - 1]:
                changed = changed | flip(UPPER_LEFT, matrix, x, y, value)
            if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
                changed = changed | flip(UP, matrix, x, y, value)
            if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
                changed = changed | flip(LEFT, matrix, x, y, value)
            
        elif 0 == y: # left-bottom corner
            if value != matrix[x - 1][y + 1] and -1 != matrix[x - 1][y + 1]:
                changed = changed | flip(UPPER_RIGHT, matrix, x, y, value)
            if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
                changed = changed | flip(UP, matrix, x, y, value)
            if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
                changed = changed | flip(RIGHT, matrix, x, y, value)

        else: # on bottom boundary not corner
            if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
                changed = changed | flip(UP, matrix, x, y, value)
            if value != matrix[x - 1][y - 1] and -1 != matrix[x - 1][y - 1]:
                changed = changed | flip(UPPER_LEFT, matrix, x, y, value)
            if value != matrix[x - 1][y + 1] and -1 != matrix[x - 1][y + 1]:
                changed = changed | flip(UPPER_RIGHT, matrix, x, y, value)
            if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
                changed = changed | flip(LEFT, matrix, x, y, value)
            if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
                changed = changed | flip(RIGHT, matrix, x, y, value)

    elif 0 == x:
        if 7 == y: # right-top corner
            if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
                changed = changed | flip(LEFT, matrix, x, y, value)
            if value != matrix[x + 1][y - 1] and -1 != matrix[x + 1][y - 1]:
                changed = changed | flip(LOWER_LEFT, matrix, x, y, value)
            if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
                changed = changed | flip(DOWN, matrix, x, y, value)
        elif 0 == y: # left-top corner
            if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
                changed = changed | flip(RIGHT, matrix, x, y, value)
            if value != matrix[x + 1][y + 1] and -1 != matrix[x + 1][y + 1]:
                changed = changed | flip(LOWER_RIGHT, matrix, x, y, value)
            if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
                changed = changed | flip(DOWN, matrix, x, y, value)
        else: # on top boundary not corner
            if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
                changed = changed | flip(LEFT, matrix, x, y, value)
            if value != matrix[x + 1][y - 1] and -1 != matrix[x + 1][y - 1]:
                changed = changed | flip(LOWER_LEFT, matrix, x, y, value)
            if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
                changed = changed | flip(DOWN, matrix, x, y, value)
            if value != matrix[x + 1][y + 1] and -1 != matrix[x + 1][y + 1]:
                changed = changed | flip(LOWER_RIGHT, matrix, x, y, value)
            if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
                changed = changed | flip(RIGHT, matrix, x, y, value)
    elif 0 == y:
        if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
            changed = changed | flip(UP, matrix, x, y, value)
        if value != matrix[x - 1][y + 1] and -1 != matrix[x - 1][y + 1]:
            changed = changed | flip(UPPER_RIGHT, matrix, x, y, value)
        if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
            changed = changed | flip(RIGHT, matrix, x, y, value)
        if value != matrix[x + 1][y + 1] and -1 != matrix[x + 1][y + 1]:
            changed = changed | flip(LOWER_RIGHT, matrix, x, y, value)
        if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
            changed = changed | flip(DOWN, matrix, x, y, value)
    elif (BROAD_SIZE - 1) == y:
        if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
            changed = changed | flip(UP, matrix, x, y, value)
        if value != matrix[x - 1][y - 1] and -1 != matrix[x - 1][y - 1]:
            changed = changed | flip(UPPER_LEFT, matrix, x, y, value)
        if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
            changed = changed | flip(LEFT, matrix, x, y, value)
        if value != matrix[x + 1][y - 1] and -1 != matrix[x + 1][y - 1]:
            changed = changed | flip(LOWER_LEFT, matrix, x, y, value)
        if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
            changed = changed | flip(DOWN, matrix, x, y, value)
    else:
        # Not on the boundary
        if value != matrix[x - 1][y] and -1 != matrix[x - 1][y]:
            changed = changed | flip(UP, matrix, x, y, value)
        if value != matrix[x - 1][y - 1] and -1 != matrix[x - 1][y - 1]:
            changed = changed | flip(UPPER_LEFT, matrix, x, y, value)
        if value != matrix[x][y - 1] and -1 != matrix[x][y - 1]:
            changed = changed | flip(LEFT, matrix, x, y, value)
        if value != matrix[x + 1][y - 1] and -1 != matrix[x + 1][y - 1]:
            changed = changed | flip(LOWER_LEFT, matrix, x, y, value)
        if value != matrix[x + 1][y] and -1 != matrix[x + 1][y]:
            changed = changed | flip(DOWN, matrix, x, y, value)
        if value != matrix[x + 1][y + 1] and -1 != matrix[x + 1][y + 1]:
            changed = changed | flip(LOWER_RIGHT, matrix, x, y, value)
        if value != matrix[x][y + 1] and -1 != matrix[x][y + 1]:
            changed = changed | flip(RIGHT, matrix, x, y, value)
        if value != matrix[x - 1][y + 1] and -1 != matrix[x - 1][y + 1]:
            changed = changed | flip(UPPER_RIGHT, matrix, x, y, value)

    return changed

def move(matrix, x, y, value):
    if not checkMatrix(matrix):
        print "check Matrix error"
        return False
    if not checkAroundDisc(matrix, x, y, value):
        print "check AroundDisc error"
        return False

    matrix[x][y] = value

    return True

def main():
    matrix = initGame()
    render(matrix)

    x = 3
    y = 5
    print "move to(%d, %d)" % (x + 1 , y + 1)
    if not move(matrix, x, y, BLACK):
        print "Position(%d, %d) is not valid." % (x + 1, y + 1)
    else: 
        render(matrix)

    x = 2
    y = 3
    print "move to(%d, %d)" % (x + 1, y + 1)
    if not move(matrix, x, y, WHITE):
        print "Position(%d, %d) is not valid." % (x + 1, y + 1)
    else: 
        render(matrix)

    x = 4
    y = 2
    print "move to(%d, %d)" % (x + 1, y + 1)
    if not move(matrix, x, y, BLACK):
        print "Position(%d, %d) is not valid." % (x + 1, y + 1)
    else: 
        render(matrix)

    x = 3
    y = 6
    print "move to(%d, %d)" % (x + 1, y + 1)
    if not move(matrix, x, y, WHITE):
        print "Position(%d, %d) is not valid." % (x + 1, y + 1)
    else: 
        render(matrix)

if __name__ == "__main__":
    main()