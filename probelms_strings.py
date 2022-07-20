name = input("what is you name: ")
greetings = "good afternoon "
string = (greetings + name)
print(string)


name = input("enter you name: ")
date = input("enter date: ")
letter = '''hello <NAME>
you are selected
date: <DATE>'''
letter = letter.replace("<NAME>", name)
letter = letter.replace("<DATE>", date)
print(letter)


st = "hello  everyone"
doublespaces = st.find("  ")
print(doublespaces)
st = st.replace("  ", " ")
print(st)

letter = "hey sahil,\nthis python course is nice.\nthankyou"
print(letter)

