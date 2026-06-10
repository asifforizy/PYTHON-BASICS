
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b = "Hello, World!"
print(b[1])

# Looping Through a String
for x in "banana":
  print(x)
  
# String Length

d = "Hello, World!"
print(len(d))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Slicing
c = "Hello, World!"
print(c[2:5])
e = "Hello, World!"
print(e[:5])


b = "Hello, World!"
print(b[-5:-2])


# upper case
a = "Hello, World!"
print(a.upper())


# lower case
a = "Hello, World!"
print(a.upper())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# The replace() method replaces a string with another string:
a = "I am a astudent!"
print(a.replace("I", "J"))



# the split() method splits the string into substrings if it finds instances of the separator:
f = "Hello, World!"
print(f.split(",")) # returns ['Hello', ' World!']

