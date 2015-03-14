# 2015 MBU Programming Assignment 2
#
# Write a program that will take several inputs on the command line and
# determine if the numbers are odd or even.
#
# Run the program by using the terminal by typing:
# "python mbu_assignment.py number1_input number2_input number3_input"
#
# You can access the arguments on the command line by using the object sys.argv
# sys.argv[0] is the name of the file. sys.argv[1] is the first argument.
#
# The demo program prints out the arguments on the command line. Please
# modify the program to accomplish the goal.
#
# You will need to do a few things to successfully complete the project including:
#          * Use a loop through an arbitrary number of inputs. Stop when you run out of inputs.
#          * Converting strings to integers (Hint -- Use the string.atoi() function)
#          * Use some mathematical tricks to determine if the number is odd or even.
#                Hint -- what unique property do even numbers have?
#          
# What happens if you enter a value that is not a number?
#

import sys
import string

def main():

    #Remember that the first element (element 0) of sys.argv is the program name.
    print "The name of the script is " + str(sys.argv[0])+"."
    #Remember to convert numbers into strings before printing them.
    print "You have entered " + str(len(sys.argv[1:])) + " numbers"

    #This is for loop. We take each element from sys.argv and print it to the consile.
    for i in sys.argv[1:]:
    
        a = int (i)
             
        b = a % 5   
        print a, " % 5 is", b
              
        print a, " % 5 is", a % 5
  
        print str(a)
        if a % 2 == 0:
            print "This number is even"
        if a % 2 == 1:
            print "This number is odd"
            
        if a % 3 == 0:
            print "This number is divisible by three"
        if a % 3 > 0:
            print "This number is not divisible by three"

        if a % 4 == 0:
            print "This number is divisible by four"
        if a % 4 >= 1:
            print "This number is not divisible by four"
            
        if a % 5 == 0:
            print "This number is divisible by five"
        if a % 5 == 1:
            print "This number is not divisible by five"

        if a % 6 == 0:
            print "This number is divisible by six"
        if a % 6 == 1:
            print "This number is not divisible by six"
        if a % 7 == 0:
            print "This number is divisible by seven"
        if a % 7 == 1:
            print "This number is not divisible by seven"
        if a % 8 == 0:
            print "This number is divisible by eight"
        if a % 8 == 1:
            print "This number is not divisible by 8"
        if a % 9 == 0:
            print "This number is divisible by nine"
        if a % 9 == 1:
            print "This number is not divisible by nine"

        if a % 10 == 0:
            print "This number is divisible by ten"
        if a % 10 == 1:
            print "This number is not divisible by ten"
            
        print "\n"

if __name__ == '__main__':
    main()