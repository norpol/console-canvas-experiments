#!/usr/bin/env python3
from shutil import get_terminal_size

term = get_terminal_size((80, 20))

arms = ['/', '\\', '|']
heads = ['o', '°']
fps = 3

# inf = infinite, 1s = duration
duration =  'inf'

# reverse, default is non-reverse
playback = 'non-reverse'


def return_random_element(elements):
    import random
    secure_random = random.SystemRandom()
    return secure_random.choice(elements)


def return_person(arms, heads):
    import random
    left_arm = return_random_element(arms)
    right_arm = return_random_element(arms)
    head = return_random_element(heads)
    return str(left_arm + head + right_arm)


def fps_to_secs(fps):
    return float(1)/fps


def print_loop(frames, arms, heads, interval):
    import time
    import curses

    stdscr = curses.initscr()
    duration = fps_to_secs(interval)
    curses.curs_set(0)  # invisible

    try:
        while True:
            frame = frames(arms, heads)
            frame_height = sum(1 for line in frame)
            canvas_height = int(term[1]/2 - frame_height/2)
            canvas_width = int(term[0]/2 - len(frame)/2)

            canvas = str('\n' * canvas_height) + str(' ' * canvas_width) + frame

            print(canvas, end='')
            time.sleep(duration)

            print(u'\33[A\r' * int(canvas_height), end='')
    except KeyboardInterrupt:
        print('')
        curses.curs_set(1)  # visible
        curses.endwin()


print_loop(return_person, arms, heads, fps)
