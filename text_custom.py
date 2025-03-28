import random, time, sys, os

def typewriter(text, delay=0.08, clear_after=False):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')
    if clear_after:  # Clear the line after typing is done
        time.sleep(0.2)  # Give a small pause after typing before clearing
        clear_screen()

def to_color(string, color):
    color_code = {'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
                    }
    return color_code[color] + str(string) + '\033[0m'

def load_animation(load_str, speed, length):
    #STOLE THIS FROM YOU MR.WATSON
  # String to be displayed when the application is loading
  ls_len = len(load_str)

  # String for creating the rotating line
  animation = "|/-\\"
  anicount = 0

  # used to keep the track of the duration of animation
  count_time = 0

  # pointer for travelling the loading string
  i = 0
  # smaller value for short time length of animation
  while count_time != length:
    # used to change the animation speed smaller the value, faster will be the animation
    time.sleep(speed)

    # converting the string to list as string is immutable
    load_str_list = list(load_str)

    # x->obtaining the ASCII code
    x = ord(load_str_list[i])
    # y->for storing altered ASCII code
    y = 0

    # if the character is "." or " ", keep it unaltered switch uppercase to lowercase and vice-versa
    if x != 32 and x != 46:
      if x>90:
        y = x-32
      else:
        y = x + 32
      load_str_list[i]= chr(y)

    # for storing the resultant string
    res =''
    for j in range(ls_len):
      res = res + load_str_list[j]

    # displaying the resultant string
    sys.stdout.write("\r"+res + animation[anicount])
    sys.stdout.flush()

    # Assigning loading string to the resultant string
    load_str = res

    anicount = (anicount + 1)% 4
    i =(i + 1)% ls_len
    count_time = count_time + 1

  # for windows OS
  if os.name =="nt":
    pass
    #os.system("cls")
  # for linux / Mac OS
  else:
    os.system("clear")
