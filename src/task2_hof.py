"""
Lab 3 Task 2: Higher-Order Function Implementation
Implement these WITHOUT using built-in map, filter, reduce.
"""
from typing import TypeVar, Callable, Iterator, List, Any

T = TypeVar('T')
U = TypeVar('U')

def my_map(func: Callable[[T], U], iterable: Iterator[T]) -> Iterator[U]:
    """Apply func to each element. Must return a generator."""
    # YOUR CODE HERE
    pass

def my_filter(predicate: Callable[[T], bool], iterable: Iterator[T]) -> Iterator[T]:
    """Keep elements where predicate is True. Must return a generator."""
    # YOUR CODE HERE
    pass

def my_reduce(func: Callable[[U, T], U], iterable: Iterator[T], initial: U) -> U:
    """Reduce iterable to single value using func."""
    # YOUR CODE HERE
    pass

def my_zip_with(func: Callable[[T, U], Any], iter1: Iterator[T], iter2: Iterator[U]) -> Iterator[Any]:
    """Combine two iterables element-wise using func."""
    # YOUR CODE HERE
    pass

def compose(*funcs: Callable) -> Callable:
    """Compose functions right-to-left: compose(f, g)(x) = f(g(x))

    Args:
        *funcs: Two or more functions to compose

    Returns:
        A new function that applies the input functions from right to left

    Example:
        double = lambda x: x * 2
        increment = lambda x: x + 1
        composed = compose(double, increment)
        composed(5) == 12  # double(increment(5))
    """
    # TODO: Implement function composition
    raise NotImplementedError("compose not yet implemented")

# Tests
if __name__ == "__main__":
    # Test my_map
    result = list(my_map(lambda x: x * 2, iter([1, 2, 3])))
    print(f"my_map double: {result}")  # [2, 4, 6]
    
    # Test my_filter
    result = list(my_filter(lambda x: x % 2 == 0, iter([1, 2, 3, 4])))
    print(f"my_filter even: {result}")  # [2, 4]
    
    # Test my_reduce
    result = my_reduce(lambda acc, x: acc + x, iter([1, 2, 3, 4]), 0)
    print(f"my_reduce sum: {result}")  # 10
