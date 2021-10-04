"""

# -----------------------
# File      : q3.py
# Created   : 30/09/21 2:35 PM
# Author    : Ron Greego
# Version   : v1.0.0
# Description : Write a Python program that accepts a string and calculate the number of digits,
                upper case letters and lower case letters
# --------------------------
"""

if __name__ == '__main__':

    upper_count, lower_count, digit_count = 0, 0, 0
    input_string = input("Enter a string: ")
    for i in input_string:
        if i.isnumeric():
            digit_count += 1
        elif 'a' <= i <= 'z':
            # counting lower case (we can either use islower() inbuilt function)
            lower_count += 1
        elif 'A' <= i <= 'Z':
            # counting upper case (we can either use isupper() inbuilt function)
            upper_count += 1

    print('Digit count : {} \nLower case count : {} \nUpper case count : {}'.format(digit_count, lower_count, upper_count))