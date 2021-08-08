s = input("Input string: ")
try:
    while s:
        print(s[:s.index(" ")])
        s = s[s.index(" ")+1:]
except ValueError:
    if s:
        print(s)
    print("No spaces")
finally:
    print("End of program")

