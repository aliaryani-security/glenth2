import sys
import os

def __move_to_bottom() :
    rows = os.get_terminal_size().lines
    print (f"\033[{rows};O", end='')

def __clear_line() :
    print("\033[K", end='')

# def log_line (text):
#     print(text)

def update_bottom_line (value):
    __move_to_bottom()
    __clear_line()
    print (value, end='\r')
    sys.stdout.flush()