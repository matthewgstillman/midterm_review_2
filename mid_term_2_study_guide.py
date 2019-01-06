#Functions:
#1. Need to know all functions written in labs and homeworks

#Write a function that accepts a word (string) and prints out whether the word is a palindrome. This
#function does not need to return anything.
#(Hint: Use [::-1])
#palindrome(“happy”)
#This word is not a palindrome
#palindrome(“hannah”)
#This word is a palindrome

my_string = "racecar"
def palindrome(string):
    first = 0
    last = len(my_string) - 1
    while first < last:
        if my_string[first] != my_string[last]:
            print("Error! This string is NOT a palindrome!")
        else:
            print("Going good so far!")
            first += 1
            last -= 1
    if my_string[first] == my_string[last]:
        print("The string {} is MOST DEFINITELY a palindrome!".format(my_string))  
palindrome(my_string)


#3. A hex number can only use these following characters "0123456789ABCDEF" (Hint: Use the in
#operator). Write a function called isHex(). It takes in a string and determines if the number is
#hexadecimal. It returns true or false

def isHex(hexnumber):
  import string
  result = string.ascii_letters
  length = len(hexnumber)
  good_digit_count = 0

  for i in range(0, len(hexnumber)):
    if hexnumber[i] in result[26:32] or int(hexnumber[i]) in range(0,10):
      print("Good So Far!")
      good_digit_count += 1
    else:
      print("Sorry! {} is not a properly formatted hexadecimal number!".format(hexnumber))

  if good_digit_count == length:
    print("Success! {} is a proper hexadecimal number!".format(hexnumber))
    return(True)
  else:
    print("Fail! This is NOT a properly formatted hexadecimal number!")
    return(False)


isHex("002B5C")


#4. Write a program that takes in a string of characters and returns the longest value-ascending string
#starting from the first position of the string. It means that, in the string, each subsequent character is
#greater than the previous one. Use the ASCII value table
#For example, ‘a’ is greater than “_” but it is smaller than “|”
#For example, given a string ”abcdefgzab” , it will return the longest string “abcdefgz” because it stops at
#the a after z

my_str = "abcdefgzab"

def ascii_length(str):
  my_str = "abcdefgzab"
  new_str = ""
  for i in range(0, len(my_str)):
    print("{} - {}".format(my_str[i], ord(my_str[i])))
    if int(ord(my_str[i])) < 122:
      new_str += my_str[i]
    elif int(ord(my_str[i])) == 122:
      new_str += my_str[i]
      print("Longest String in {}: {}".format(my_str, new_str))
      break
    elif ord(i) > 122:
      print("Longest String in {}: {}".format(my_str, new_str))

ascii_length(my_str)


#2. Write a function that returns the square of a number given
def return_square(number):
    square = number * number
    print("{} squared is {}".format(number, square))

return_square(2)


#3. Write a function that returns the negative number given an integer. If the number is
#positive, return the negative number. If the number is negative, return the same
#number

def get_negative(number):
    if number < 0:
        print("Number {} already less than zero")
        return number
    elif number > 0:
        negative = number * -1
        print("Number {} is now equal to {}".format(negative, number))

get_negative(15)

#4. Write a function that returns a number 3 times as much as the number given

def three_times(number):
    three_timer = number * 3
    print("{} * 3 = {}".format(number, three_timer))

three_times(5)

#5. Write a function that returns 1 if the given number is a multiple of 5.

def no_five_mult(number):
    if number % 5 == 0:
        print("{} is a multiple of five! Now equal to 1".format(number))
        return 1
    else:
        print("{} is not a multiple of 5".format(number))
        return 5

no_five_mult(5)


#6. Write a function that returns the sum of all elements in the list given.

def sum_list(my_list):
    list_sum = 0
    for i in range(0, len(my_list)):
        list_sum += my_list[i]

    print("Final sum of list: {}".format(list_sum))


