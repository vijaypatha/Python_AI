'''
Source: https://realpython.com/python-for-loop/

EXPECT OUTCOME: ability to access anything from any where. 

WHAT IS ITERATION: repeted exectuion of same block of code is called iteration. There are two types of repetitive execution 
1) Definite iteration: # of repetition is explicitly specified in adavance. This is accomplished by for loops
2) Indefinite iternation: # of repetition is not known, hence we provide a condition to be met. This types of iterations are done using while loops

SINCE THIS file is for FOR LOOPS, we will cover While loops later. 

for <var> in <iterable>:
    <statements>

for idx in range(0, len(in_files), 1): # idx is the loop variable that takes on the next element range(x,x,x), a iterable, each time a loop is ran. 

WHAT IS ITERABLE AND ITERATORS: an object that can be used in iteration. Key point is there are objects that are iterable - lists, sets, dictionaries, strings. These objects where you iterate are called iterators. Some objects are not iternable like integer and floats. 

BENEFIT OF ITERATORS: Iterators saves space. It waits to give you the iterable until you ask for it (next()). 
'''

# Lesson 1
d = {'foo':1, 'bar':2, 'baz':3}
for i in d:
    print(i)
# i, the for loop variable, is only assigned to keys

for k in d.values():
    print(k)
#k, the loop variable, can access values by using builtin function .values()

#loop variable of a for loop isn’t limited to just a single variable.
for i, k in d.items():
    print(i, k)

# Lesson 2
# RANGE is used when start and ending values of iterable are not known. 
x = range(5)
print(x) #range(0, 5)
print(type(x)) #<class 'range'>
print(list(x)) #[0, 1, 2, 3, 4]

