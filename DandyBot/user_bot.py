def noWallsAround(check, x, y):
    return not(check('wall', x-1, y) or check('wall', x, y-1) or check('wall', x+1, y) or check('wall', x, y+1))


def script(check, x, y):

    if check('gold', x, y):
        return 'take'

    if check('level') < 3:
        if check('gold', x, y + 1) != 0:
            return 'down'
        if check('gold', x + 1, y) != 0:
            return 'right'
        if check('gold', x, y - 1) != 0:
            return 'up'

        if check('level') == 1:
            return 'right'
        if check("level") == 2:
            if check('gold', x+2, y) != 0:
                return 'right'
            return 'up'

    if check('level') == 4:
        if x == 4 and y == 13:
            return 'right'
        if x == 10 and y in (12, 13):
            return 'up'

    if check('level') in (3, 4):
        # 1
        if (check('wall', x-1, y) and not check('wall', x, y-1)) or (check('wall', x-1, y-1) and noWallsAround(check, x, y)) or (check('wall', x-1, y) and not check('wall', x, y-1)):
            return 'up'
        # 2
        if (check('wall', x-1, y) and check('wall', x, y-1)) or (check('wall', x, y-1) and not check('wall', x+1, y)) or (check('wall', x+1, y-1) and noWallsAround(check, x, y)):
            return 'right'
        # 5
        if (check('wall', x+1, y) and not check('wall', x, y+1)) or (check('wall', x+1, y+1) and noWallsAround(check, x, y)):
            return 'down'
        # 7
        if check('wall', x-1, y+1) and noWallsAround(check, x, y) or (check('wall', x, y+1) and not check('wall', x-1, y)):
            return 'left'
    return "pass"
