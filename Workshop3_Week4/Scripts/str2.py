# file: str2.py
# How many characters in a string come before
# the first period.

s = "blah.blah.blah"
n = 0
for c in s:
   if c == '.':
      break
   else:
      n += 1
print(n)