sum_list([1,2,3,4,5,6,7,8,9,10])


#7. Write a function that accepts 2 (x,y) coordinates and returns the distance between them

def distance(x1,y1,x2,y2):
    import math
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Distance between ({},{}) and ({},{}) is {}".format(x1,y1,x2,y2, distance))

distance(2,3,5,6)

#8. Write a function that accepts 1 (x,y) coordinate and prints out whether it is in the first,
#second, third, or fourth quadrant

def quadrant_locator(x,y):
    if x > 0 and y > 0:
        quadrant = "I"
    elif x < 0 and y > 0:
        quadrant = "II"
    elif x < 0 and y < 0:
        quadrant = "III"
    elif x > 0 and y < 0:
        quadrant = "IV"

    print("X Y Coordinates ({},{}) are located in Quadrant {}".format(x, y, quadrant))

quadrant_locator(1,2)

#9. Write a function that accepts 2 coordinates and prints out whether they form a vertical
#line or a horizontal line
#void function - doesnt return things
#if x values are same = horizontal
#if y values are same = vertical

#10. Write a function that accepts a tuple and returns a sorted list

def tuple_to_sorted_list(my_tuple):
    my_list = list(my_tuple)
    sorted_list = sorted(my_list)
    print("Sorted List: {}".format(sorted_list))

tuple_to_sorted_list((2,3,1))

#11. Write a function that accepts a list and returns a sorted tuple

def list_to_sorted_tuple(my_list):
    my_tuple = tuple(my_list)
    print("My Tuple: {}".format(my_tuple))
    sorted_tuple = tuple(sorted(my_tuple))
    print("Sorted Tuple: {}".format(sorted_tuple))


list_to_sorted_tuple([2,3,4,1])

#12. Write a function that return the pig latin verion of a word given. For example, Python
#becomes ythonpay

def pig_latin(string):
    latin_part = string[0] + "ay"
    pig_string = string[1:] + latin_part
    print("{} in Pig Latin is {}".format(string.title(), pig_string.title()))

pig_latin("poop")


#Recursive function: (short question only)
#1. Factorial function on the slide



#2. Fibonacci sequence on the slide
#DOESN'T WORK RIGHT
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci = fib(n-1) + fib(n-2)
        print(fibonacci)
        fib(n-1) + fib(n-2)

fib(5)


#3. Monkey and message function

def Monkey(n):
    if n == 1:
        print("{} monkeys jumping on the bed!".format(n))
    else:
        print("{} monkeys jumping on the bed!".format(n))
        Monkey(n-1)

Monkey(5)

#4. All recursive functions in your lab and homework.

def rec_print(n):
    if n != 1:
        rec_print(n-1)
        print("n = {}".format(n))
    else:
        print("n = {}".format(n))
    
rec_print(5)

def recur_asterisk(n):
    if n != 1:
        recur_asterisk(n-1)
        print(n * "*")
    else:
        print(n * "*")
        return("n = {}".format(n))


recur_asterisk(5)
#5. Need to know how to find the total number of calls. Need to know what is returned
#for these recursive functions

#For loops
#for i in [1,2,3,4,5,6,7,8,9,10]:
#print i
#Output: "Error! Print Statement must have parenthesis"

#list1 = [1,4,5,6,7,8,9,10]

#for i in list1:
#print(i+1)
#Output: "Error! Indentation Block Expected!"
#Indented Output: 2\n5\n6\n7\n8\n9\n10\n11

#for i in list1:
#print(list1[0])
#Output: "Error! Indentation Block Expected!"
#Indented Output: 1

#list1 = [2,3,2,3,2,3,4]
#for i in list1:
#print(list1[i+1])
#Output: "Error! Indentation Block Expected!"
#Indented Output: 3\n2\n3\n2\n3\n
#THE LAST 4 IS NOT PRINTED!


