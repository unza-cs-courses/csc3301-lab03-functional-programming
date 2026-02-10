"""
Lab 3 Task 1: Basic Functional Programming Concepts
Explore first-class functions, lambda expressions, closures, and function returns.
"""
from typing import Callable, Any


# First-Class Functions - Functions as values
def apply_twice(func: Callable[[int], int], value: int) -> int:
    """
    Demonstrates that functions are first-class objects.
    Apply the given function twice to the value.

    Args:
        func: A function that takes an int and returns an int
        value: The initial value

    Returns:
        The result of applying func twice

    Example:
        apply_twice(lambda x: x * 2, 5) == 20  # 5 -> 10 -> 20
    """
    # YOUR CODE HERE
    pass


# Lambda Expressions - Anonymous functions
def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a multiplier function using a lambda.

    Args:
        factor: The number to multiply by

    Returns:
        A function that multiplies its input by factor

    Example:
        double = create_multiplier(2)
        double(5) == 10
    """
    # YOUR CODE HERE
    pass


def create_adder(addend: int) -> Callable[[int], int]:
    """
    Create an adder function using a lambda.

    Args:
        addend: The number to add

    Returns:
        A function that adds addend to its input

    Example:
        add_three = create_adder(3)
        add_three(5) == 8
    """
    # YOUR CODE HERE
    pass


# Closures - Functions capturing variables from their defining scope
def make_counter() -> Callable[[], int]:
    """
    Create a counter function using closure.
    Each call to the returned function increments and returns a count.

    Returns:
        A function with no parameters that returns the current count

    Example:
        counter = make_counter()
        counter() == 1
        counter() == 2
        counter() == 3
    """
    # YOUR CODE HERE
    pass


def make_multiplier_with_limit(factor: int, max_multiplier: int) -> Callable[[int], int]:
    """
    Create a multiplier that caps the result at max_multiplier.
    Demonstrates closure capturing multiple variables.

    Args:
        factor: The number to multiply by
        max_multiplier: The maximum result value

    Returns:
        A function that multiplies by factor but returns at most max_multiplier

    Example:
        limited_double = make_multiplier_with_limit(2, 10)
        limited_double(3) == 6   # 3 * 2 = 6
        limited_double(8) == 10  # 8 * 2 = 16, but capped at 10
    """
    # YOUR CODE HERE
    pass


# Functions returning functions
def make_operation(op: str) -> Callable[[int, int], int]:
    """
    Return a function that performs the specified operation.

    Args:
        op: One of '+', '-', '*', '/'

    Returns:
        A function that performs the operation on two integers

    Example:
        add = make_operation('+')
        add(5, 3) == 8

        multiply = make_operation('*')
        multiply(5, 3) == 15
    """
    # YOUR CODE HERE
    pass


def compose_simple(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:
    """
    Compose two simple functions: (f ∘ g)(x) = f(g(x))

    Args:
        f: The outer function
        g: The inner function

    Returns:
        A function that applies g then f

    Example:
        double = lambda x: x * 2
        increment = lambda x: x + 1
        composed = compose_simple(double, increment)
        composed(5) == 12  # double(increment(5)) = double(6) = 12
    """
    # YOUR CODE HERE
    pass


def apply_in_sequence(value: Any, *funcs: Callable) -> Any:
    """
    Apply a sequence of functions to a value, left-to-right.
    (apply_in_sequence(x, f, g, h) = h(g(f(x))))

    Args:
        value: The initial value
        *funcs: Variable number of functions to apply

    Returns:
        The result of applying all functions in order

    Example:
        result = apply_in_sequence(5, lambda x: x + 1, lambda x: x * 2)
        result == 12  # (5 + 1) * 2
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    # Test first-class functions
    print("Testing apply_twice:")
    result = apply_twice(lambda x: x * 2, 5)
    print(f"  apply_twice(double, 5) = {result}")  # Expected: 20

    # Test lambda expressions
    print("\nTesting lambda expressions:")
    double = create_multiplier(2)
    print(f"  double(5) = {double(5)}")  # Expected: 10

    add_three = create_adder(3)
    print(f"  add_three(5) = {add_three(5)}")  # Expected: 8

    # Test closures
    print("\nTesting closures:")
    counter = make_counter()
    print(f"  counter() = {counter()}")  # Expected: 1
    print(f"  counter() = {counter()}")  # Expected: 2
    print(f"  counter() = {counter()}")  # Expected: 3

    # Test function composition
    print("\nTesting composition:")
    double = lambda x: x * 2
    increment = lambda x: x + 1
    composed = compose_simple(double, increment)
    print(f"  compose_simple(double, increment)(5) = {composed(5)}")  # Expected: 12
