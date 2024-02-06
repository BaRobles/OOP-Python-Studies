class Programmer:

  # Add the class attributes
  salary = 100000
  monthly_bonus = 400

  def __init__(self, name, age, address, phone, programming_languages):
    self.name = name
    self.age = age
    self.address = address
    self.phone = phone
    self.programming_languages = programming_languages


class Assistant:

  # Add the class attributes
  salary = 100200
  monthly_bonus = 200

  def __init__(self, name, age, address, phone, is_bilingual):
    self.name = name
    self.age = age
    self.address = address
    self.phone = phone
    self.is_bilingual = is_bilingual


# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month.
def calculate_payroll(employees):

  total = 0

  print("\n========= Welcome to our Payroll System =========\n")

  # Iterate over the list of instances to calculate
  # and display the monthly salary of each employee,
  # and add the monthly salary to the total for this month.
  for employee in employees:
    salary = round(employee.salary / 12, 2) + employee.monthly_bonus
    print(employee.name.capitalize() + "'s salary is: $" + str(salary))
    total += salary

  # Display the total
  print("\nThe total payroll this month will be: $", total)


# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)

# List of instances
employees = [jack, isabel, nora]

# Function call (Passing the list of instances as argument)
calculate_payroll(employees)


#NON-PUBLIC ATTRIBUTES
class Student:
  def __init__(self, student_id, name, age, gpa):
    self.student_id = student_id
    self.name = name
    self._age = age
    self.gpa = gpa

print("-----------------")
student_nora = Student("245AFS", "NoraNav", 21, 3.8)
print(student_nora.student_id)
print(student_nora.name)
#PyCharm would give an allert here, because we are accessing a non-public attribute.
# print(student_nora.age) would return an Error
print(student_nora._age)
print(student_nora.gpa)
# but if we use double underscore, the Error will be thrown, 
# even if we call the attribute with the leading double score!

#NAME MANGLING
print("==================")
class Backpack:
  def __init__(self):
    self.__items = []

my_backpack = Backpack()
#to access __items, we have to add _Classname:
print(my_backpack._Backpack__items)

class Book:
  def __init__(self, title, year, theme):
    self.__title = title
    self.__year = year
    self.__theme = theme

my_movie = Book("The Matrix", 1999, "Science Fiction")
print(my_movie._Book__title)


def set_name(self, name):
  if isinstance(name, str):
    self._name = name # update the value
  else:
    print("Please enter a valid name")

class Patient:
  def __init__(self, name, age, id_num, num_children=0):
    self.name = name
    self.age = age
    self._id_num = id_num
    self._num_children = num_children

  def get_id_num(self):
    print("Getter")
    return self._id_num

  def set_id_num(self, new_id):
    print("Setter")
    if isinstance(new_id, str):
      self._id_num = new_id
    else:
      print("Please enter a valid id")

  id_num = property(get_id_num, set_id_num)

patient = Patient("Gino", 15, "4535")

patient.id_num # calls getter

patient.id_num = "545435" 

class House: 
  def __init__(self, price):
    self._price = price

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, new_price):
    if price > 0:
      self._price = _price
    else:
      print("Please enter a valid price")

#GETTERS & SETTERS
class Movie:
  def __init__(self, title, rating):
    self._title = title # non-public
    self.rating = rating

  #get title
  def get_title(self): #self is mandatory
    return self._title

my_movie = Movie("The Godfather", 4.8)

print("==================")
print("My favorite movie is:", my_movie.get_title())

class Dog:
  def __init__(self, name, age):
    self._name = name
    self.age = age

  def get_name(self):
    return self._name

  # new_name is here because we need to tell which variable will take the new value
  def set_name(self, new_name):
    # checking if the new instance is a string, and alphabetical:
    if isinstance(new_name, str) and new_name.isalpha():
      self._name = new_name
    else:
      print("Please enter a valid name.")

my_dog = Dog("Nora", 8)
print("My dog is:", my_dog.get_name())