#for i in range(0,6,2):
#print list1[i]
#Output: "Error! Missing Parenthesis! Indentation Block Expected!"
#Indented Output:

#string = "cat"
#for i in string:
#print i
#Output: c\na\nt\n
#Output: "Error! Missing parenthesis and Indentation Block"

#for i in range(len(string)):
#print string[i]
#Output: "Error! Missing parenthesis and Indentation Block"

#for i in string:
#print string[i]
#Needs range! String indices must be integers
#Output: "Error! Missing parenthesis and Indentation Block"

#for i in range(len(string)):
#print len(string)
#Output: "Error! Missing parenthesis and Indentation Block"
#Programs:
#1.
#def func (num1, num2, num3=4):
#print(num1*num2+num3)
func(3,2,0)
#6
func(3,2)
#10
func(num2=1,num1=4,num3=9)
#13

2.
a=40
b=a
c=[b]
print(a,b,c)?
#40 40 [40]
del a
b=100
c[0]=-1
print(b,c)
#100 [-1]

3. list1=['a','b','c']
list2=list1
#list2 = ['a','b','c']
list3=list4=list2
#list3 = ['a','b','c'] 
#list4 = ['a','b','c']
list1.append([1,2,3])
#list1 = ['a','b','c',[1,2,3]]
#len(list1)
len(list1) = 4


#4. list1=[1,2,3,4,5,6]
#list1[2:4]
#list1[2:4] = [3,4]
#list1[-3]
#4


5. def printinfo( name, age = 35 ):
    print ("Name: ", name)
    print ("Age ", age)
 # Now you can call printinfo function
printinfo( age=50, name="miki")
#Name: miki
#Age 50
printinfo( "miki" )
#Name: miki
#Age: 35


Correct these statements if needed
1. a,b=3,4
a,a=b,b # User wants to swap a and b
#Output: 4 4 (Two fours)
2. def func(num1=4,num2,num3)
3. alist=[‘a’,’b’,’c’]
alist=alist.upper()
#Output: AttributeError: 'list' object has no attribute 'upper'
4. alist=[‘a’,’b’,’c]
alist=alist.append(‘d’)
#Output: SyntaxError: EOL while scanning string literal
#Output if c is an enclosed string: ['a','b','c','d']
5. list1 = ['2',3,4]
print(list1.sort())
#Output: TypeError: '<' not supported between instances of 'int' and 'str'
6. list1=[‘happy’, ‘birthday’, ‘to’, ‘you’]
list2=list1=list3=list4 # user wants to assign them all to list1. Correct?
#Incorrect
#Output: NameError: name 'list4' is not defined

7. ten=[]
ten[0]=2 # I want to add an element to the front of the list
print(ten)
#Output: IndexError: list assignment index out of range

8. # User wants to add a list of spaces. What is wrong
ten=[ , , , ]
#Right Version: ten = [" ", " ", " "]
print(ten[0])
#Output:                    (blank)
9. 
dict={}
dict[0]=909
dict[Bob]=909
#Good?
#No. Bob is a variable that isn't defined


10. #User wants to print h, a, p, p, y lowercase
string="HAPPY"
for i in string:
 print string[i.lower()]
#This will not work - string indices must be numberic values.

#To make this work:
string="HAPPY"
for i in string:
    print(i.lower())


11. print("Happy")
 print("Birthday")
 #Correctly indented output: Happy\nBirthday

12. tuple1=(1,2,3,4)
tuple1.append(5)
#Doesn't work: Tuple Has no attribute append

#To make this work:


13. birthday={jack, 3-10-1990, jill, 3-28-2000} # a dictionary of birth dates
#Error: jack and jill are undefined variables.

14.  
# def Greetings(name="Doc", lastname):
# print("Hello",name,lastname)

#lastname is undefined. Function is uncalled, block unindented
#Making it work
def Greetings(firstname, lastname):
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    print("Hello {} {}!".format(firstname, lastname))

