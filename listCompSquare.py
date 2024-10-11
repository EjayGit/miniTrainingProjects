for i in range(1,11):
    print(i*i)

# List comprehension
newLi = [i*i for i in range(1,11)]
print(newLi)

# Conditional list comprehension
prevList = [-1, 10, -20, 2, -90, 60, 45, 20]
# newList = [newItem for item in list if condition]
newList = [number*number for number in prevList if number < 0]
print(newList)

sentence = 'My name is Erik'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('t'))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)