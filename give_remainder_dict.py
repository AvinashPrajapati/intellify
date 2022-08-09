from collections import Counter
from decimal import *   

# using counter module for counting the occurence
# using decimal module for very large decimal places

def give_remainder_dict(dividend, diviser, Number_of_digits):
    no_of_digits = Number_of_digits+2 #adding 2 means taking . and avoiding roundup in account 
    dot100 = setcontext(Context(prec=no_of_digits)) #setting precise digits
    a = Decimal(float(dividend)) / Decimal(float(diviser))  # Decimal class return the division result.

    res_string = str(a).split('.')[1][:-1] 
    # as limit is string like 3.8989899 something then we can split it using split('.')
    # getting list of strings as limit  ['3', '8989899']

    # as no_f_digits is Increased by one hence we used [:-1] to get the string of dicimal #places up to Number_of_digits

    # print(res_string) -> to check we got correct string of decimal places
    counter = Counter(res_string)  # here counter class evaluate the counter of all element.
    res = dict(counter)
    print(res) # we converted it into dict to get desired output

give_remainder_dict(dividend=22, diviser=7, Number_of_digits=10)  #calling the function
