#playing around
# testvariable = 8
# lr = list(range(testvariable))
# print(lr[-1])


# coll=[11,222,3333]
# i=0

# while(i < len(coll)):
#     print(i)
#     i = i+1




# #Create a function that returns the string
# #"Burp" with the amount of "r's" determined
# #by the input parameters of the function.
# # range(num[-1])
# def long_burp(num):
#     burp = "Bu" + (num * "r") + "p"
#     return burp


# print(long_burp(3))  #> "Burrrp"
# print(long_burp(5))  #> "Burrrrrp"
# print(long_burp(9))  #> "Burrrrrrrrrp"





# #Create a function(increment) that takes a
# #number as an argument, increments the number
# #by +1 and returns the result.
# def increment(num):
#     newnum = num + 1
#     return newnum


# print(increment(0))   #> 1
# print(increment(9))   #> 10
# print(increment(-3))  #> -2








# __________________________________________________________________

# In this challenge, a farmer is asking you to
#tell him how many legs can be counted among all
#his animals. The farmer breeds three species, chickens have
#two legs, cows have four legs, and pigs have four legs. The
#farmer has counted his animals and he gives you a subtotal for each species.
#You have to implement a function that returns the total
#number of legs of all the animals.

#your code here

print(how_many_legs(2, 3, 5))    #> 36
print(how_many_legs(1, 2, 3))    #> 22
print(how_many_legs(5, 2, 8))    #> 50

# __________________________________________________________________











# __________________________________________________________________


# Create a function that takes two numbers as arguments and return their sum.

#your code here

print(addition(2, 3))   #> 5
print(addition(-3, -6)) #> -9
print(addition(7, 3))   #> 10



# __________________________________________________________________




# __________________________________________________________________
# Given two strings, first_name and last_name, return a single
# string in the format "last, first".

#your code here

print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"
# __________________________________________________________________







# __________________________________________________________________
#Create a function that takes a string (a random name).
#If the last character of the name is an "n", return True, otherwise return False.

#your code here

print(is_last_character_n("Aiden"))  #> True
print(is_last_character_n("Piet"))   #> False
print(is_last_character_n("Bert"))   #> False
print(is_last_character_n("Dean"))   #> True
# __________________________________________________________________





# __________________________________________________________________
#Create a function that takes a list of
#elements and return the first and last elements as a new list.

#your code here

print(first_last([5, 10, 15, 20, 25]))            #> [5, 25]
print(first_last([13, None, False, True]))        #> [13, True]
print(first_last([None, 4, "6", "hello", None]))  #> [None, None]
# __________________________________________________________________
