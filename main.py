# Programmers:  Donovan,
# Course:  CS151,
# Due Date: november 6h
# Lab Assignment: PA 03
# Problem Statement:  You are creating a program to display ASCII art and string decorations to the user.
# Data In: line character, number of lines, number of charcters in a line,  circle, random, stop,
# Data Out: circle, random image 1, random image 2, random image 3, lines of characters
# Credits: https://www.asciiart.eu/image-to-ascii




import random

# Purpose: outputs a circle using line of o's
# Parameters: none
# Return: circle pattern
def print_circle():
    #outputs my circle pattern
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
    return
# Purpose: outputs a pattern of characters made to look like Mr. Zee
# Parameters: None
# Return: Mr. Zee pattern
def random_image1():
    #https://www.asciiart.eu/image-to-ascii
    #outputs a Dr. Zee Image
    print('\n'
          '                      . ... .............. ...........\n'                
          '                      ...............::::::...........\n'
          '                      ........::-::::::::::---::......\n'
          '                      .....:----::::::::::::::----:...\n'
          '                      ..:-----:::::::::::::::::------:\n'
          '              ........::-----:::::-------:::-:::-------:......\n'
          '              .......:--=----------------------------=---:....\n'
          '              ......--====--------------------------=====-:...\n'
          '              .....-=======-----------------------========--..\n'
          '              ....-==========---------------------==========:.\n'
          '              ...:=++===========----------------=======+=++=-.\n'
          '              ...=+++============---------------========++++=.\n'
          '              ...=+++========--------------------=======++++=:\n'
          '              ...=++++======------------------------===++++++-........\n'
          '              ...=+++++==--------------------------====+++++=-........\n'
          '              ...=++++++++++++++===-------==++*+++++++++++++=-........\n'
          '              ...=++++****+***++=====---====+++**+++**++++++=-........\n'
          '              :-:=+++++++++******+++=---==++*******++++++++++=--=:....\n'
          '              -+=+++++++*##+%%#+***+=---==+**+*%##+##*++==++*+=+*-....\n'
          '              :*+*++==++******++++++=-:--==++++*+++*+++===++**++*-....\n'
          '              .++*+=======+=+=+======-:--======+=======-==++**+++.....\n'
          '              ..+*++==-=--======-===-:::-===---===------==+***+=:.....\n'
          '              ..-**+===---------====-:::---=-----------===+*##+=......\n'
          '              ...**++===--------==----------=----------===+*##+=......\n'
          '              ...#%*+====------===*#*===+**+==-------====++#%#*-......\n'
          '              ..:#%%++====----===++++++++++==------======+*%%##-......\n'
          '              ...+%%#++==========+###*+*##*+============+*#%%#-.......\n'
          '               ..-*%%#++=+++=++*##*+===++++***#*+===+++**#%%%*:    . .\n'
          '              ...:##%%#**+++*#%##***+++*+****#%%%#*+***##%%%%*.  . . .\n'
          '              ....=#%%%%#**##%%##*+========+**##%%####%%%%%%#-.. ..  .\n'
          '              ....:#%%%%%#####*++++=======+++++*####%%%%%%%%+. .  .  .\n'
          '              .  ..:#%%%%%%%##+++++**#*#**+++==+#%%%%%%%%%%#:.\n'
          '              .... .:+#%%%%%%#*+++=+++**++==+++*#%%%%%%%%%+-..\n'
          '              . .... .#%%%%%%%%****++*++++++++*#%%%%%%@%%%=...\n'
          '             ........*%%%@%%%%%#%%############%%%%%@@%%%%+:.. \n'                        
          '.   ..   ..  .......:=#%%%%@%%%%%%%%%%%%%%%%%%%%%@@%%%##%+:..... .  .....  ..\n'            
          '  . ...... ........:-:-##*##%%%%@%@@@%@@%%@%%%%@%%%%##***%+::...... ....... ..\n'            
          '...   ...  .....-+++::-+#***##%%%@@@%%%%@@@@@@%%%##******#=:::==:......... ...\n'            
          '.  ........:-=+++++=:::-+#******################*****++*#*=:::++++==-:..... ..\n'            
          ' .. ..:-===+++*++++=::::=+#*+*******++++++*******+++++**%+=:::++++++++==-... . \n'           
          '++++++++**++**++++*#-::::--+#*+++++++++++++++++++++**#%#-::::++*****+++++++++==-:......  .\n'
          '::-=++++++++***+*++*::::--+#*+++*++*+++++++++++++++++*#%*-:::=+*+++*++++++=-:......... .. \n'
          '++++***++******+*+**--:::::-=#**+++++==+++++++++++*##%+:---::++*****+++++++++++++==-:.....\n'
          '+++++*****+++*+*+*==--:-::::-=#**+++++==++++++++**##+-:---:--=+*****++*++++++++++++++==-..\n'
          '+++++++++++*+*****=:--::-:::::=#***+++++++++++**#*=::--:--:--=++**+***++++++++++++++++++==\n'
          '+*+++****++****+**+:----::=#*::+#*************#*--::----:--::+**+*+***+**+++++++++++++++++\n'
          'Image of Dr.Zee')


