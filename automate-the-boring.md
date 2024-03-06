# Chapter 1 Questions

<pre>
<b>1. Which of the following are operators, and which are values?</b>
*
'hello' - Value
-88.8   - Value
- - Operator
/       - Operator
+ - Operator
5       - Value
</pre>
<pre>
<b>2. Which of the following is a variable, and which is a string?</b>
spam    - Variable
'spam'  - String, strings are "quoted"
</pre>
<pre>
<b>3. Name three data types.</b>
    - Bool
    - String
    - Int
</pre>
<pre>
<b>4. What is an expression made up of? What do all expressions do?</b>
An expression is made up of variables and operators. they always reduce down to a single value.
</pre>
<pre>
<b>5. This chapter introduced assignment statements, like spam = 10. What
is the difference between an expression and a statement?</b>
"In summary, expressions are used to produce new values, statements are used to perform actions or operations." - Quora.
</pre>
<pre>
<b>6. What does the variable bacon contain after the following code runs?</b>
bacon = 20
bacon + 1

Still 20, bacon + 1 doesnt assign + 1 to bacon.
</pre>
<pre>
<b>7. What should the following two expressions evaluate to?</b>
'spam' + 'spamspam' - 'spamspamspam'
'spam' * 3 - 'spamspamspam'
</pre>
<pre>
<b>8. Why is eggs a valid variable name while 100 is invalid?</b>
Variables cannot start with digits.
</pre>
<pre>
<b>9. What three functions can be used to get the integer, floating-point
number, or string version of a value?</b>
int(), float(), str()
</pre>
<pre>
<b>10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.</b>
You cannot concatenate ints and strings. str(99) to fix.
</pre>

# Chapter 2 Questions

<pre>
<b>1.What are the two values of the Boolean data type? How do you write them?</b>
True and False.
</pre>
<pre>
<b>2. What are the three Boolean operators?</b>
and, or, not
</pre>
<pre>
<b>3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean
values for the operator and what they evaluate to).</b>
</pre>
|            | True  | False |
|------------|-------|-------|
| True and   | True  | False |
| False and  | False | False |
| True or    | True  | True  |
| False or   | True  | False |
| not True and | False | True |
| not False and | True | True |
<pre>
<b>4. What do the following expressions evaluate to?</b>
(5 > 4) and (3 == 5)                - False
not (5 > 4)                         - False
(5 > 4) or (3 == 5)                 - True
not ((5 > 4) or (3 == 5))           - False
(True and True) and (True == False) - False
(not False) or (not True)           - True
</pre>
<pre>
<b>5. What are the six comparison operators?</b>
>, <, ==, !=, >=, <=
</pre>
<pre>
<b>6. What is the difference between the equal to operator and the assignment operator?</b>
Equal (==) checks if two statements are equal and returns a bool.
An assignment operator assigns something to a variable.
</pre>
<pre>
<b>7. Explain what a condition is and where you would use one.</b>
A condition is an expression that evaluates to True or False and controls wheter something happens. Required in a while-loop.
</pre>
<pre>
<b>8. Identify the three blocks in this code:</b>
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
</pre>
<pre>
<b>9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if
anything else is stored in spam.</b>
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
</pre>
<pre><b>10. What keys can you press if your program is stuck in an infinite loop?</b>
CTRL+C
</pre>
<pre>
<b>11. What is the difference between break and continue?</b>
break exits out of a loop. continue goes to the next iteration.
</pre>
<pre>
<b>12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?</b>
None, they are all the same.
</pre>
<pre>
<b>13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.</b>
for i in range(11):
    print(i)

i = 0
while i != 10:
    print(i)
    i += 1
</pre>
<pre>
<b>14. If you had a function named bacon() inside a module named spam, how would you call it after importing
spam?</b>
spam.bacon()
</pre>

# Chapter 3 Options

