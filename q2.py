"""

# -----------------------
# File      : q2.py
# Created   : 30/09/21 2:35 PM
# Author    : Ron Greego
# Version   : v1.0.0
# Description : Program to count the number of even and odd numbers from a series of numbers
# --------------------------
"""

if __name__ == '__main__':

    number_series = (10, 11, 20, 22, 35, 76, 33)  # tuple to store a series of numbers
    print(number_series)
    even_number, odd_number = 0, 0
    for i in number_series:
        if i % 2 == 0:
            even_number += 1
        else:
            odd_number += 1

    print("Total count of even numbers : {}".format(even_number))
    print("Total count of odd numbers : {}".format(odd_number))
