# Comments start with a Pound sign better known as hash

#numbers are immutable i was wrong earlier
a = 1
print("a is ", a)
b = a
print("b is ", b)
a = 2
print("a is ", a, " and b is ", b)

a = list([1, 2, 3, 4])
b = a

# lists are mutable
print("a is ", str(a), " and b is ", str(b))
a.remove(2)
print("a is ", str(a), " and b is ", str(b))

# but if instead i do
b = a[1:4]

print("a is ", str(a), " and b is ", str(b))

colors = dict()

def checkColors(colordict):
  if not colordict:
    print("Sorry there are no colors yet")
  elif len(colordict) == 1:
    print("You can have any color like as long as its",
          str(iter(colordict).begin()))
  else:
    #how big is it?
    print("There are", str(len(colordict)), "colors")

checkColors(colors)

colors['black'] = 0x000000  #hexcode for black

checkColors(colors)

def InsertColor(container, name, color):
  container[name]=color

InsertColor( colors, red,    0x990000)
InsertColor( colors, blue,   0x000099)
InsertColor( colors, yellow, 0x009900)

checkColors(colors)

#what colors are there?
print(str(colors.keys()))

print ("the dict is ", str(colors))
#lets iterate over every item in the dictionary
for color, code in colors.items():
    print("The color:", color, "has code:", code)

#does our dictionary have color black?
if 'black' in colors:
  print ("We have black in stock")

if 'pink' in colors:
  print ("What kinda shop do you think this is?")

# a true pythonic monty pythonism
print("What is your name?")
name = input()
print(name + ", what is your quest?")
x = input()
print("A noble quest indeed %s" % (name,))
print("{}, what is your favorite color".format(name))
choice = input()
result = colors.get(choice, None)
if result is not None:
  print ("{} the color code for that is {}".format(name, result))
else:
  print ("{}, {}".format(name, "Sorry thats not your favorite color"))