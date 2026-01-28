word = input("Enter a word: ")

length = len(word)
numbers = []

for i in range(1, length + 1):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print(numbers)
print("The length of the word is", length)
print("The average of the numbers is", average)

if length < average:
    print(f"The length of the word '{word}' is less than the average.")
elif length > average:
    print(f"The length of the word '{word}' is greater than the average.")
else:
    print(f"The length of the word '{word}' is equal to the average.")
