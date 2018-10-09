
# coding: utf-8

# # Hello World

# In[1]:


print("Hello world!")


# # Variables and Types
# 
# **Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.**

# In[2]:


myint = 7
print(myint)


# In[3]:


myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


# In[4]:


mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)


# In[5]:


one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


# **Python uses C-style string formatting to create new, formatted strings.<br>
# %s - String (or any object with a string representation, like numbers)<br>
# %d - Integers<br>
# %f - Floating point numbers**

# In[6]:


# This prints out "Nik is 21 years old."
name = "Nik"
age = 21
print("%s is %d years old." % (name, age))
print("{} is {} years old.".format(name, age))


# # Getting user input

# In[7]:


a = input("insert a number")
print(a)


# # Lists
# 
# **Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.**

# In[8]:


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)


# In[9]:


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


# **what if we want to add the elements of this two list with each other?**

# In[10]:


[x + y for x, y in zip(even_numbers, odd_numbers)]


# # tuple
# **A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses**

# In[11]:


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";


# # Dictionaries
# **A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.**

# In[12]:


phonebook = {}
phonebook["Nik"] = 938477566
phonebook["Hamed"] = 938377264
phonebook["Erfan"] = 947662781
print(phonebook)


# In[13]:


phonebook = {
    "Nik" : 938477566,
    "Hamed" : 938377264,
    "Erfan" : 947662781
}


# In[14]:


for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# In[16]:


phonebook = {
   "Nik" : 938477566,
   "Hamed" : 938377264,
   "Erfan" : 947662781
}
del phonebook["Nik"]
# print(phonebook)
print(phonebook["Erfan"])
print(phonebook)


# # Condition
# ## Indentation and if statement
# **Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported**

# In[17]:


x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
else:
    print("x is not 1.")


# In[18]:


name = "Nik"
age = 21
if name == "Nik" and age == 21:
    print("Your name is Nik, and you are also 21 years old.")
if name == "Nik" or name == "Erfan":
    print("Your name is either Nik or Erfan.")


# In[19]:


name = "Nik"
if name in ["Nik", "Hamed"]:
    print("Your name is either Nik or Hamed.")


# ## Not
# **Using "not" before a boolean expression inverts it:**

# In[20]:


print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# # Loops
# ## The "for" loop
# ** For loops iterate over a given sequence. Here is an example:**

# In[21]:


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


# In[22]:


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime, end=' ')


# **For loops can iterate over a sequence of numbers using the "range"**

# In[23]:


# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x,end=' ')
print("\n")

# Prints out 3,4,5
for x in range(3, 6):
    print(x,end=' ')
print("\n")

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x,end=' ')


# ## For loop with Enumerate
# **It's helpful if you want to loop over an interator, and also want to have an index counter available**

# In[24]:


for item in enumerate(["a", "b", "c"]):
    print(item)


# **Start index from some other value**

# In[25]:


for item in enumerate(["a", "b", "c"],2):
    print(item)


# ## "While" loop
# **While loops repeat as long as a certain boolean condition is met. For example:**

# In[26]:


# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# ## "break" and "continue" statements
# **break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples**

# In[27]:


# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


# # Functions
# ## How do you write functions in Python?

# In[28]:


# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, Nik, From My Function!, I wish you a great year!"
my_function_with_args("Nik", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)


# # Classes and Objects
# **Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes**

# In[29]:


class MyClass:
    variable = "blah"

    def function(self):
        return("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
print(myobjectx.function())


# ## init,private and public
# **The init method gets called when memory for the object is allocated:**<br>
# **with ._ and .__ we can change the public variable and func. to protected and private variable and func.**<br>
# **private - only available to be accessed within the class that defines them.**<br>
# **protected - accessible in the class that defines them and in other classes which inherit from that class.**<br>

# In[30]:


class Car:
    maxspeed = 0
    name = ""

    def __init__(self,a,b):
        self.maxspeed = a
        self.name = b

    def drive(self):
        print('driving. maxspeed ' + str(self.maxspeed))


redcar = Car(120,"pride")
print("maxspeed is=>",redcar.maxspeed)
redcar.drive()

redcar.maxspeed = 10  # will not change variable because its private
redcar.drive()


# ## setter and getter

# In[31]:


class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ',(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()


# # Modules and Packages

# In[32]:


import numpy as np


# In[33]:


numpy.nan


# In[34]:


np.nan

