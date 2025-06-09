def make_negative(number):
    return -abs(number)  # Ensures the number is always negative

# Get a number from user input
Number = int(input("Enter a number to make negative: "))
print(make_negative(Number))  # This was missing in your code

print("ddd\n")  # Random print — optional

def smash(words):
    return ''.join(words)  # Joins list of words or characters into a single string

# If you're entering a sentence or space-separated words:
words = input("Enter a sentence: ").split()  # Converts input string to list of words

print(smash(words))



