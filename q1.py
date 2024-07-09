'''
If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 

(one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.)
'''

def number_to_words(n):
    """ Convert a number n (1 <= n <= 1000) to words """
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)
    elif n == 1000:
        return "onethousand"
    else:
        return ""  # For numbers outside the specified range (1-1000)

def count_letters_in_words(n):
    #Count the number of letters in the words representation of number n
    words = number_to_words(n)
    return len(words)

def total_letters_used_in_numbers_up_to(limit):
    #Calculate the total number of letters used in numbers from 1 to limit
    total_letters = 0
    for i in range(1, limit + 1):
        total_letters += count_letters_in_words(i)
    return total_letters

# Calculate the total letters used for numbers from 1 to 1000
total_letters = total_letters_used_in_numbers_up_to(1000)
print("Total letters used:", total_letters)
