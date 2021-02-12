# This is a sample Python script.



#print('savan')

#price = 10
#price = 20
#print(price)

#name = input('what is your name? ')
#print(' Hi ' + name)

#course = 'python for biginners'
#print(course[0])
#print(course[-1])
#print(course[0:3])

#print(course.upper())

#x = 10 ** 3
#print(x)

#x = 10 + 2 * 5
#print(x)
"""
is_hot = False
is_cold = True

if is_hot:
   print("It's a hot day")
elif is_cold:
   print("It's cold day")
else:
    print("It's lovely day")
"""
"""
i = 6

while i>0:
    print('*' * i)
    i -= 1
print("Done")
"""
"""
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("car is aiready started")
        else:
            started = True
            print('car is start......')
    elif command == "stop":
        if not started:
            print('car is already stopped')
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print( """
#start - to start car
#stop - to stop car
#quit - to quit
 #       """ )
  #  elif command == "quit":
   #     break
    #else:
     #   print("Sorry, I don't understand ")
"""
"""
#for x in range(0,10):
 #   print(x)
"""
for x in range (4):
    for y in range (3):
        print(f"({x},{y})")


"""

#number = [5,2,5,2,5]
#for x in number:
 #   print('x' * x)
"""
list = [45,65,78,2,46,99,34,54,23,1000]
max = list[0]
for x in list:
    if x > max:
        max = x
print(max)
"""
"""
number = [3,6,9,43,5]
number.append(23)
print(number)
number.insert(3,56)
print(number)
number.remove(6)
print(number)
number.pop()
print(number)
"""
"""
#list
numbers = [4,5,6,2,3,2,5,6,7,9,8,7,9,1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

"""
"""
#tuples
numbers = (1,2,3)
numbers[0] = 10
print(numbers[0])
"""
"""
#unpacking
coordinates = (1,2,3)
x,y,z = coordinates
print(x)
print(y)
print(z) 
"""

"""
#dictionary
customer = {
    "name" : "ABC XYZ",
    "age" : 39,
    "mno" : "1234567890"
}
print(customer["name"])



phone = input("Phone: ")
digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for x in phone:
    output += digit_mapping.get( x , "!" ) + ""
print(output)

"""
#emoji converter using dictionary



