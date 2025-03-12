string = input("Enter a string: ")
result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]
print("String after removing characters at odd index positions:", result)
