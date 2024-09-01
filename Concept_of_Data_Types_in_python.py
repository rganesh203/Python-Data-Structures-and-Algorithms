Here is a detailed breakdown of all major data types in Python:

1. Numeric Types:
int: Represents whole numbers, both positive and negative, with no fractional component.
python
Copy code
x = 10
y = -5
float: Represents numbers that have a fractional part, written with a decimal point.
python
Copy code
a = 3.14
b = -0.001
complex: Represents complex numbers with real and imaginary components.
python
Copy code
z = 3 + 4j  # 3 is the real part, 4j is the imaginary part
2. Boolean Type:
bool: Represents truth values True or False. Typically used for conditions and comparisons.
python
Copy code
is_active = True
is_valid = False
3. Sequence Types:
str: Represents a sequence of characters, used for storing text.
python
Copy code
name = "Alice"
message = 'Hello, World!'
list: Represents an ordered, mutable collection of items, which can be of different types.
python
Copy code
numbers = [1, 2, 3, 4]
mixed = [1, "apple", True]
tuple: Represents an ordered, immutable collection of items. Once created, tuples cannot be modified.
python
Copy code
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")
range: Represents an immutable sequence of numbers, typically used for looping.
python
Copy code
r = range(1, 10)  # Sequence from 1 to 9
4. Mapping Type:
dict: Represents a collection of key-value pairs, where each key is unique, and values can be of any type.
python
Copy code
person = {"name": "Alice", "age": 30, "job": "Engineer"}
5. Set Types:
set: Represents an unordered collection of unique items. Sets do not allow duplicates.
python
Copy code
unique_numbers = {1, 2, 3, 4}
frozenset: Immutable version of a set. Once created, you cannot add or remove elements.
python
Copy code
frozen_numbers = frozenset([1, 2, 3, 4])
6. None Type:
NoneType: Represents the absence of a value or a null value. Commonly used for default values or when no value is assigned.
python
Copy code
x = None
7. Binary Types:
bytes: Represents immutable sequences of bytes, typically used for binary data.
python
Copy code
b = b"hello"
bytearray: Mutable sequence of bytes. It can be modified after creation.
python
Copy code
ba = bytearray(b"hello")
ba[0] = 104  # Modifies the first byte
memoryview: Provides a memory view of a binary object, allowing you to work with slices of the binary data without copying it.
python
Copy code
mv = memoryview(b"hello")
8. Callable Types:
function: A function is a block of code that can be executed when called.
python
Copy code
def add(a, b):
    return a + b
lambda: A shorthand way of defining anonymous functions (functions without a name).
python
Copy code
add = lambda x, y: x + y
9. Iterator Types:
iterators: Objects that implement the iterator protocol, meaning they provide methods __iter__() and __next__().
python
Copy code
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # Output: 1
10. Modules:
module: A file containing Python code that can be imported and reused in other scripts.
python
Copy code
import math
print(math.sqrt(16))
11. Custom Types:
Classes and Objects: You can define your own data types using classes in Python, enabling object-oriented programming.
python
Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
Each of these types serves a different purpose in Python, and understanding when and how to use them is key to effective programming in the language. Python's dynamic typing allows variables to change types as needed, but it's important to be mindful of the types you're working with to avoid unexpected behavior.
