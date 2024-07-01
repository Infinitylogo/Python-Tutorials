"""
In Python, a decorator is a design pattern that allows you to modify or extend the behavior of callable objects 
(functions, methods, or classes) without permanently modifying their code. Decorators are widely used in frameworks 
like Flask, Django, and others to add functionality to functions or methods in a clean and readable way.
"""

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def greet():
    return 'Hello, World!'

message = greet()
print(message)

#Generators :--
"""
A generator in Python is a special type of iterator that generates values on-the-fly. 
Unlike normal functions that return a single value using return, generators use yield 
to produce a sequence of values lazily, one at a time, and only when requested. 
This makes generators memory-efficient and particularly useful for dealing with 
large datasets or infinite sequences.
"""
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to print the first 10 Fibonacci numbers
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen), end=" ->> ")

