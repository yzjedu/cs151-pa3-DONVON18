- **Name: Main**
- **Parameters: **
- **Return:**
- **Algorithm:**
1.  choices = to empty string
2. while choices is not end
   1. set choice to choices()
   2. print thank you for choosing. We will start 
   generating your (choices) image. 
   3. if the user chose circle
      1. return circle 
   4. if the user chose lines
      1. explain how to use lines and ask the user how 
      many lines the user want and save as num_lines
      2. while the user input isn't a digit
         1. ask again and save as num_lines
      3. ask the user how many times the user wants the 
      character to be repeated in each line and save it
      as num_char
      4. while the user input isn't a digit
         1. ask again
      5. call lines_output(num_char, num_lines)
   5.  if the user chose random
      1. set x to a random number between 1 and 3
      2. return random(x)

    
- **Name: choices**
- **Parameters:**
- **Return:**
- **Algorithm:**
1. display choices and the user what type of design they 
want or if they want to stop
2. while it is not one of the 3 choices
   1. ask the user again


- **Name: Random**
- **Parameters: x**
- **Return:**
- **Algorithm:**
1. if x is 1
   1. print my first image
2. if x is 2
   1. print my second image
3. if x is 3
   1. print online image

    
- **Name: circle**
- **Parameters:**
- **Return: circle image**
- **Algorithm:**
1. print a circle image


- **Name: line_output**
- **Parameters: num_char, num_lines**
- **Return:**
- **Algorithm:**
1. ask the user what character(s) they want to use and 
save it as string
2. For the amount of num_lines
   1. print the string times the num_char