my_dog.set_name("Norita")
# my_dog.set_name("Norita324") # won't work
# my_dog.set_name(12345) # won't work
print("Her new name is:", my_dog.get_name())


class Backpack2:
  def __init__(self):
    self._items = []

  def get_items(self):
    return self._items

  def set_items(self, new_items):
    if isinstance(new_items, list):
      self._items = new_items
    else:
      print("Please enter a valid list of items")

my_backpack = Backpack2()
print(my_backpack.get_items())

# my_backpack.set_items(["Water Bottle", "Sleeping Bag", "First Aid Kit"])
my_backpack.set_items("Hello, World!") # won't work
print(my_backpack.get_items())
print("==================")

#PROPERTIES
class Circle:
  # constant variables should be written in uppercase letters (convention):
  VALID_COLORS = ["red", "green", "blue"]
#(NOTE: above we have a list, that works as a [tuple])
  
  def __init__(self, radius, color):
    self._radius = radius
    self._color = color

# defining the getter:
  def get_radius(self):
    return self._radius

# defining the setter:
  def set_radius(self, new_radius):
    if isinstance(new_radius, float) and new_radius > 0:
      self._radius = new_radius
    else:
      print("Please enter a valid number.")

  #set the property
  radius = property(get_radius, set_radius)

  def get_color(self):
    return self._color

  def set_color(self, new_color):
    if new_color in Circle.VALID_COLORS:
      self._color = new_color
    else:
      print("Please enter a valid color.")
# we normally call the property with the same name the variable we want to protect:
  color = property(get_color, set_color)

my_circle = Circle(10, "blue")
# radius
print(my_circle.radius)
my_circle.radius = 16
print(my_circle.radius)

my_circle = Circle(7.0, "red")
print("My circle radius is:", my_circle.get_radius())

my_circle.set_radius(9.2)
print("My new circle radius is:", my_circle.get_radius())


print("==================")
class Movie2:
  def __init__(self, title, rating):
    self.title = title
    self._rating = rating
    
  @property
  def rating(self):
    print("Calling the getter.")
    return self._rating

  @rating.setter
  def rating(self, new_rating):
    print("Calling the setter...")
    if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
      self._rating = new_rating
    else:
      print("Please enter a valid rating.")

favorite_movie = Movie2("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie


class Backpack3:
  def __init__(self):
    self._items = []

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, new_items):
    if isinstance(new_items, list):
      self._items = new_items
    else:
      print("Please enter a valid list of items.")

print("==================")
my_backpack = Backpack3()
print(my_backpack.items)
my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)
my_backpack.items = "Hello World"
print(my_backpack.items)
    

print("==================")

# @property X property()
class BouncyBall:
  def __init__(self, price, size, brand):
    self._price = price
    self._size = size 
    self._brand = brand
  
  # @property
  @property
  def price(self):
    return self._price
    
  @price.setter
  def price(self, new_price):
    if new_price > 0:
      print("setter activated")
      self._price = new_price

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, new_size):
    if new_size in ["small", "medium", "large"]:
      self._size = new_size

  @property
  def brand(self):
    return self._brand

  @brand.setter
  def brand(self, new_brand):
    if isinstance(new_brand, str) and new_brand:
      self._brand = new_brand

  
  # property ()  
  # def get_price(self):
  #   return self._price

  # def set_price(self, price):
  #   if price > 0:
  #     self._price = price

  # price = property(get_price, set_price)

  # def get_size(self):
  #   return self._size

  # def set_size(self, size):
  #   if size in ["small", "medium", "large"]:
  #     self._size = size

  # size = property(get_size, set_size)

  # def get_brand(self):
  #   return self._brand

  # def set_brand(self, brand):
  #   if isinstance(brand, str) and brand:
  #     self._brand = brand

  # brand = property(get_brand, set_brand)
  

ball = BouncyBall("öo", "c", 2)
print(ball._price)
print(ball._size)
print(ball._brand)