# Purpose: Outputs the letter d using D's
# Parameters: none
# Return: the D pattern
def random_image2():
    #outputs the letter z
    print('            iiii\n'
          '            iiii\n'
          '\n'
          '\n'
          '')
    print('iiiiiiiiiiiiiiii')
    for i in range(0, 5):
        print("              i\n")
    print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    print('The letter i')


# Purpose: Prints a box
# Parameters: none
# Return: the box pattern
def random_image3():
    #outputs a box
    print('------------------------------------------------------------------')
    for i in range(0,12):
        print('|                                                                |')
    print('------------------------------------------------------------------')

# Purpose: outputs line/s of a character after inputting which character you want
# Parameters: (num_lines, num_char) The number of lines and the amount of character/s per line
# Return: the string pattern
def lines_output(num_lines, num_char):
    #asks for the character that you want to use and prints it using the other 2 parameters that you inputted before
    char = input("Enter a character to use: ")
    for num in range(0, num_lines):
        print(char * num_char)


# Purpose: coordinates the function to the right path depending on what random number we get
# Parameters: the random number x
# Return: a coordinated program to help output the random patterns
def randomi(x):
    #decides what get outputted after x is assigned to a random number between 1 and 3
    if x == 1:
        random_image1()
    elif x == 2:
        random_image2()
    elif x == 3:
        random_image3()

# Purpose: displays a menu of choices and force the user to choose an input
# Parameters: none
# Return: Choice
def choices():
    #displays the menu and forces you to choose one of the options
    choice = input('The image choices are \n'
                    '\t Circle -- outputs the pattern for a circle\n'
                    '\t Line -- outputs line of a set of characters that you choose\n'
                    '\t Random -- outputs 1/3 random patterns\n'
                    '\t Please input "stop" if you would like to stop\n'
                    '').strip().lower()
    while choice not in ['line','circle','random','stop'] :
        print('Please choose one of the following options')
        choice = input('The image choices are \n'
                        '\t Circle -- outputs the pattern for a circle\n'
                        '\t Line -- outputs lines of a set of characters that you choose\n'
                        '\t Random -- outputs 1/3 random patterns\n'
                        '\t Please input "stop" if you would like to stop\n'
                        '').strip().lower()
    return choice


# Purpose: Main function to repeat and coordinate the program down the right paths
# Parameters: none
# Return:
def main():
    #creates a loop with the sentinel end
    loop = ''
    while loop != 'end':
        #sets choice to the return in the choices function
        choice = choices()

        #depending on your choice you are taken down one of the if else paths
        if choice == 'circle':
            print_circle()

        elif choice == 'line':
            #explains how to use the function to the users
            print('In order to create a line pattern you must input your number of lines and \n'
                  'how many times you want your character(s) to be repeated in each line.\n')

            #Gets the parameters for the lines output function
            num_char = input('How many times you want your character(s) to be repeated in each line. ')
            while not num_char.isdigit():
                num_char = input('How many times you want your character(s) to be repeated in each line. ')
            num_char = int(num_char)

            num_lines = input('How many lines do you need.' )
            while not num_lines.isdigit():
                num_lines = input('How many lines do you need. ')
            num_lines = int(num_lines)

            # calls the lines output function
            lines_output(num_lines, num_char)

        elif choice == 'random':
            x = random.randint(1, 3)
            randomi(x)

        elif choice == 'stop':
            loop = 'end'

#calls the main function
main()