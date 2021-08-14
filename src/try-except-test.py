s = input("Input string: ")
try:
    while s:
        print(s[:s.index(" ")])
        s = s[s.index(" ")+1:]
except ValueError:
    print(s) if s else None
    print("No spaces")
finally:
    print("End of program")

