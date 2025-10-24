def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)

text = input("Enter a string: ")
count_case(text)
