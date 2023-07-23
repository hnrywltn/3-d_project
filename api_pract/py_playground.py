# Write a function dynamic_duos that accepts a string as an argument
# and returns the count of the number of times the same character
# appears consecutively in the given string.

def dynamic_duos(string):
    count = 0
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i + 1]
        if letter1 == letter2:
            count+= 1
    return count


    # your code here


print(dynamic_duos('bootcamp'))     # 1
print(dynamic_duos('wxxyzz'))       # 2
print(dynamic_duos('hoooraay'))     # 3
print(dynamic_duos('dinosaurs'))    # 0
print(dynamic_duos('e'))            # 0

print('_____________________________________________________')







# Write a function potent_product that accepts a list of numbers and
# a product as arguments. The function should return a boolean indicating
# whether or not a pair of distinct elements in the list result in the
# product when multiplied together. You may assume that the input list
# contains unique elements.

def potent_product(numbers, product):
    # your code here
    for u in range(len(numbers)):
        x = numbers[u]
        for a in range(len(numbers)):
            y = numbers[a]
            if x * y == product and u != a:
                return True
    return False


print(potent_product([4, 2, 5, 8], 16))    # True
print(potent_product([8, 9, 1, 3], 8))     # True
print(potent_product([3, 4], 12))          # True
print(potent_product([3, 4, 6, 2, 5], 12)) # True
print(potent_product([4, 2, 5, 7], 16))    # False
print(potent_product([8, 4, 9, 3], 8))     # False
print(potent_product([3], 12))             # False

print('_____________________________________________________')






# Write a function savvy_sums that accepts a list of numbers as an
# argument. The function should return a count of the number of
# distinct pairs of elements that have a sum of zero. You may
# assume that the input list contains unique elements.

def savvy_sums(numbers):
    # your code here
    count = 0
    for i in range(len(numbers)):
        a = numbers[i]
        for j in range(len(numbers)):
            b = numbers[j]
            if a + b == 0 and j > i:
                count += 1
    return count


# count = 0 - 1 - 2 - 3 - 4
#                               i
#                 j
print(savvy_sums([2, -3, 3, 4, -2]))     # 2

print(savvy_sums([42, 3, -1, -42]))      # 1
print(savvy_sums([-5, 5]))               # 1
print(savvy_sums([19, 6, -3, -20]))      # 0
print(savvy_sums([9]))                   # 0


print('_____________________________________________________')



# Write a function rational_repeats that accepts a string and a
# dictionary as arguments. The function should return a new string
# where characters of the original string are repeated the number
# of times specified by the dictionary. If a character does not
# exist as key of the dictionary, then it should remain unchanged.

def rational_repeats(string, d):
    # your code here
    word = ''
    for i in range(len(string)):
        if string[i] in d:
            word += string[i] * d[string[i]]
        else:
            word += string[i]
    return word
    # ( :

print(rational_repeats('taco', {'a':3, 'c':2}))
# 'taaacco'
print(rational_repeats('feverish', {'e':2, 'f':4, 's':3}))
# 'ffffeeveerisssh'
print(rational_repeats('misispi', {'s':2, 'p':2}))
# 'mississppi'
print(rational_repeats('faarm', {'e':3, 'a':2}))
# 'faaaarm'



print('_____________________________________________________')





# Write a function cryptic_conversion that accepts a sentence as an argument.
# The function should translate the sentence according to the following rules:

# words that are shorter than 3 characters are unchanged

# words that are 3 characters or longer are translated according to the following rules:
    # if the word begins with a vowel, simply add 'yay' to the end of the word (example: 'eat'->'eatyay')
    # if the word begins with a non-vowel, move all letters that come before the word's first vowel to the end of the word and add 'ay' (example: 'trash'->'ashtray')
# Note that if words are capitalized in the original sentence, they should remain capitalized in the translated sentence. Vowels are the letters a, e, i, o, u.


def cryptic_conversion(sentence):
    words = sentence.split(' ')
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word)
        else:
            new_words.append(convert_word(word))
    return ' '.join(new_words)


def convert_word(word):
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        return word + 'yay'
    for i in range(len(word)):
        letter = word[i]
        if letter in vowels:
            return word[i:] + word[:i] + 'ay'
#   2
# france

