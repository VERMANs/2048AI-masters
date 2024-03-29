import os


# getKey():
# 	Waits for a keyboard input and determines which key was pressed, up, down, left or right.
#	It supports windows, linux and OSX
#	returns:
#		'up', 'down', 'left' or 'right' respectively if the up, down, left or right keys are pressed.
#		None is returned, otherwise.

def getKey():
    # if windows
    if os.name == 'nt':

        from msvcrt import getch
        UP, DOWN, LEFT, RIGHT = 80, 72, 75, 77
        key = ord(getch())

        if key == 224:
            key = ord(getch())

            if key == 80:
                return 'down'

            elif key == 72:
                return 'up'

            elif key == 75:
                return 'left'

            elif key == 77:
                return 'right'

        return None
    # not windows
    else:
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)

        tty.setraw(fd)
        c = sys.stdin.read(3)
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

        print(c)
        if c == '\x1b[A':
            return 'up'
        elif c == '\x1b[B':
            return 'down'
        elif c == '\x1b[C':
            return 'right'
        elif c == '\x1b[D':
            return 'left'
