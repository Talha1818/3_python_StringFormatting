
# =======================
# 3_StringFormatting.py:
# =======================

# Displaying string and numbers at the same time
# Note that you cannot use "string" + 5 because python will try to add a string to a number and crash
# To be able to concantenate a string and number using +, you need to use str(number) to convert number to string
# Here you convert age (number) to a string and then concatenate it with the other string

age = 24
print("My age is " + str(age) + " years")
print()
# If you are dealing with lots of data, str becomes tedious
# To make it easier, we use "replacement fields"

# Replacement fields
# Here we take age and put it in field position {0)

print("My age is {0} years".format(age))
print()

# Here age1 is put in field {0} and age2 in field {1}
age1 = 10
age2 = 20
print("Age1 is {0} and Age2 is {1}".format( (age1), (age2) ))
print()

# Example of using replacement fields to get the months that have 31 days
# Here we are replacing field {0} with 31 and other fields {1} to {7} with the Month numbers

print("There are {0} days in {1}, {2}. {3}, {4}, {5}, {6}, {7} ".format(31, "January",
            "March", "May", "July", "August", "October", "December"))
print()

# We can also print the month names and then show their days next to them
# In this case we will use triple quotes " " " so we can type in multiple lines.
# And then we have numbers 28, 30,31 being populated in their respective positions next to the months
# NOTE that we are using position 2 and 1 several times. This is possible in replacement fields but not in string formatting.

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
print()

# String formatting operator %d
# # NOTE this String formatting operator is being deprecated in python3 but is in python2
# Here d is being replaced with an integer from variable age

age = 24
print("My age is %d years" % age)
print()

# Then we can do multiple replacement
# %d is to replace integer or number
# %s is to replace string.

print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
print()

# String formatting to allocate space
# We use %2d to allocate two spaces, %4d to allocate 4 spaces for the numbers

for i in range(1, 12):
    print("No# %2d squared is %3d and Cubed is %4d" %(i, i ** 2, i ** 3))
print()

# Using string format to specify the precision of a number
# The %6f specifies reserving 6 characters for float
# The results show 3.142857 (8 characters with default 6 decimal places

print("Pi is approx equal to: %6f" % (22/7))
print("Pi is approx equal to: %8f" % (22/7))
print("Pi is approx equal to: %10f" % (22/7))
print("Pi is approx equal to: %12f" % (22/7))
print("Pi is approx equal to: %14f" % (22/7))
print()

# We can request more digits after the decimal place.
# Say in this case we want 20 decimals
print("Pi is approx equal to: %12.20f" %(22/7))
print()
# link to string formatting operators
# https://docs.python.org/2.4/lib/typesseq-strings.html

# Using replacement fields instead of using string formatting
# {0:2} means start at position 0 and allocate 2 digits. {0} if first in .format(), {1} is second in .format()
# {1:4} means start at position 1 and allocate 4 digits. etc
# Then use the .format (for replacement fields) instead of % (for string formatting)
# Note that the results are right formatted.

for i in range(1, 12):
    print("No# {0:2} squared is {1:4} and Cubed is {2:4}".format(i, i ** 2, i ** 3))
print()

# you can use the < sign to left format as follows
for i in range(1, 12):
    print("No# {0:2} squared is {1:<4} and Cubed is {2:<4}".format(i, i ** 2, i ** 3))
print()

# Using replacement fields on the Pi code
print("Pi is approx equal to: {0}".format(22/7))
print()

# NOTE that replacement field is the new format on python 3 and string formatting is the old on python 2
# NOTE in string formatting, you can use a position once.
# In replacement fields, you can use a position as many times as you want

# NOTE that using numbers in replacement fields is optional.
# If you don't use them, python assumes you are starting from position 0 and incrementing upwards

for i in range(1, 12):
    print("No# {:2} squared is {:4} and Cubed is {:4}".format(i, i ** 2, i ** 3))
print()

# If you don't specify the numbers, then you can use the positions only once.
# If you want to use the positions more than once, you have to specify numbers in replacement fields.

for i in range(1, 12):
    print("No# {} squared is {} and Cubed is {}".format(i, i ** 2, i ** 3))
print()