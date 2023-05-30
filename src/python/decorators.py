"""
This ia a decorator example. Decorators are used to modify the behavior of a function or class.
In this example, the announce decorator is used to print a message before and after the hello function is called.

The @announce syntax is equivalent to calling announce(hello) and assigning the return value to hello.

The wrapper function is a closure because it captures the variable f from the enclosing scope.

The wrapper function is a decorator because it "wraps" another function.

The wrapper function is a decorator factory because it returns a decorator.

The hello function is a decorated function because it is wrapped by a decorator.

"""


def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")

    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()
