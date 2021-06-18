import random

class Convert:

    def start(level1):
        genrow = level1[-1]
        gencolumn = level1[-2]
        heigh = level1[-3]
        width = level1[-4]
        Convert.cut(genrow, gencolumn, level1, width, heigh)

    def cut(genrow, gencolumn, level1, width, heigh):
        x = ((genrow - 1) * width + gencolumn) * 4
        y = x - 4
        print(x, y)
        room = level1[y:x]
        Level.gen(room, genrow, gencolumn, level1)


class Level:

    def gen(room, genrow, gencolumn, level1):
        print('You are currently in: row ', genrow, ' and column ', gencolumn)

        if(room[0] > 0):
            n = '1'
        else:
            n = '-'

        if (room[1] > 0):
            e = '2'
        else:
            e = '-'

        if (room[2] > 0):
            s = '3'
        else:
            s = '-'

        if (room[3] > 0):
            w = '4'
        else:
            w = '-'

        print('----[', n, ']----')
        print('[', w, ']-----[', e, ']')
        print('----[', s, ']----')

        Choice.roomchoose(room, level1)

    def move(choice, room, level1, c):
        if(choice == 0):
            print('Ooops... You can\'t go here')

        elif(choice == 1):
            if (c == 1):
                level1[-1] = int(level1[-1]) - 1

            elif (c == 2):
                level1[-2] = int(level1[-2]) + 1

            elif (c == 3):
                level1[-1] = int(level1[-1]) + 1

            elif (c == 4):
                level1[-2] = int(level1[-2]) - 1

        elif(choice == 2):
            Level.teleport(heigh, width, genrow, gencolumn)

        elif(choice == 3):
            print('You escaped! Now come back to your boring life...')

    def teleport(heigh, width, genrow, gencolumn):
        genrow = random.randint(1, heigh)
        gencolumn = random.randint(1, width)


class Choice:

    def roomchoose(room, level1):
        c = int(input())
        c = c - 1
        choice = room[c]

        Level.move(choice, room, level1, c)


stage = 1
row = 0
column = 0

level1 = [0, 1, 1, 0,  # Row 1
          0, 0, 1, 1,
          0, 2, 1, 0,

          1, 2, 1, 0,  # Row 2
          1, 0, 0, 1,
          1, 3, 1, 0,

          1, 1, 0, 0,  # Row 3
          0, 1, 2, 1,
          1, 1, 0, 1,

          3, 3, 1, 1]  # Last 4 digits are: columns, rows, starting column, starting row


class Game:

    while(0<1):
        Convert.start(level1)