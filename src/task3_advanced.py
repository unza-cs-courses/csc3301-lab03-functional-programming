"""
Lab 3 Task 3: Advanced Functional Programming Concepts
Explore currying, partial application, lazy evaluation, function pipelines, and memoization.
"""
from typing import Callable, TypeVar, Iterator, Dict, Any
from functools import wraps

T = TypeVar('T')
U = TypeVar('U')


# Currying - Converting a function of multiple arguments into a chain of functions
def curry(func: Callable) -> Callable:
    """
    Convert a function with multiple arguments into a curried function.
    A curried function takes one argument at a time and returns a new function
    that takes the next argument, until all arguments are satisfied.

    Args:
        func: A function with multiple parameters

    Returns:
        A curried version of the function

    Example:
        def add(a, b, c):
            return a + b + c

        curried_add = curry(add)
        add_one = curried_add(1)
        add_one_and_two = add_one(2)
        result = add_one_and_two(3)  # 6
    """
    # YOUR CODE HERE
    pass


def partial(func: Callable, *args) -> Callable:
    """
    Create a partial application of a function by fixing some arguments.

    Args:
        func: The function to partially apply
        *args: The arguments to fix

    Returns:
        A new function that takes the remaining arguments

    Example:
        def multiply(a, b, c):
            return a * b * c

        double_and_multiply = partial(multiply, 2)
        result = double_and_multiply(3, 4)  # 2 * 3 * 4 = 24
    """
    # YOUR CODE HERE
    pass


# Lazy Evaluation - Computing values only when needed
def lazy_range(start: int, end: int) -> Iterator[int]:
    """
    Create a lazy range iterator that yields values on demand.
    This doesn't compute all values upfront like range().

    Args:
        start: The starting number (inclusive)
        end: The ending number (exclusive)

    Yields:
        Integers from start to end-1

    Example:
        lazy = lazy_range(1, 1000000)
        first = next(lazy)  # Only computes 1
        second = next(lazy)  # Only computes 2
    """
    # YOUR CODE HERE
    pass


def take(n: int, iterable: Iterator[T]) -> list:
    """
    Take the first n elements from an iterator.
    Useful for working with infinite or large lazy sequences.

    Args:
        n: Number of elements to take
        iterable: An iterator to take from

    Returns:
        A list of the first n elements

    Example:
        naturals = lazy_range(1, 100000)
        first_five = take(5, naturals)  # [1, 2, 3, 4, 5]
    """
    # YOUR CODE HERE
    pass


def pipe(*funcs: Callable) -> Callable:
    """
    Create a function pipeline that applies functions left-to-right.
    pipe(f, g, h)(x) = h(g(f(x)))

    Args:
        *funcs: Two or more functions to pipeline

    Returns:
        A new function that applies all functions left-to-right

    Example:
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        square = lambda x: x ** 2

        pipeline = pipe(add_one, double, square)
        pipeline(5) == 144  # ((5+1)*2)^2 = (12)^2 = 144
    """
    # YOUR CODE HERE
    pass


# Memoization - Cache function results to avoid recomputation
def memoize(func: Callable) -> Callable:
    """
    Decorator that caches function results based on arguments.
    Subsequent calls with the same arguments return the cached result.

    Args:
        func: The function to memoize

    Returns:
        A memoized version of the function

    Example:
        call_count = 0

        @memoize
        def expensive_computation(n):
            global call_count
            call_count += 1
            return n * n

        expensive_computation(5)  # Computed, call_count = 1
        expensive_computation(5)  # Returned from cache, call_count = 1
        expensive_computation(6)  # Computed, call_count = 2
    """
    # YOUR CODE HERE
    pass


def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number efficiently using memoization.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Example:
        fibonacci(0) == 0
        fibonacci(1) == 1
        fibonacci(5) == 5
        fibonacci(10) == 55
    """
    # YOUR CODE HERE
    pass


class Pipeline:
    """
    A class-based pipeline builder for functional composition.
    Allows chaining transformations in a fluent style.

    Example:
        result = (Pipeline(5)
                  .apply(lambda x: x + 1)
                  .apply(lambda x: x * 2)
                  .get_value())
        result == 12  # (5+1)*2
    """

    def __init__(self, value: Any):
        """Initialize the pipeline with an initial value."""
        self._value = value

    def apply(self, func: Callable) -> 'Pipeline':
        """
        Apply a function to the current value and return self for chaining.

        Args:
            func: A function to apply

        Returns:
            Self for method chaining
        """
        # YOUR CODE HERE
        pass

    def get_value(self) -> Any:
        """Get the final value from the pipeline."""
        return self._value


# Higher-order function utilities
def repeatedly(n: int, func: Callable) -> Callable:
    """
    Create a function that applies func to its input n times.

    Args:
        n: Number of times to repeat
        func: The function to repeat

    Returns:
        A function that applies func n times

    Example:
        double_thrice = repeatedly(3, lambda x: x * 2)
        double_thrice(1) == 8  # 1 * 2 * 2 * 2
    """
    # YOUR CODE HERE
    pass


def until(predicate: Callable[[T], bool], func: Callable[[T], T]) -> Callable[[T], T]:
    """
    Create a function that repeatedly applies func until predicate is true.

    Args:
        predicate: A function that returns True when to stop
        func: The function to repeatedly apply

    Returns:
        A function that applies func until predicate is satisfied

    Example:
        is_even = lambda x: x % 2 == 0
        double = lambda x: x * 2

        apply_until_even = until(is_even, double)
        apply_until_even(3) == 12  # 3->6->12 (12 is even)
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    print("Testing currying:")
    def add3(a, b, c):
        return a + b + c

    curried_add = curry(add3)
    add1 = curried_add(1)
    add1_2 = add1(2)
    result = add1_2(3)
    print(f"  curry(add)(1)(2)(3) = {result}")  # Expected: 6

    print("\nTesting lazy evaluation:")
    lazy = lazy_range(1, 10)
    first_three = take(3, lazy)
    print(f"  take(3, lazy_range(1, 10)) = {first_three}")  # Expected: [1, 2, 3]

    print("\nTesting pipe:")
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x ** 2

    pipeline = pipe(add_one, double, square)
    result = pipeline(5)
    print(f"  pipe(+1, *2, ^2)(5) = {result}")  # Expected: 144

    print("\nTesting memoization:")
    call_count = 0

    @memoize
    def expensive(n):
        global call_count
        call_count += 1
        return n * n

    print(f"  First call expensive(5): {expensive(5)}, call_count = {call_count}")
    print(f"  Second call expensive(5): {expensive(5)}, call_count = {call_count}")

    print("\nTesting Pipeline class:")
    result = (Pipeline(5)
              .apply(lambda x: x + 1)
              .apply(lambda x: x * 2)
              .get_value())
    print(f"  Pipeline(5).apply(+1).apply(*2).get_value() = {result}")  # Expected: 12