<pre>
<b>1. Why are functions advantageous to have in your programs?</b>
They break down programs into smaller parts and allow for easier flow control.
</pre>
<pre>
<b>2. When does the code in a function execute: when the function is defined or
when the function is called?</b>
When the function is called.
</pre>
<pre>
<b>3. What statement creates a function?</b>
def
</pre>
<pre>
<b>4. What is the difference between a function and a function call?</b>
A function is just the definition and code of the function laying dormant. The function call actually executes the function and evaluates return calls.
</pre>
<pre>
<b>5. How many global scopes are there in a Python program? How many local
scopes?</b>
There's one global, and infinite local scopes.
</pre>
<pre>
<b>6. What happens to variables in a local scope when the function call returns?</b>
They are destoyed.
</pre>
<pre>
<b>7. What is a return value? Can a return value be part of an expression?</b>
Its a value returned to whatever called the function, it can be part of an expression.
</pre>
<pre>8. If a function does not have a return statement, what is the return value of a
call to that function?</b>
None
</pre>
<pre>
<b>9. How can you force a variable in a function to refer to the global variable?</b>
Write global "variable" before the variable is used.
</pre>
<pre>
<b>10. What is the data type of None?</b>
A NoneType.
</pre>
<pre>
<b>11. What does the import areallyourpetsnamederic statement do?</b>
</pre>
Imports the module areallyourpersnamederic to your program.
<pre>
<b>12. If you had a function named bacon() in a module named spam, how would you
call it after importing spam?</b>
spam.bacon()
</pre>
<pre>
<b>13. How can you prevent a program from crashing when it gets an error?</b>
Do a try: except "error": catch.
</pre>
<pre>
<b>14. What goes in the try clause? What goes in the except clause?</b>
In the try clause goes whatever code you want to try run.
In the except clause goes whatever code you want to execute if an error is caught.
</pre>

# Chapter 4 Questions

<pre>
<b>1. What is []?</b>
</pre>
<pre>
<b>2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam?</b>
(Assume spam contains [2, 4, 6, 8, 10].)
For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
</pre>
<pre>
<b>3. What does spam[int(int('3' * 2) // 11)] evaluate to?</b>
</pre>
<pre>
<b>4. What does spam[-1] evaluate to?</b>
</pre>
<pre>
<b>5. What does spam[:2] evaluate to?</b>
For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
</pre>
<pre>
<b>6. What does bacon.index('cat') evaluate to?</b>
</pre>
<pre>
<b>7. What does bacon.append(99) make the list value in bacon look like?</b>
</pre>
<pre>
<b>8. What does bacon.remove('cat') make the list value in bacon look like?</b>
</pre>
<pre>
<b>9. What are the operators for list concatenation and list replication?</b>
</pre>
<pre>
<b>10. What is the difference between the append() and insert() list methods?</b>
</pre>
<pre>
<b>11. What are two ways to remove values from a list?</b>
</pre>
<pre>
<b>12. Name a few ways that list values are similar to string values.</b>
</pre>
<pre>
<b>13. What is the difference between lists and tuples?</b>
</pre>
<pre>
<b>14. How do you type the tuple value that has just the integer value 42 in it?</b>
</pre>
<pre>
<b>15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?</b>
</pre>
<pre>
<b>16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?</b>
</pre>
<pre>
<b>17. What is the difference between copy.copy() and copy.deepcopy()?</b>
</pre>

# Chapter 5 Questions

<pre>
<b>1. What does the code for an empty dictionary look like?</b>
</pre>
<pre>
<b>2. What does a dictionary value with a key 'foo' and a value 42 look
like?</b>
</pre>
<pre>
<b>3. What is the main difference between a dictionary and a list?</b>
</pre>
<pre>
<b>4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?</b>
</pre>
<pre>
<b>5. If a dictionary is stored in spam, what is the difference between the
expressions 'cat' in spam and 'cat' in spam.keys()?</b>
</pre>
<pre>
<b>6. If a dictionary is stored in spam, what is the difference between the
expressions 'cat' in spam and 'cat' in spam.values()?</b>
</pre>
<pre>
<b>7. What is a shortcut for the following code?</b>
if 'color' not in spam:
spam['color'] = 'black'
</pre>
<pre>
<b>8. What module and function can be used to “pretty print” dictionary
values?</b>
</pre>

# Chapter 6 Questions

<pre>
<b>1. What are escape characters?</b>
</pre>
<pre>
<b>2. What do the \n and \t escape characters represent?</b>
</pre>
<pre>
<b>3. How can you put a \ backslash character in a string?</b>
</pre>
<pre>
<b>4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote
character in the word Howl's isn’t escaped?</b>
</pre>
<pre>
<b>5. If you don’t want to put \n in your string, how can you write a string with newlines in it?</b>
</pre>
<pre>
<b>6. What do the following expressions evaluate to?</b>
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
</pre>
<pre>
<b>7. What do the following expressions evaluate to?</b>
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
</pre>
<pre>
<b>8. What do the following expressions evaluate to?</b>
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
</pre>
<pre>
<b>9. What string methods can you use to right-justify, left-justify, and center a string?</b>
</pre>
<pre>
<b>10. How can you trim whitespace characters from the beginning or end of a string?</b>
</pre>
