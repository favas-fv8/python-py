string = input("Enter a string: ")
mid = len(string) // 2
first_half = string[:mid][::-1]
second_half = string[mid:][::-1]
result = first_half + second_half
print("String after reversing first and second half separately:", result)
