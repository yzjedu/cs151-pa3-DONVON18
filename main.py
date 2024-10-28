import random


# Code goes here and DO NOT FORGET INTRO COMMENTS




def circle():
    print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
          "oooooooooooooooooooooooooooooooo                  oooooooooooooooooooooooooooooooo\n"
          "oooooooooooooooooooooooo                                  oooooooooooooooooooooooo\n"
          "oooooooooooooooooo                                              oooooooooooooooooo\n"
          "oooooooooooooo                                                      oooooooooooooo\n"
          "oooooooooooo                                                           ooooooooooo\n"
          "ooooooooo                                                                ooooooooo\n"
          "ooooooo                                                                    ooooooo\n"
          "ooooo                                                                        ooooo\n"
          "oooo                                                                          oooo\n"
          "ooo                                                                            ooo\n"
          "oo                                                                              oo\n"
          "oo                                                                              oo\n"
          "o                                                                                o\n"
          "o                                                                                o\n"
          "o                                                                                o\n"
          "o                                                                                o\n"
          "o                                                                                o\n"
          "oo                                                                              oo\n"
          "oo                                                                              oo\n"
          "ooo                                                                            ooo\n"
          "oooo                                                                          oooo\n"
          "ooooo                                                                        ooooo\n"
          "ooooooo                                                                    ooooooo\n"
          "ooooooooo                                                                ooooooooo\n"
          "oooooooooooo                                                           ooooooooooo\n"
          "oooooooooooooo                                                      oooooooooooooo\n"
          "oooooooooooooooooo                                              oooooooooooooooooo\n"
          "oooooooooooooooooooooooo                                  oooooooooooooooooooooooo\n"
          "oooooooooooooooooooooooooooooooo                  oooooooooooooooooooooooooooooooo\n"
          "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
def lines_output(num_lines, num_char):
    char = input("Enter a character to use: ")
    for num in range(0, num_lines):
        print(char * num_char)

def choices():
    choice = input('The image choices are \n'
                    '\t 1. circle -- outputs the pattern for a circle\n'
                    '\t 2. line -- outputs line of a set of characters that you choose\n'
                    '\t 3. random -- outputs 1/3 random patterns\n'
                    '\t Please input "stop" if you would like to stop\n'
                    '').strip().lower()
    while choice not in ['line','circle','random','stop'] :
        print('Please choose one of the following options')
        choice = input('The image choices are \n'
                        '\t 1. circle -- outputs the pattern for a circle\n'
                        '\t 2. line -- outputs lines of a set of characters that you choose\n'
                        '\t 3. random -- outputs 1/3 random patterns\n'
                        '\t Please input "stop" if you would like to stop\n'
                        '').strip().lower()
    return choice

def main():
    loop = ''
    while loop != 'end':
        choice = choices()
        if choice == 'circle':
            circle()
        elif choice == 'line':
            print('In order to create a line pattern you must input your number of lines and \n'
                  'how many times you want your character(s) to be repeated in each line.\n')
            num_char = input('How many times you want your character(s) to be repeated in each line. ')
            while not num_char.isdigit():
                num_char = input('How many times you want your character(s) to be repeated in each line. ')
            num_char = int(num_char)

            num_lines = input('How many lines do you need.' )
            while not num_lines.isdigit():
                num_lines = input('How many lines do you need. ')
            num_lines = int(num_lines)
            lines_output(num_lines, num_char)
        elif choice == 'random':
            ###### do something or this later
        elif choice == 'stop':
            loop = 'end'
main()