# def cryptic_conversion(sentence):
#     # your code here
#     sentence = sentence.split()
#     wreturn = ''
#     sreturn = ''
#     nvset = ''
#     vset = ''
#     for i in sentence:
#         wreturn = i
#         if len(i) >= 3:
#             if i.lower().startswith('a') or i.lower().startswith('e') or i.lower().startswith('i') or i.lower().startswith('o') or i.lower().startswith('u'):
#                 wreturn += 'yay'
#             else:
#                 continuecons = True
#                 conscount = -1
#                 vset = ''
#                 nvset = ''
#                 for u in i:
#                     if u.lower() == 'a' or u.lower() == 'e' or u.lower() == 'i' or u.lower() == 'o' or u.lower() == 'u':
#                         continuecons = False
#                     else:
#                         if continuecons == True:
#                             nvset += u
#                     if continuecons == False:
#                         vset += u
#                 wreturn = vset + nvset + 'ay'
#         sreturn = sreturn + ' ' + wreturn
#     return sreturn







print(cryptic_conversion('We like to eat bananas')) # "We ikelay to eatyay ananasbay"
print(cryptic_conversion('I cannot find the trash')) # "I annotcay indfay ethay ashtray"
print(cryptic_conversion('What an interesting problem')) # "Atwhay an interestingyay oblempray"
print(cryptic_conversion('Her family flew to France')) # "Erhay amilyfay ewflay to Ancefray"
print(cryptic_conversion('Our family flew to France')) # "Ouryay amilyfay ewflay to Ancefray"



























# #playing around
# # testvariable = 8
# # lr = list(range(testvariable))
# # print(lr[-1])


# # coll=[11,222,3333]
# # i=0

# # while(i < len(coll)):
# #     print(i)
# #     i = i+1




# # #Create a function that returns the string
# # #"Burp" with the amount of "r's" determined
# # #by the input parameters of the function.
# # # range(num[-1])
# # def long_burp(num):
# #     burp = "Bu" + (num * "r") + "p"
# #     return burp


# # print(long_burp(3))  #> "Burrrp"
# # print(long_burp(5))  #> "Burrrrrp"
# # print(long_burp(9))  #> "Burrrrrrrrrp"





# # #Create a function(increment) that takes a
# # #number as an argument, increments the number
# # #by +1 and returns the result.
# # def increment(num):
# #     newnum = num + 1
# #     return newnum


# # print(increment(0))   #> 1
# # print(increment(9))   #> 10
# # print(increment(-3))  #> -2








# # __________________________________________________________________

# # In this challenge, a farmer is asking you to
# #tell him how many legs can be counted among all
# #his animals. The farmer breeds three species, chickens have
# #two legs, cows have four legs, and pigs have four legs. The
# #farmer has counted his animals and he gives you a subtotal for each species.
# #You have to implement a function that returns the total
# #number of legs of all the animals.

# #your code here
# def how_many_legs(num1, num2, num3):
#     sum = (num1 * 2) + (num2 * 4) + (num3 * 4)
#     return sum
# print(how_many_legs(2, 3, 5))    #> 36
# print(how_many_legs(1, 2, 3))    #> 22
# print(how_many_legs(5, 2, 8))    #> 50

# # __________________________________________________________________





# print("-")





# # __________________________________________________________________


# # Create a function that takes two numbers as arguments and return their sum.

# #your code here
# def addition(nu1, nu2):
#     sumq2 = nu1 + nu2
#     return sumq2
# print(addition(2, 3))   #> 5
# print(addition(-3, -6)) #> -9
# print(addition(7, 3))   #> 10



# # __________________________________________________________________


# print("-")

# # __________________________________________________________________
# # Given two strings, first_name and last_name, return a single
# # string in the format "last, first".

# #your code here
# def concat_name(fst, lst):
#     endname = lst + ", " + fst
#     return endname
# print(concat_name("First", "Last"))  #> "Last, First"
# print(concat_name("John", "Doe"))    #> "Doe, John"
# print(concat_name("Mary", "Jane"))   #> "Jane, Mary"
# # __________________________________________________________________



# print("-")



# # __________________________________________________________________
# #Create a function that takes a string (a random name).
# #If the last character of the name is an "n", return True, otherwise return False.

# #your code here
# # def is_last_character_n(nam):
# #    if nam.endswith()
# #     return isn
# # print(is_last_character_n("Aiden"))  #> True
# # print(is_last_character_n("Piet"))   #> False
# # print(is_last_character_n("Bert"))   #> False
# # print(is_last_character_n("Dean"))   #> True
# # __________________________________________________________________


# print('-')


# # __________________________________________________________________
# #Create a function that takes a list of
# #elements and return the first and last elements as a new list.

# #your code here
# def first_last(fl):
#     sorted = [(fl[0]), (fl[-1])]
#     return sorted

# print(first_last([5, 10, 15, 20, 25]))            #> [5, 25]
# print(first_last([13, None, False, True]))        #> [13, True]
# print(first_last([None, 4, "6", "hello", None]))  #> [None, None]

# # surprisingly, this part was easier than the last prompt, leading to a weird error?? idk i cant find out how to fix it
# # __________________________________________________________________