Greetings("Matt", "Stillman")


Misc:
1. What is string module? What do these mean? ascii_lowercase, ascii_uppercase, digits, letter
#When you import the string module (import string), you get access to a library of ascii characters that make up strings
#string.ascii_lowercase prints abcdefghijklmnopqrstuvwxyz
#string.ascii_uppercase prints ABCDEFGHIJKLMNOPQRSTUVWXYZ 
#string.ascii_digits prints 0123456789
#string.ascii.letter prints an error - string.ascii.letters prints abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
2. How do you use the abs() function?
# The abs() function returns the absolute value (distance from zero on a number line) of a number put inside the parenthesis.
absolute_five = abs(-5)
print("Absolute Five: {}".format(absolute_five))

3. What is ord()? What is chr()?
#ord() - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364.
#chr() - Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'.

4. What does the range() function return? For example, what does range(10) return? What does
range(0,20,2) return?
#Range prints all numbers within specified range
#range(10)
for i in range(10):
    print(i)
#Output: 1\n2\n3\n4\n5\n6\n7\n8\n9\n
#range(0,20,2)
for i in range(0, 20, 2):
    print(i)
#Output: 0\n2\n4\n6\n8\n10\n12\n14\n16\n18\n

5. What are the 3 different types of functions? Void vs value-returning. Ones that accept an
argument (required or optional) vs no argument
#Void
#Value-Returning
#Argument
#No Arguement

#6. All string methods on page 38. Write a short program to show how you use each one.
user_string = input("Type in a string: ")
upper_string = user_string.upper()
lower_string = user_string.lower()
swapcase_string = user_string.swapcase()
capitalize_string = user_string.capitalize()
title_string = user_string.title()
strip_string = user_string.strip(" ")
replace_string = user_string.replace("Hello", "Fuck off")
print("User String: {}, Upper Case String: {}, Lower Case String: {}, Swapcase String: {}, Capital String: {}, Title String: {}, Stripped String: {}".format(user_string, upper_string, lower_string, swapcase_string, capitalize_string, title_string, strip_string, replace_string))

#7. All list methods on page 132. Write a short program to show how you use each one.
my_list = [1,2,3,4]
my_list.append(5)
print("My list now has a 5 at the end of it: {}".format(my_list))
one_count = my_list.count(1)
print("Number of times 1 is in my_list: {}".format(one_count))
one_index = my_list.index(1)
print("Index where the number 1 occurs: {}".format(one_index))
inserted_value_list = my_list.insert(5, 5
)
print("Inserted Value List: {}".format(my_list))
popped_last_value = my_list.pop()
print("List With Last Item Popped: {}".format(my_list))
remove_five_list = my_list.remove(5)
reversed_list = my_list.reverse()
print("Reversed List: {}".format(my_list))

#8. What is a list of tuples? What is a tuple of lists?
# List of tuples: list_of_tuples = [(1,2,3), (3,4,5), (6,7,8)]
# Tuple of lists: tuple_of_lists = ([1,2,3], [3,4,5]. [6,7,8])

#9. How do you create a dictionary? Start with a null dictionary, then add
#phonebook[‘Jack’]=789752 (example)
phonebook = {}
phonebook['Jack'] = '408-555-1234'
print("Phonebook: {}".format(phonebook))

#10. Are these mutable or immutable? Strings, tuples, lists, dictionaries
#Strings and tuples are immutable; Dictionaries and Lists are Mutable

#11. How do you ask users to enter 2 words and assign them to word1 and word2 variable?
words = input("Enter 2 words: ").split()
word1 = words[0]
word2 = words[1]
[word1, word2] = input("Enter 2 words").split(",")
word1, word2 = input("Please Enter A Word: "), input("Please Enter Another Word: ")
print("Word 1: {}, Word 2: {}".format(word1,word2))
#What if the user enters 2 words separated by comma? 
