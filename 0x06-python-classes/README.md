# 0x06. Python - Classes and Objects
`Python`
`OOP`

[Object Oriented Programming](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

# Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## Resources

**Read or watch:**
 * [Object Oriented Programming](https://intranet.alxswe.com/rltoken/i49z6HxrBGRNnixo7ZWbEQ) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and staticmethod yet)
 * [Object-Oriented Programming](https://intranet.alxswe.com/rltoken/qz3KSn154ia4H2DPaabOzg) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The`__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
 * [Properties vs. Getters and Setters](https://intranet.alxswe.com/rltoken/Wy2djWXK5b4rnnYlAq_wlA)
 * [Learn to Program 9 : Object Oriented Programming](https://intranet.alxswe.com/rltoken/MxIOanLf5vG5QeCWek2nqQ)
* [Python Classes and Objects](https://intranet.alxswe.com/rltoken/AoLH4xp5StrQST-Cu0Fg8w)
 * [Object Oriented Programming](https://intranet.alxswe.com/rltoken/-vVnWzwR3a3X0H8Oia78Ug)

# Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/WxAcwZ7gFDS8MKYqhB9Gzw),**without the help of Google:**

# General

* Why Python programming is awesome
 * What is OOP
 * “first-class everything”
 * What is a class
 * What is an object and an instance
 * What is the difference between a class and an object or instance
 * What is an attribute
 * What are and how to use public, protected and private attributes
 * What is `self`
 * What is a method
 * What is the special `__init__` method and how to use it
 * What is Data Abstraction, Data Encapsulation, and Information Hiding
 * What is a property
 * What is the difference between an attribute and a property in Python
 * What is the Pythonic way to write getters and setters in Python
 * How to dynamically create arbitrary new attributes for existing instances of a class
 * How to bind attributes to object and classes
 * What is the `__dict__` of a class and/or instance of a class and what does it contain
 * How does Python find the attributes of an object or class
 * How to use the `getattr` function

# Requirements

## General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.\*)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (**inside and outside a class**) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# More Info

**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://intranet.alxswe.com/rltoken/dOO785g5EQYkRU2E1wri0g)


### Quiz questions

**Question #0**

In this following code, what is `is_new`?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
⚪ A private instance attribute

⚪ A public class attribute

⚪ A protected class attribute

⚪ A protected instance attribute

⚪ A private class attribute

🟢 A public instance attribute

**Question #1**

In this following code, what is `User`?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
⚪ An instance

⚪ A method

⚪ An attribute

🟢 A class

⚪ A string

**Question #2**

In this following code, what is `id`?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
⚪ A protected class attribute

⚪ A public instance attribute

⚪ A public class method

⚪ A public instance method

⚪A private class attribute

🟢 A public class attribute

**Question #3**

What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>>
>>> u = User("John")
>>> u.name
```
🟢 John

⚪ no name

⚪ name

⚪ None

**Question #4**

What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>>
>>> u = User()
>>> u.is_new
```
⚪ False

🟢 True

⚪ is\_new

⚪ Nothing

**Question #5**

In this following code, what is `__password`?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
⚪ A private instance attribute

⚪ A public class attribute

⚪ A protected class attribute

⚪ A protected instance attribute

🟢 A private class attribute

⚪ A public instance attribute

**Question #6**

What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>>
>>> u = User()
>>> u.id
```
⚪ User.id

⚪ Nothing

🟢 89

⚪ id

**Question #7**

What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```
⚪ John

🟢 no name

⚪ name

⚪ None

Happy coding🎆
