numbers=[-10,15,-3,7,-25,18,0]
positive_numbers=[num for num in numbers if num>0]
print(f"positive numbers in {numbers}:",positive_numbers)
N=5
square=[num **2 for num in range(1,N+1)]
print("Squares of first 5 numbers : ",square)
word="comperehension"
vowels=[char for char in word if char in 'aeiou']
print(f"vowels in the words : {word}",vowels)
word="hello"
ordinal_value=[ord(char)for char in word]
print("Ordinal value of each character in the word: hello",ordinal_value)
