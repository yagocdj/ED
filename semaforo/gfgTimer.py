# timer by GeeksForGeeks
import time

# define the countdown function


def countdown(t: int) -> None:
    # It's the same as "while t != 0" because 0 == False
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = int(input('Enter the time in seconds: '))

# function call
countdown(t)
